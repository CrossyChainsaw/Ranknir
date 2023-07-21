import discord
import time

PURGE_LIMIT = 0  # 12


def prepare_embeds_clan_mix_console(clan, players_sorted, clan_data_array, console_player_amount):

    # OPTIONAL ADD ONS
    embed_title = discord.Embed(title='', description='', color=clan.color)
    embed_title = __add_title(clan_data_array, embed_title)
    if clan.member_count == 'show':
        embed_title = __add_member_count(
            clan_data_array, embed_title, console_player_amount)
    if clan.xp == 'show':
        embed_title = __add_xp(clan_data_array, embed_title)
    # Variables
    embed_array = []
    global rank
    rank = 1
    count = 0
    embed = discord.Embed(description="", color=clan.color)

    # Format Embeds
    for player in players_sorted:
        if count == 21:
            embed_array.append(embed)
            count = 0
        if count == 0:
            embed = discord.Embed(description="", color=clan.color)
        if count <= 20:
            embed.description += "**%s.** **%s**: current: **%s** peak: **%s**\n" % (
                str(rank), player.name, str(player.current), str(player.peak))
        rank += 1
        count += 1
    embed_array.append(embed)

    return embed_title, embed_array


def prepare_embeds_server(server, players_sorted):
    embed_title = discord.Embed(title=server.name, color=server.color)

    # Variables
    embed_array = []
    global rank
    rank = 1
    count = 0
    embed = discord.Embed(description="", color=server.color)

    # Format Embeds
    for player in players_sorted:
        if count == 0:
            embed = discord.Embed(description="", color=server.color)
        if count <= 20:
            embed.description += "**%s.** **%s**: current: **%s** peak: **%s**\n" % (
                str(rank), player.name, str(player.current), str(player.peak))
        rank += 1
        count += 1
        if count == 21:
            embed_array.append(embed)
            count = 0
    embed_array.append(embed)
    return embed_title, embed_array


async def send_embeds(embed_title, embed_array, bot, clan, channel_id):
    channel = bot.get_channel(channel_id)
    print('this channel')
    print(channel)

    # Remove last FEW messages in channel
    await channel.purge(limit=PURGE_LIMIT)  # CHANGE TO 12

    time.sleep(1)

    # Send Image
    try:
        await channel.send(clan.image)
        print("sent clan image")
    except:
        print('NO IMAGE PROVIDED')

    time.sleep(1)

    # Send Embed
    await channel.send(embed=embed_title)
    print("sent title embed")

    time.sleep(1)

    num = 1
    print('embed_array length: ' + str(len(embed_array)))
    for embed in embed_array:
        # Send Embed (if possible)
        if len(embed.description) > 0:
            await channel.send(embed=embed)
            print('sent player embed: ' + str(num))
            time.sleep(5)
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


def __add_member_count(clan_data_array, embed_title, console_player_amount):
    embed_title.description += "\n\n"
    if len(clan_data_array) == 1:
        embed_title.description = '**Member Count\n**'
        embed_title.description += "Total: %s" % (
            str(len(clan_data_array[0]['clan']) + console_player_amount))
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
        embed2.description += "Total: " + str(clan_data_array[0]['clan_xp'])
        return embed2
    if len(clan_data_array) > 1:
        embed2.description += '**Clan XP\n**'
        count = 0
        total_xp = 0
        for clan in clan_data_array:
            clan_xp = int(clan['clan_xp'])
            total_xp += clan_xp
            if count == 0:
                embed2.description += clan['clan_name'] + ": " + str(clan_xp)
            else:
                embed2.description += "\n" + clan_data_array[count][
                    'clan_name'] + ": " + str(clan_xp)
            count += 1
        embed2.description += "\nTotal: " + str(total_xp)
        return embed2
