import discord
from discord import Embed
import asyncio
from Ranknir.modules.data_management import FlagType, ServerIDs, RegionFlagEmojis, CountryFlagEmojis, LegendEmojis
from Ranknir.classes.Player import Player
from Ranknir.classes.Team import Team
from Ranknir.classes.Clan import Clan
from Ranknir.classes.Server import Server

PURGE_LIMIT = 12  # 12
SEND_ELO_EMBEDS_WAIT_TIME = 4.8 # 4.8 works
BOT_WAIT_TIME = 2.8 # 2.8 works
PLAYERS_PER_EMBED = 20 #20 usually worked


def prepare_embeds_clan_mix_console(clan:Clan, entities_sorted:list[Player|Team], clan_data_array, console_player_amount):
    
    # TITLE EMBED
    title_embed = Embed(title='', description='', color=clan.color)
    title_embed = __add_title(clan_data_array, title_embed)
    if clan.show_member_count:
        title_embed = __add_member_count(clan_data_array, title_embed, console_player_amount, entities_sorted)
    if clan.show_xp:
        title_embed = __add_xp(clan_data_array, title_embed)
    
    # LEADERBOARD EMBEDS
    embed_array = []
    rank = 1
    count = 0
    # PLAYER ITERATION
    for entity in entities_sorted:
        # CREATE NEW EMBED
        if count == 0:
            embed = Embed(description="", color=clan.color)
        # FILL WITH PLAYERS/TEAMS
        if count < PLAYERS_PER_EMBED:
            
            # Add Legend Emoji
            if clan.show_legends:
                embed.description += __add_legend_emoji(entity, clan)
            
            # Format Teamname
            if isinstance(entity, Team):
                entity.name = __format_teamname(entity)
            
            # Add Player Information
            embed.description += __add_rank_name_current_peak(rank, entity)
            
            # Add Win Loss
            if clan.show_win_loss:
                embed.description += __add_player_win_loss(entity)

            # Add Newline
            embed.description += "\n"

        # APPEND EMBED AND RESET LOOP
        if count == PLAYERS_PER_EMBED:
            embed_array.append(embed)
            count = 0
        rank += 1
        count += 1
    embed_array.append(embed)
    return title_embed, embed_array


def __add_legend_emoji(entity:Player|Team, server:Server) -> str:
    if isinstance(entity, Player):
        if server.show_legends:
            player:Player = entity
            legend_emoji = getattr(LegendEmojis, player.legend).value
            return f"{legend_emoji} "
    elif isinstance(entity, Team):
        if server.show_legends:    
            legend_emoji = getattr(LegendEmojis, entity.legend).value
            mate_legend_emoji = getattr(LegendEmojis, entity.mate_legend).value
            return f"{legend_emoji}{mate_legend_emoji} "


def prepare_embeds_server(server:Server, entities_sorted:list[Player|Team]):
    
    # TITLE EMBED
    title_embed = Embed(title=server.leaderboard_title, description='', color=server.color)
    if server.show_member_count:
        title_embed = __add_member_count([{"clan": []}], title_embed, 0, entities_sorted)
    
    # LEADERBOARD EMBEDS
    embed_array = []
    rank = 1
    count = 0
    # PLAYER ITERATION - entity is either type Player or Team
    for entity in entities_sorted:
        if count == 0:
            embed = Embed(description="", color=server.color)
        if count < PLAYERS_PER_EMBED:

            # Add Flag
            if server.flag_type is not FlagType.NONE.value:
                embed.description += __add_flag_emoji(server, embed, entity)
            
            # Add Legend Emoji
            if server.show_legends:
                embed.description += __add_legend_emoji(entity, server)
            
            # Format Teamname
            if isinstance(entity, Team):
                entity.name = __format_teamname(entity)
            
            # Add Player Information
            embed.description += __add_rank_name_current_peak(rank, entity)
            
            # Add Win Loss
            if server.show_win_loss:
                embed.description += __add_player_win_loss(entity)

            # Add Newline
            embed.description += "\n"

        # APPEND EMBED AND RESET LOOP
        if count == PLAYERS_PER_EMBED:
            embed_array.append(embed)
            count = 0
        rank += 1
        count += 1
    embed_array.append(embed)
    return title_embed, embed_array


async def send_embeds(embed_title, embed_array, bot, clan: Clan, channel_id):
    channel = bot.get_channel(channel_id)
    print('Target Channel: ' + channel.name)

    # Remove last FEW messages in channel
    print('purging...')
    await channel.purge(limit=PURGE_LIMIT)  # CHANGE TO 12

    await asyncio.sleep(BOT_WAIT_TIME)

    # Send Image
    try:
        await channel.send(clan.image)
        print("sent clan image")
    except:
        print('NO IMAGE PROVIDED')

    await asyncio.sleep(BOT_WAIT_TIME)

    # Send Embed
    await channel.send(embed=embed_title)
    print("sent title embed")

    await asyncio.sleep(BOT_WAIT_TIME)

    num = 1
    print('embed_array length: ' + str(len(embed_array)))
    for embed in embed_array:
        # Send Embed (if possible)
        if len(embed.description) > 0:
            await channel.send(embed=embed)
            print('sent player embed: ' + str(num))
            await asyncio.sleep(SEND_ELO_EMBEDS_WAIT_TIME)
        num += 1


def __add_player_win_loss(player:Player) -> str:
    return f" **[**{player.total_wins}W**/**{player.total_losses}L**]**"

def __add_rank_name_current_peak(rank, player:Player) -> str:
    return f"**{rank}.** **{player.name}**: current: **{player.current}** peak: **{player.peak}**"

def __set_default_flag(server:Server) -> str:
    # Set Default Flag
    if server.id == ServerIDs.BHNL:
        return CountryFlagEmojis.NL.value
    elif server.id == ServerIDs.M30W:
        return RegionFlagEmojis.USE.value

def __add_flag_emoji(server:Server, embed:Embed, player:Player) -> str:
    flag_source = __get_flag_source(server, player)
    default_flag = __set_default_flag(server)
    if server.flag_type == FlagType.COUNTRY.value or server.flag_type == FlagType.ETHNICITY.value:
        flag = default_flag
        for CountryFlagEmoji in CountryFlagEmojis:
            if flag_source == CountryFlagEmoji.name:
                flag = CountryFlagEmoji.value
        return f"{flag} "
    elif server.flag_type == FlagType.REGION.value:
        flag = default_flag
        for RegionFlagEmoji in RegionFlagEmojis:
            if flag_source == RegionFlagEmoji.name:
                flag = RegionFlagEmoji.value
        return f"{flag} "
    else:
        return ""

def __add_title(clan_data_array, embed2):
    if len(clan_data_array) == 1:
        embed2.title += clan_data_array[0]['clan_name']
        return embed2
    if len(clan_data_array) > 1:
        # Title
        count = 0
        for clan in clan_data_array:
            if count == 0:
                embed2.title += clan['clan_name']
            else:
                embed2.title += " & " + clan_data_array[count]['clan_name']
            count += 1
        return embed2

def __add_member_count(clan_data_array, title_embed, console_player_amount, players_sorted: list[Player]) -> Embed:
    title_embed.description += "\n\n"
    if len(clan_data_array) == 1:
        title_embed.description = '**Member Count\n**'
        title_embed.description += "Total: %s" % (str(len(players_sorted)))
        return title_embed
    if len(clan_data_array) > 1:
        title_embed.description += '**Member Count\n**'
        count = 0
        total_member_count = 0
        for clan in clan_data_array:
            member_count = len(clan['clan'])
            total_member_count += member_count
            if count == 0:
                title_embed.description += clan['clan_name'] + ": " + str(
                    member_count)
            else:
                title_embed.description += "\n" + clan_data_array[count][
                    'clan_name'] + ": " + str(member_count)
            count += 1
        if console_player_amount > 0:
            title_embed.description += "\n" + \
                "Console: " + str(console_player_amount)
        title_embed.description += "\nTotal: " + \
            str(total_member_count + console_player_amount)
        return title_embed

def __add_xp(clan_data_array, embed):
    embed.description += "\n\n"
    if len(clan_data_array) == 1:
        embed.description += '**Clan XP\n**'
        clan_xp = int(clan_data_array[0]['clan_xp'])
        clan_xp_reformatted = '{:,.0f}'.format(clan_xp)
        embed.description += "Total: " + str(clan_xp_reformatted)
        return embed
    if len(clan_data_array) > 1:
        embed.description += '**Clan XP\n**'
        count = 0
        total_xp = 0
        for clan in clan_data_array:
            clan_xp = int(clan['clan_xp'])  
            total_xp += clan_xp
            if count == 0:
                embed.description += clan['clan_name'] + ": " + str('{:,.0f}'.format(clan_xp))
            else:
                embed.description += "\n" + clan_data_array[count]['clan_name'] + ": " + str('{:,.0f}'.format(clan_xp))
            count += 1
        total_xp_reformatted = '{:,.0f}'.format(total_xp)
        embed.description += "\nTotal: " + str(total_xp_reformatted)
        return embed

def __get_flag_source(server:Server, player:Player):
    if server.flag_type == FlagType.ETHNICITY.value:
        return player.ethnicity
    elif server.flag_type == FlagType.COUNTRY.value:
        return player.country
    elif server.flag_type == FlagType.REGION.value:
        return player.region
    else:
        return ""
    
def __format_teamname(team_object:Team):
    """Puts 2 asterisks after name 1, and 2 asterisks before name 2. Necessary for making the names bold when sending the embed (consider putting this in embed.py)"""
    best_team_name = team_object.name
    if '+' in best_team_name:
        name_plus_index = best_team_name.find('+')
        name_length = len(best_team_name)
        name_1 = best_team_name[0:name_plus_index]
        name_2 = best_team_name[name_plus_index + 1:name_length]
        new_name = name_1 + '** + **' + name_2
        return new_name
    else:
        return best_team_name