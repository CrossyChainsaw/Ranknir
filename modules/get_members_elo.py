import json
from modules.api import fetch_player_ranked_stats
from modules.clan import get_clan_members
from modules.ps4_players import get_ps4_players
from modules.server import get_server_players

# remove clan_id dependency for server logic

def get_members_1v1_elo(clan_repl, clan_name):
  print(clan_name)
  name_array = []
  current_array = []
  peak_array = []
  console_player_amount = 0
  
  # ps4 players
  ps4_players = get_ps4_players(clan_repl, clan_name)
  name, current, peak = __get_clan_members_elo_1v1(ps4_players)
  while len(name) > 0:
    name_array.append(name.pop(0))
    current_array.append(current.pop(0))
    peak_array.append(peak.pop(0))
  console_player_amount = len(ps4_players)

  # clan members
  for clan_id in clan_repl.id_array:
    clan_members = get_clan_members(clan_id)
    name, current, peak = __get_clan_members_elo_1v1(clan_members)
    while len(name) > 0:
      name_array.append(name.pop(0))
      current_array.append(current.pop(0))
      peak_array.append(peak.pop(0))
  
  players = [name_array, current_array, peak_array]
  return players, console_player_amount

  
def get_members_2v2_elo(clan_repl, sorting_method, clan_name):
  teamname_array = []
  current_array = []
  peak_array = []
  console_player_amount = 0
  
  # ps4 players
  ps4_players = get_ps4_players(clan_repl, clan_name)
  teamname, current, peak = __get_clan_members_elo_2v2(ps4_players, sorting_method)
  while len(teamname) > 0:
    teamname_array.append(teamname.pop(0))
    current_array.append(current.pop(0))
    peak_array.append(peak.pop(0))
  console_player_amount = len(ps4_players)
  
  # get clan and clan members
  for clan_id in clan_repl.id_array:
    clan_members = get_clan_members(clan_id)
    teamname, current, peak = __get_clan_members_elo_2v2(clan_members, sorting_method)
    while len(teamname) > 0:
      teamname_array.append(teamname.pop(0))
      current_array.append(current.pop(0))
      peak_array.append(peak.pop(0))
  
  # get ps4 players
  #clan_members = get_ps4_players(clan_repl, clan, clan_members)
  print(teamname)
  players = [teamname_array, current_array, peak_array]
  return players, console_player_amount

def get_members_1v1_elo_server(server):# get clan and clan members
  
  server_members = []

  # get ps4 players
  server_members = get_server_players(server, server_members)

  # define elo arrays
  server_members_name = []
  server_members_current = []
  server_members_peak = []

  # get everyone's rank stats
  num = 1
  for member in server_members:
    print("member")
    print(member)
    try:
      player = fetch_player_ranked_stats(member["brawlhalla_id"])
      
      server_members_name.append(player["name"])
      server_members_current.append(player["rating"])
      server_members_peak.append(player["peak_rating"])

      print(str(num) + ". " + player["name"])
      print("current: " + str(player["rating"]))
      print("peak: " + str(player["peak_rating"]))
    except:
      server_members_name.append(member["name"])
      server_members_current.append(-1)
      server_members_peak.append(-1)

      print(str(num) + ". " + member['name'])
      print("current: " + "-1")
      print("peak: " + "-1")
    num += 1
  
  # return values
  return server_members_name, server_members_current, server_members_peak
    


def __get_clan_members_elo_1v1(clan_members):
  # define elo arrays
  clan_members_name = []
  clan_members_current = []
  clan_members_peak = []  
  
  num = 1
  for member in clan_members:
    try:
      player = fetch_player_ranked_stats(member["brawlhalla_id"])
      
      clan_members_name.append(player["name"])
      clan_members_current.append(player["rating"])
      clan_members_peak.append(player["peak_rating"])

      print(str(num) + ". " + player["name"])
      print("current: " + str(player["rating"]))
      print("peak: " + str(player["peak_rating"]))
    except:
      clan_members_name.append(member["name"])
      clan_members_current.append(-1)
      clan_members_peak.append(-1)

      print(str(num) + ". " + member['name'])
      print("current: " + "-1")
      print("peak: " + "-1")
    num += 1
    
  # return values
  return clan_members_name, clan_members_current, clan_members_peak
def __get_clan_members_elo_2v2(clan_members, sorting_method):
  clan_2v2_teamnames = []
  clan_current_2v2_ratings = []
  clan_peak_2v2_ratings = []
  num = 0
  for player in clan_members:
    num += 1
    try:
        all_my_2v2_teams = fetch_player_ranked_stats(player["brawlhalla_id"])["2v2"]

        if sorting_method == "current":
          
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


                
        elif sorting_method == "peak":
                        # FIND BEST TEAM PEAK ELO
          bestCurrentTeam = "bestCurrentTeam is undefined"
          bestCurrent = -1
          bestPeak = -1

          for team in all_my_2v2_teams:
              rating = team["rating"]
              peak = team["peak_rating"]
              if peak > bestPeak:
                  bestCurrent = rating
                  bestPeak = peak
                  bestCurrentTeam = team["teamname"]
        
        # Format best current team
        name_plus = bestCurrentTeam.find('+')
        name_length = len(bestCurrentTeam)
        name_1 = bestCurrentTeam[0:name_plus]
        name_2 = bestCurrentTeam[name_plus+1:name_length]
        full_name = name_1 + ' **+** ' + name_2 
        bestCurrentTeam = full_name

        # ADD ALL VALUES TO ARRAYS
        if bestCurrentTeam.startswith("bestCurrentTeam is undefine"):
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
      try:
        currentResult = "**" + \
            str(num) + ". " + player["name"] + \
            "**: **current:**" + " -1" + " **peak:**" + " -1"

        clan_2v2_teamnames.append(player["name"])
        clan_current_2v2_ratings.append(-1)
        clan_peak_2v2_ratings.append(-1)
      except:
        #ps4 player format stupid dadabase shizzle :<
        currentResult = "**" + \
            str(num) + ". " + player["brawlhalla_name"] + \
            "**: **current:**" + " -1" + " **peak:**" + " -1"

        clan_2v2_teamnames.append(player["brawlhalla_name"])
        clan_current_2v2_ratings.append(-1)
        clan_peak_2v2_ratings.append(-1)

        print(currentResult)
  return clan_2v2_teamnames, clan_current_2v2_ratings, clan_peak_2v2_ratings
