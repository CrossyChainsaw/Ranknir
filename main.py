import os
import os
from pydoc import classname
import discord
from discord.ext import commands
from discord.ext import tasks
import time
import json
from api import getClan
from api import getPlayerStats
from keep_alive import keep_alive
from order_teamname import ArrangeTeamName

skyward_image_link = 'https://cdn.discordapp.com/attachments/841405262023884820/841405879496212530/Skyward-1.png'
elo_channel = 976552050953437194
test_channel = 973594560368373820
using_channel = elo_channel
first_time = True
clan = []
clan_members = []
clan_current_2v2_ratings = []
clan_peak_2v2_ratings = []
clan_2v2_teamnames = []
clan_current_2v2_ratings_sorted = []
clan_peak_2v2_ratings_sorted = []
clan_2v2_teamnames_sorted = []

bot = commands.Bot(command_prefix=['r', 'R'])

@bot.event
async def on_ready():
  print(f'We have logged in as {bot.user}')
  log_channel = bot.get_channel(973594560368373820)
  await log_channel.send("I'm back online!")
  while True:
    await loop()
    time.sleep(2500)

@commands.has_role('DevOps')
@bot.command(name='start', help='starts bruh')
async def start(ctx):
    loop.start()


def get_clan():
    global clan
    try:
        clan = json.loads(getClan().content)  # request
    except:
        clan = []


def get_clan_members():
    global clan_members
    try:
        clan_members = clan['clan']
    except:
        clan_members = []


def Save2v2Elo():
    num = 0
    for player in clan_members:
        num += 1
        try:
            all_my_2v2_teams = json.loads(getPlayerStats(player["brawlhalla_id"]).content)[
                "2v2"]  # request

            # FIND BEST TEAM CURRENT ELO
            bestCurrentTeam = "bestCurrentTeam is undefined"
            bestCurrent = -1
            bestPeak = -1

            for team in all_my_2v2_teams:
                rating = team["rating"]
                peak = team["peak_rating"]
                if rating > bestCurrent:
                    bestCurrent = rating
                    bestPeak = peak
                    bestCurrentTeam = team["teamname"]

            # ADD ALL VALUES TO ARRAYS
            if bestCurrentTeam.startswith("bestCurrentTeam is undefined"):
                bestCurrent = -1
                bestPeak = -1
                bestCurrentTeam = player["name"]
            print(bestCurrentTeam)
            print("current: " + str(bestCurrent))
            print("peak: " + str(bestPeak))
            clan_2v2_teamnames.append(bestCurrentTeam)
            clan_current_2v2_ratings.append(bestCurrent)
            clan_peak_2v2_ratings.append(bestPeak)

        except:
            currentResult = "**" + \
                str(num) + ". " + player["name"] + \
                "**: **current:**" + " -1" + " **peak:**" + " -1"

            clan_2v2_teamnames.append(player["name"])
            clan_current_2v2_ratings.append(-1)
            clan_peak_2v2_ratings.append(-1)

            print(currentResult)
    time.sleep(1)


def SortPlayersElo():
    print('start sorting players elo...')
    while len(clan_current_2v2_ratings) > 0:
        index = -1
        bestIndex = 0
        highestCurrentRating = -2
        for (current, peak, teamCurrent) in zip(clan_current_2v2_ratings, clan_peak_2v2_ratings, clan_2v2_teamnames):
            index += 1
            if current > highestCurrentRating:
                highestCurrentRating = current
                bestIndex = index
        clan_current_2v2_ratings_sorted.append(
            clan_current_2v2_ratings.pop(bestIndex))
        clan_peak_2v2_ratings_sorted.append(
            clan_peak_2v2_ratings.pop(bestIndex))
        clan_2v2_teamnames_sorted.append(
            clan_2v2_teamnames.pop(bestIndex))
    print('done sorting')


async def loop():
    get_clan()
    global clan
    get_clan_members()
    global clan_members
    Save2v2Elo()
    SortPlayersElo()
    global first_time
    global msg1
    global msg2
    global msg3
    global msg4
    embed1 = discord.Embed(description="skyward image", color=0x289fb4)
    embed2 = discord.Embed(
        title="Skyward", description="Total Exp: " + str(clan['clan_xp']), color=0x289fb4)
    embed3 = discord.Embed(description="", color=0x289fb4)
    embed4 = discord.Embed(description="", color=0x289fb4)
    global num
    num = 1
    for (current, peak, currentTeam) in zip(clan_current_2v2_ratings_sorted, clan_peak_2v2_ratings_sorted, clan_2v2_teamnames_sorted):
        if num <= 25:
            embed3.description += "**" + \
                str(num) + ". " + currentTeam + "**: **current:** " + \
                str(current) + " **peak:** " + str(peak) + '\n'
        else:
            embed4.description += "**" + \
                str(num) + ". " + currentTeam + "**: **current:** " + \
                str(current) + " **peak:** " + str(peak) + '\n'
        num += 1
        await send_embeds(embed1=embed1, embed2=embed2, embed3=embed3, embed4=embed4)


async def send_embeds(embed1, embed2, embed3, embed4):
    channel = bot.get_channel(using_channel)
    await channel.purge(limit=10)  
    global msg1
    global msg2
    global msg3
    global msg4
    msg1 = await channel.send(skyward_image_link)  # send 1
    print("sent 1")
    msg2 = await channel.send(embed=embed2)  # send 2
    print("sent 2")
    msg3 = await channel.send(embed=embed3)  # send 3
    print('sent 3')
    msg4 = await channel.send(embed=embed4)  # send 3
    print('sent 4')


async def delete_embeds(msg1, msg2, msg3, msg4):
    await msg1.delete()
    await msg2.delete()
    await msg3.delete()
    await msg4.delete()

keep_alive()
bot.run(bot.run(get_keys(0))
