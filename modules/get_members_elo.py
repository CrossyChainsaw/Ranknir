import json
from modules.api import fetch_clan, fetch_player_ranked_stats

# todo (should)
# remove stupid arrays for return values

def get_clan(clan_id):
    try:
        clan = json.loads(fetch_clan(clan_id).content)  # request
    except:
        clan = []
        print("couldn't fetch clan data of clan " + str(clan_id))
    return clan


def get_clan_members(clan_id):
    clan = get_clan(clan_id)
    try:
        clan_members = clan['clan']

        # test process with only 3 clan members
        #with open('./test_data.json') as f:
          #clan_members = json.load(f)
    except:
        print("ERROR: couldn't get clan members, returned empty array")
        clan_members = []

    # return values
    return clan_members, clan

def get_clans(clan_id_array):
  print('created clan array')
  clans = []
  for clan_id in clan_id_array:
    clans.append(get_clan(clan_id))
  print("returning clan array")
  return clans
  
def get_ps4_players(clan, clan_members):
  try: 
    with open('./Data/ps4_players/' + clan['clan_name'] + '_ps4_players.json') as file:
      ps4_players = json.load(file)
      print("Amount of ps4 players in " + clan['clan_name'] + ": " + str(len(ps4_players)))
      while len(ps4_players) > 0:
        clan_members.append(ps4_players.pop(0))
  except:
    print(clan['clan_name'] + " doesn't have any ps4 players")
  return clan_members

def get_members_1v1_elo(clan_id):

  # get clan and clan members
  clan_members, clan = get_clan_members(clan_id)

  # get ps4 players
  clan_members = get_ps4_players(clan, clan_members)

  # define elo arrays
  clan_members_name = []
  clan_members_current = []
  clan_members_peak = []

  # get everyone's rank stats
  num = 1
  for member in clan_members:
    try:
      player = json.loads(fetch_player_ranked_stats(member["brawlhalla_id"]).content)
      
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
  return clan_members_name, clan_members_current, clan_members_peak, clan
    


def get_members_2v2_elo(clan_id, sorting_method):
    
  # get clan and clan members
  clan_members, clan = get_clan_members(clan_id)

  # get ps4 players
  clan_members = get_ps4_players(clan, clan_members)

  # Define elo arrays
  clan_2v2_teamnames = []
  clan_current_2v2_ratings = []
  clan_peak_2v2_ratings = []

  # get everyone's ranked stats
  num = 0
  for player in clan_members:
    num += 1
    try:
        all_my_2v2_teams = json.loads(
            fetch_player_ranked_stats(player["brawlhalla_id"]).content)["2v2"]  # request

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
        print(full_name)
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
        currentResult = "**" + \
            str(num) + ". " + player["name"] + \
            "**: **current:**" + " -1" + " **peak:**" + " -1"

        clan_2v2_teamnames.append(player["name"])
        clan_current_2v2_ratings.append(-1)
        clan_peak_2v2_ratings.append(-1)

        print(currentResult)
  print('teamnames amount (in get_members_elo)')
  print(len(clan_2v2_teamnames))
  return clan_2v2_teamnames, clan_current_2v2_ratings, clan_peak_2v2_ratings, clan
