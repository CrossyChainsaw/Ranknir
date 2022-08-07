import os
from pydoc import classname
from secrets import get_keys
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
        await poop()
        print('start waiting')
        time.sleep(2500)
        print('done waiting')


@commands.has_role('DevOps')
@bot.command(name='start', help='starts bruh')
async def start(ctx):
    poop.start()


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
        # print(clan_members)
        clan_members_test_2members = [{
            "brawlhalla_id": 6433263,
            "name": "Zwergennest",
            "rank": "Member",
            "join_date": 1618333318,
            "xp": 232764
        }, {
            "brawlhalla_id": 56793941,
            "name": "GÃ¸d-sÃ±Ã®pÃªr",
            "rank": "Member",
            "join_date": 1659878282,
            "xp": 228
        }]
        clan_members_test_3members = [
            {
                "brawlhalla_id": 3764805,
                "name": "Kyouno Natsumi <3",
                "rank": "Officer",
                "join_date": 1618497345,
                "xp": 126456
            },
            {
                "brawlhalla_id": 49936771,
                "name": "Hunter",
                "rank": "Officer",
                "join_date": 1618949986,
                "xp": 559758
            },
            {
                "brawlhalla_id": 7364605,
                "name": "100 ping",
                "rank": "Officer",
                "join_date": 1629141768,
                "xp": 148940
            }, {
                "brawlhalla_id": 56793941,
                "name": "GÃ¸d-sÃ±Ã®pÃªr",
                "rank": "Member",
                "join_date": 1659878282,
                "xp": 228
            }]
        clan_members_test_26members = [
            {
                "brawlhalla_id": 6433263,
                "name": "Zwergennest",
                "rank": "Member",
                "join_date": 1618333318,
                "xp": 232764
            },
            {
                "brawlhalla_id": 3764805,
                "name": "Kyouno Natsumi <3",
                "rank": "Officer",
                "join_date": 1618497345,
                "xp": 126456
            },
            {
                "brawlhalla_id": 49936771,
                "name": "Hunter",
                "rank": "Officer",
                "join_date": 1618949986,
                "xp": 559758
            },
            {
                "brawlhalla_id": 7364605,
                "name": "100 ping",
                "rank": "Officer",
                "join_date": 1629141768,
                "xp": 148940
            },
            {
                "brawlhalla_id": 9316238,
                "name": "Nymphe",
                "rank": "Member",
                "join_date": 1630749984,
                "xp": 196595
            },
            {
                "brawlhalla_id": 71428893,
                "name": "zDisigma",
                "rank": "Member",
                "join_date": 1631063079,
                "xp": 246692
            },
            {
                "brawlhalla_id": 6202261,
                "name": "Linox",
                "rank": "Member",
                "join_date": 1633609381,
                "xp": 221639
            },
            {
                "brawlhalla_id": 5708299,
                "name": "55p",
                "rank": "Member",
                "join_date": 1638807175,
                "xp": 96895
            },
            {
                "brawlhalla_id": 79588993,
                "name": "Helsem",
                "rank": "Member",
                "join_date": 1642035178,
                "xp": 96609
            },
            {
                "brawlhalla_id": 8615459,
                "name": "Hidetsu?!",
                "rank": "Member",
                "join_date": 1644348435,
                "xp": 46956
            },
            {
                "brawlhalla_id": 3794093,
                "name": "MrEmpanadilla19",
                "rank": "Member",
                "join_date": 1644749675,
                "xp": 186442
            },
            {
                "brawlhalla_id": 35913608,
                "name": "rufus",
                "rank": "Member",
                "join_date": 1645191275,
                "xp": 86445
            },
            {
                "brawlhalla_id": 7940781,
                "name": "Solarson",
                "rank": "Officer",
                "join_date": 1645883930,
                "xp": 110952
            },
            {
                "brawlhalla_id": 43227947,
                "name": "Mogzy",
                "rank": "Member",
                "join_date": 1646239755,
                "xp": 56374
            },
            {
                "brawlhalla_id": 26358569,
                "name": "Uncle Timmy",
                "rank": "Member",
                "join_date": 1646239982,
                "xp": 64960
            },
            {
                "brawlhalla_id": 5111230,
                "name": "WE CAN'T PROMISE ANYTHING",
                "rank": "Member",
                "join_date": 1646913914,
                "xp": 65003
            },
            {
                "brawlhalla_id": 74662063,
                "name": "Roddd",
                "rank": "Leader",
                "join_date": 1647024356,
                "xp": 27000
            },
            {
                "brawlhalla_id": 58366728,
                "name": "DanHasCorona",
                "rank": "Member",
                "join_date": 1648231212,
                "xp": 124323
            },
            {
                "brawlhalla_id": 70022787,
                "name": "WE WILL THINK ABOUT IT",
                "rank": "Officer",
                "join_date": 1648927059,
                "xp": 137165
            },
            {
                "brawlhalla_id": 84499165,
                "name": "Kaizaar",
                "rank": "Member",
                "join_date": 1649621274,
                "xp": 62369
            },
            {
                "brawlhalla_id": 2658232,
                "name": "gonconist",
                "rank": "Member",
                "join_date": 1650631486,
                "xp": 14671
            },
            {
                "brawlhalla_id": 61355963,
                "name": "abzyo",
                "rank": "Member",
                "join_date": 1651247127,
                "xp": 12692
            },
            {
                "brawlhalla_id": 9201392,
                "name": "Lowkey",
                "rank": "Member",
                "join_date": 1652175951,
                "xp": 118006
            },
            {
                "brawlhalla_id": 40660695,
                "name": "twitch.tv/friendlyherobrn",
                "rank": "Member",
                "join_date": 1653504781,
                "xp": 56326
            },
            {
                "brawlhalla_id": 3221385,
                "name": "El Eldad",
                "rank": "Member",
                "join_date": 1653506496,
                "xp": 31008
            },
            {
                "brawlhalla_id": 47231784,
                "name": "Fochino",
                "rank": "Member",
                "join_date": 1653659995,
                "xp": 25528
            },
        ]
        clan_members = clan_members_test_3members
    except:
        clan_members = []


def Save2v2Elo():
    num = 0
    for player in clan_members:
        num += 1
        try:
            all_my_2v2_teams = json.loads(
                getPlayerStats(
                    player["brawlhalla_id"]).content)["2v2"]  # request

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
            print(str(num) + ': ' + bestCurrentTeam)
            print("current: " + str(bestCurrent))
            print("peak: " + str(bestPeak))
            print(' ')
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
        for (current, peak, teamCurrent) in zip(clan_current_2v2_ratings,
                                                clan_peak_2v2_ratings,
                                                clan_2v2_teamnames):
            index += 1
            if current > highestCurrentRating:
                highestCurrentRating = current
                bestIndex = index
        clan_current_2v2_ratings_sorted.append(
            clan_current_2v2_ratings.pop(bestIndex))
        clan_peak_2v2_ratings_sorted.append(
            clan_peak_2v2_ratings.pop(bestIndex))
        clan_2v2_teamnames_sorted.append(clan_2v2_teamnames.pop(bestIndex))
    print('done sorting')


async def poop():
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
    embed2 = discord.Embed(title="Skyward",
                           description="Total Exp: " + str(clan['clan_xp']),
                           color=0x289fb4)
    embed3 = discord.Embed(description="", color=0x289fb4)
    embed4 = discord.Embed(description="", color=0x289fb4)
    global num
    num = 1
    print("current: " + str(len(clan_current_2v2_ratings_sorted)))
    print("peak: " + str(len(clan_peak_2v2_ratings_sorted)))
    print("names: " + str(len(clan_2v2_teamnames_sorted)))
    for (current, peak, currentTeam) in zip(clan_current_2v2_ratings_sorted,
                                            clan_peak_2v2_ratings_sorted,
                                            clan_2v2_teamnames_sorted):
        if num <= 25:
            embed3.description += "**" + \
                str(num) + ". " + currentTeam + "**: **current:** " + \
                str(current) + " **peak:** " + str(peak) + '\n'
        else:
            embed4.description += "**" + \
                str(num) + ". " + currentTeam + "**: **current:** " + \
                str(current) + " **peak:** " + str(peak) + '\n'
        num += 1
    await send_embeds(embed1=embed1,
                      embed2=embed2,
                      embed3=embed3,
                      embed4=embed4)


async def send_embeds(embed1, embed2, embed3, embed4):
    channel = bot.get_channel(using_channel)
    await channel.purge(limit=10)

    await channel.send(skyward_image_link)  # send 1
    print("sent 1")

    await channel.send(embed=embed2)  # send 2
    print("sent 2")

    await channel.send(embed=embed3)  # send 3
    print('sent 3')

    if len(embed4.description) > 1:
        await channel.send(embed=embed4)  # send 3
        print('sent 4')


keep_alive()
bot.run(get_keys(0))