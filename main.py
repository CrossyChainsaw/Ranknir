import os
import discord
from discord.ext import commands
from discord.ext import tasks
import time
import json
from api import getClan
from api import getPlayerStats
from keep_alive import keep_alive
from OrderTeamName import ArrangeTeamName

# VARIABLES
skywardImageLink = os.environ['IMG_LINK']
eloChannel = 976552050953437194
skywardCurrentRatings = []
skywardPeakRatings = []
skywardCurrentTeamNames = []

skywardCurrentRatingsSorted = []
skywardPeakRatingsSorted = []
skywardCurrentTeamsSorted = []


# COMMANDS
bot = commands.Bot(command_prefix=['r'])

@commands.has_role('DevOps')
@bot.command(name='start', help='starts bruh')
async def start(ctx):  
  loop.start()


# PRINT
#get all players
json_object = json.loads(getClan().content) # request
allPLayersInSkyward = json_object["clan"];

def GetPlayersElo():
  num = 0
  for player in allPLayersInSkyward:
    num += 1
    try:
      all2v2Teams = json.loads(getPlayerStats(player ["brawlhalla_id"]).content)["2v2"] #request

      # FIND BEST TEAM CURRENT ELO
      bestCurrentTeam = "bestCurrentTeam is undefined"
      bestCurrent = -1
      bestPeak = -1

      for team in all2v2Teams:
        rating = team["rating"]
        peak = team["peak_rating"]
        if rating > bestCurrent:
          bestCurrent = rating
          bestPeak = peak
          bestTeam = team
          bestCurrentTeam = team["teamname"]


      # ORDER TEAMNAME
      bestCurrentTeam = ArrangeTeamName(bestTeam) # error
      print('ordered: ' + bestCurrentTeam)
          
      # ADD ALL VALUES TO ARRAYS
      if bestCurrentTeam.startswith("bestCurrentTeam is undefined"):
        bestCurrent = -1
        bestPeak = -1
        bestCurrentTeam = player["name"]
      print(bestCurrentTeam)
      print("current: " + str(bestCurrent))
      print("peak: " + str(bestPeak))
      skywardCurrentTeamNames.append(bestCurrentTeam)
      skywardCurrentRatings.append(bestCurrent)
      skywardPeakRatings.append(bestPeak)

    except:
      currentResult = "**" + str(num) + ". " + player["name"] + "**: **current:**" + " -1" + " **peak:**" + " -1"
      
      skywardCurrentTeamNames.append(player["name"])
      skywardCurrentRatings.append(-1)
      skywardPeakRatings.append(-1)
      
      print(currentResult)
  time.sleep(1)



def SortPlayersElo():
  print('start sorting players elo...')
  while len(skywardCurrentRatings) > 0:
    index = -1
    bestIndex = 0
    highestCurrentRating = -2
    for (current, peak, teamCurrent) in zip(skywardCurrentRatings, skywardPeakRatings, skywardCurrentTeamNames):
      index+=1
      if current > highestCurrentRating:
        highestCurrentRating = current  
        bestIndex = index
    skywardCurrentRatingsSorted.append(skywardCurrentRatings.pop(bestIndex))
    skywardPeakRatingsSorted.append(skywardPeakRatings.pop(bestIndex))
    skywardCurrentTeamsSorted.append(skywardCurrentTeamNames.pop(bestIndex))
  print('done sorting')


@tasks.loop(seconds=10)
async def loop():  
  GetPlayersElo()
  SortPlayersElo()
  
  # SEND SKYWARD IMAGE
  channel = bot.get_channel(eloChannel)  
  msg1 = await channel.send(skywardImageLink) # send 1
  print("sent image")

  # SEND CLAN XP
  json_object = json.loads(getClan().content)# request
  _clanExp = json_object["clan_xp"]
  
  embed2=discord.Embed(title="Skyward", description="Total Exp: " + str(_clanExp), color=0x289fb4)
  channel = bot.get_channel(eloChannel)  
  msg2 = await channel.send(embed=embed2) # send 2
  print("sent clan xp")

  # SEND MEMBERS ELO
  embed3=discord.Embed(description = "", color=0x289fb4)
  num = 1
  for (current, peak, currentTeam) in zip(skywardCurrentRatingsSorted, skywardPeakRatingsSorted, skywardCurrentTeamsSorted):
    embed3.description += "**" + str(num) + ". " + currentTeam + "**: **current:** " + str(current) + " **peak:** " + str(peak) + '\n'
    num+=1
  channel = bot.get_channel(eloChannel)  
  msg3 = await channel.send(embed=embed3) # send 3
  
  # DELETE MESSAGES
  skywardCurrentRatings.clear()
  skywardPeakRatings.clear()
  skywardCurrentRatingsSorted.clear()
  skywardPeakRatingsSorted.clear()
  skywardCurrentTeamsSorted.clear()

  time.sleep(2000)

  await msg1.delete()
  await msg2.delete()
  await msg3.delete()

keep_alive()
bot.run(os.environ['BOT_KEY'])

#extra if peak and current is same team just show in one line?
#logic for sorting, if starts with player[name] nothing else yk
# get player id of the teammate and do request for name ez
#then do line 2
