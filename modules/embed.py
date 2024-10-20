import discord
import asyncio
from Ranknir.modules.data_management import FlagType, ServerIDs, RegionFlagEmojis, CountryFlagEmojis, LegendEmojis
from Ranknir.classes.Player import Player
from Ranknir.classes.Team import Team
from Ranknir.classes.Clan import Clan
from Ranknir.classes.Server import Server

PURGE_LIMIT = 12  # 12
SEND_ELO_EMBEDS_WAIT_TIME = 4.9
BOT_WAIT_TIME = 2.9
PLAYERS_PER_EMBED = 20


def prepare_embeds_clan_mix_console(clan:Clan, entities_sorted:list, clan_data_array, console_player_amount):

    # for entity in entities_sorted:
    #     if isinstance(entity, Player):
    #         entities_sorted:list[Player] = entities_sorted
    #     elif isinstance(entity, Team):
    #         entities_sorted:list[Team] = entities_sorted



    # OPTIONAL ADD ONS
    embed_title = discord.Embed(title='', description='', color=clan.color)
    embed_title = __add_title(clan_data_array, embed_title)
    if clan.show_member_count:
        embed_title = __add_member_count(clan_data_array, embed_title, console_player_amount, entities_sorted)
    if clan.show_xp:
        embed_title = __add_xp(clan_data_array, embed_title)
    # Variables
    embed_array = []
    rank = 1
    count = 0
    # Format Embeds
    # if isinstance(entity, Player):
    for team in entities_sorted:
        if count == PLAYERS_PER_EMBED:
            embed_array.append(embed)
            count = 0
        if count == 0:
            embed = discord.Embed(description="", color=clan.color)
        if count < PLAYERS_PER_EMBED:
            # Add Legend
            if clan.show_legends:
                if isinstance(team, Player):
                    player:Player = team
                    legend_emoji = getattr(LegendEmojis, player.legend).value
                    embed.description += f"{legend_emoji} "
                elif isinstance(team, Team):
                    legend_emoji = getattr(LegendEmojis, team.legend).value
                    mate_legend_emoji = getattr(LegendEmojis, team.mate_legend).value
                    embed.description += f"{legend_emoji}{mate_legend_emoji} "
            # Player Information
            embed.description += __add_rank_name_current_peak(rank, team)
            
            # Add Win Loss
            if clan.show_win_loss:
                embed.description += __add_player_win_loss(team)
            
            embed.description += "\n"
        rank += 1
        count += 1
    embed_array.append(embed)
    # elif isinstance(entity, Team):
    #     for team in entities_sorted:
    #         if count == PLAYERS_PER_EMBED:
    #             embed_array.append(embed)
    #             count = 0
    #         if count == 0:
    #             embed = discord.Embed(description="", color=clan.color)
    #         if count < PLAYERS_PER_EMBED:
    #             # Add Own Legend and Teammate Legend 
    #             if clan.show_legends:
    #                 legend_emoji = getattr(LegendEmojis, team.legend).value
    #                 mate_legend_emoji = getattr(LegendEmojis, team.mate_legend).value
    #                 embed.description += f"{legend_emoji}{mate_legend_emoji} "
                
    #             # Player Information
    #             embed.description += __add_rank_name_current_peak(team)
                
    #             # Add Win Loss
    #             if clan.show_win_loss:
    #                 embed.description += __add_player_win_loss(team)
                
    #             embed.description += "\n"
    #         rank += 1
    #         count += 1
    #     embed_array.append(embed)


    return embed_title, embed_array

def __add_player_win_loss(player:Player):
    return f" **[**{player.total_wins}W**/**{player.total_losses}L**]**"
def __add_rank_name_current_peak(rank, player:Player):
    return f"**{rank}.** **{player.name}**: current: **{player.current}** peak: **{player.peak}**"


def prepare_embeds_server(server:Server, players_sorted: list[Player]):
    color2 = server.color
    embed_title = discord.Embed(title=server.leaderboard_title, description='', color=color2)
    if server.show_member_count:
        embed_title = __add_member_count([{"clan": []}], embed_title, 0, players_sorted)
    # Variables
    embed_array = []
    global rank
    rank = 1
    count = 0
    embed = discord.Embed(description="", color=color2)

    # Format Embeds
    for player in players_sorted:
        if count == 21:
            embed_array.append(embed)
            count = 0
        if count == 0:
            embed = discord.Embed(description="", color=color2)
        if count <= 20:
            if server.flag_type is not FlagType.NONE.value: # ideally if show_flags = true, append to msg, and later again append to msg
                flag_source = __get_flag_source(server, player)
                # Set Default Flag
                if server.id == ServerIDs.BHNL:
                    default_flag = CountryFlagEmojis.NL.value
                elif server.id == ServerIDs.M30W:
                    default_flag = RegionFlagEmojis.USE.value
                # Set Flag Emoji and add player
                if server.flag_type == FlagType.COUNTRY.value or server.flag_type == FlagType.ETHNICITY.value:
                    flag = default_flag
                    for CountryFlagEmoji in CountryFlagEmojis:
                        if flag_source == CountryFlagEmoji.name:
                            flag = CountryFlagEmoji.value
                    embed.description += f"{flag} **{rank}.** **{player.name}**: current: **{player.current}** peak: **{player.peak}**\n"
                elif server.flag_type == FlagType.REGION.value:
                    flag = default_flag
                    for RegionFlagEmoji in RegionFlagEmojis:
                        if flag_source == RegionFlagEmoji.name:
                            flag = RegionFlagEmoji.value
                    embed.description += f"{flag} **{rank}.** **{player.name}**: current: **{player.current}** peak: **{player.peak}**\n"
                else:
                    if flag_source == "":
                        flag = ""
                    embed.description += f"**{rank}.** {flag} **{player.name}**: current: **{player.current}** peak: **{player.peak}**\n"
            else:
                embed.description += f"**{rank}.** **{player.name}**: current: **{player.current}** peak: **{player.peak}**\n"
        rank += 1
        count += 1
    embed_array.append(embed)
    return embed_title, embed_array


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


def __add_member_count(clan_data_array, embed_title, console_player_amount, players_sorted: list[Player]):
    embed_title.description += "\n\n"
    if len(clan_data_array) == 1:
        embed_title.description = '**Member Count\n**'
        embed_title.description += "Total: %s" % (str(len(players_sorted)))
        return embed_title
    if len(clan_data_array) > 1:
        embed_title.description += '**Member Count\n**'
        count = 0
        total_member_count = 0
        for clan in clan_data_array:
            member_count = len(clan['clan'])
            total_member_count += member_count
            if count == 0:
                embed_title.description += clan['clan_name'] + ": " + str(
                    member_count)
            else:
                embed_title.description += "\n" + clan_data_array[count][
                    'clan_name'] + ": " + str(member_count)
            count += 1
        if console_player_amount > 0:
            embed_title.description += "\n" + \
                "Console: " + str(console_player_amount)
        embed_title.description += "\nTotal: " + \
            str(total_member_count + console_player_amount)
        return embed_title


def __add_xp(clan_data_array, embed2):
    embed2.description += "\n\n"
    if len(clan_data_array) == 1:
        embed2.description += '**Clan XP\n**'
        clan_xp = int(clan_data_array[0]['clan_xp'])
        clan_xp_reformatted = '{:,.0f}'.format(clan_xp)
        embed2.description += "Total: " + str(clan_xp_reformatted)
        print(clan_xp_reformatted)
        return embed2
    if len(clan_data_array) > 1:
        embed2.description += '**Clan XP\n**'
        count = 0
        total_xp = 0
        for clan in clan_data_array:
            clan_xp = int(clan['clan_xp'])  
            total_xp += clan_xp
            if count == 0:
                embed2.description += clan['clan_name'] + ": " + str('{:,.0f}'.format(clan_xp))
            else:
                embed2.description += "\n" + clan_data_array[count]['clan_name'] + ": " + str('{:,.0f}'.format(clan_xp))
            count += 1
        total_xp_reformatted = '{:,.0f}'.format(total_xp)
        embed2.description += "\nTotal: " + str(total_xp_reformatted)
        return embed2

def __get_flag_source(server:Server, player:Player):
    if server.flag_type == FlagType.ETHNICITY.value:
        return player.ethnicity
    elif server.flag_type == FlagType.COUNTRY.value:
        return player.country
    elif server.flag_type == FlagType.REGION.value:
        return player.region
    else:
        return ""