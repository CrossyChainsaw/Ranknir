from secrets import get_keys
import os
from pydoc import classname
import re
import discord
from discord.ext import commands
from discord.ext import tasks
import time
import json
from api import fetch_clan
from api import fetch_player_ranked_stats
from keep_alive import keep_alive
from order_teamname import ArrangeTeamName
from send_embeds import send_embeds
from get_members_2v2_elo import get_members_2v2_elo
from sort_players_elo import sort_players_elo
from wait import wait

# Skyward
skyward_elo_channel_id = 976552050953437194
skyward_clan_id = '84648'
skyward_color = 0x289fb4
skyward_image = 'https://cdn.discordapp.com/attachments/841405262023884820/841405879496212530/Skyward-1.png'

# Insomnia
insomnia_elo_channel_id = 1006780905131614280
insomnia_clan_id = '1919781'
insomnia_color = 0x301834
insomnia_image = "https://cdn.discordapp.com/attachments/967468594285924382/1006783742179823646/Insomnia_Logo_Concept_Purple.png"

# Testing
test_channel_id = 973594560368373820

# insomnia_clan_id, insomnia_elo_channel_id, insomnia_image
# skyward_clan_id, skyward_elo_channel_id, skyward_image

bot = commands.Bot(command_prefix=['r', 'R'])


@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    skyward_log_channel_id = bot.get_channel(973594560368373820)
    await skyward_log_channel_id.send("I'm back online!")
    while True:
        await main(insomnia_clan_id, insomnia_elo_channel_id, insomnia_image, insomnia_color)
        wait(2500)
        await main(insomnia_clan_id, insomnia_elo_channel_id, insomnia_image, insomnia_color)
        wait(2500)


async def main(clan_id, channel_id, clan_image, clan_color):
    # get teams, current and peak elo's sorted
    return_values = sort_players_elo(clan_id)
    clan_2v2_teamnames_sorted = return_values[0]
    clan_current_2v2_ratings_sorted = return_values[1]
    clan_peak_2v2_ratings_sorted = return_values[2]
    clan = return_values[3]

    # prepare embeds - make this a diff method
    embed2 = discord.Embed(title=clan['clan_name'],
                           description="Total Exp: " + str(clan['clan_xp']),
                           color=clan_color)
    embed3 = discord.Embed(description="", color=clan_color)
    embed4 = discord.Embed(description="", color=clan_color)
    embed5 = discord.Embed(description="", color=clan_color)
    global num
    num = 1
    for (current, peak, currentTeam) in zip(clan_current_2v2_ratings_sorted,
                                            clan_peak_2v2_ratings_sorted,
                                            clan_2v2_teamnames_sorted):
        if num <= 20:
            embed3.description += "**" + \
                str(num) + ". " + currentTeam + "**: **current:** " + \
                str(current) + " **peak:** " + str(peak) + '\n'
        elif num <= 40:
            embed4.description += "**" + \
                str(num) + ". " + currentTeam + "**: **current:** " + \
                str(current) + " **peak:** " + str(peak) + '\n'
        else:
            embed5.description += "**" + \
                str(num) + ". " + currentTeam + "**: **current:** " + \
                str(current) + " **peak:** " + str(peak) + '\n'
        num += 1
    await send_embeds(embed2=embed2,
                      embed3=embed3,
                      embed4=embed4,
                      embed5=embed5,
                      bot=bot, channel_id=channel_id, clan_image=clan_image)

    # clear embeds for some reason
    clan_current_2v2_ratings_sorted.clear()
    clan_peak_2v2_ratings_sorted.clear()
    clan_2v2_teamnames_sorted.clear()


keep_alive()
bot.run(get_keys(0))