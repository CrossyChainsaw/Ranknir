import os
from pydoc import classname
import re
from secrets import get_keys
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

bot = commands.Bot(command_prefix=['r', 'R'])


@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    log_channel = bot.get_channel(973594560368373820)
    await log_channel.send("I'm back online!")
    while True:
        await main()
        print('start waiting')
        time.sleep(2500)
        print('done waiting')


async def main():
    # get teams, current and peak elo's sorted
    return_values = sort_players_elo()
    clan_2v2_teamnames_sorted = return_values[0]
    clan_current_2v2_ratings_sorted = return_values[1]
    clan_peak_2v2_ratings_sorted = return_values[2]
    clan = return_values[3]

    # prepare embeds
    embed2 = discord.Embed(title="Skyward",
                           description="Total Exp: " + str(clan['clan_xp']),
                           color=0x289fb4)
    embed3 = discord.Embed(description="", color=0x289fb4)
    embed4 = discord.Embed(description="", color=0x289fb4)
    embed5 = discord.Embed(description="", color=0x289fb4)
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
                      embed5=embed5, bot=bot)

    # clear embeds for some reason
    clan_current_2v2_ratings_sorted.clear()
    clan_peak_2v2_ratings_sorted.clear()
    clan_2v2_teamnames_sorted.clear()


keep_alive()
bot.run(get_keys(0))
