from classes.Player import Player
from classes.Team import Team
from modules2.api import fetch_player_ranked_stats

# There are different functions for 1v1, 2v2 and 1v1&2v2. I made an extra one for 1v1&2v2 because it halves the api requests.


#################### GET ALL PLAYERS ELO ######################

async def get_players_elo_1v1(clan, players):
  """Gets the elo for each player and `returns` an array of `Player` objects"""
  player_object_array = []
  for i, player in enumerate(players):
      player_ranked_stats = await fetch_player_ranked_stats(player['brawlhalla_id'])
      player_object = __extract_player_stats_into_player_object_1v1(
          player_ranked_stats)
      if __check_if_name_is_blank(clan, player_object):
          continue
      player_object_array.append(player_object)
      print('%s %s/%s' % (clan.name, str(i+1), str(len(players))))
      print('1s: ' + player_object.name)
  return player_object_array


async def get_players_elo_2v2(clan, players):
  """Gets the best team for each player and `returns` an array of `Team` objects"""
  team_object_array = []
  for i, player in enumerate(players):
      player_ranked_stats = await fetch_player_ranked_stats(player['brawlhalla_id'])
      team_object = __extract_player_stats_into_team_object_2v2(clan, player_ranked_stats)
      if __check_if_name_is_blank(clan, team_object):
          continue
      team_object_array.append(team_object)
      print('%s %s/%s' % (clan.name, str(i+1), str(len(players))))
      print('2s: ' + team_object.name)
  return team_object_array

# maybe use this function always and leave out 1s or 2s if not wanted, configure if wanted or not in clan_data.py. so you don't have to change everything here and in 1v1 and in 2v2


async def get_players_elo_1v1_and_2v2(clan, players):
  """Gets the personal elo and best-team for each player and `returns` an array of `Player` objects and `Team` objects"""
  player_object_array = []
  team_object_array = []
  for i, player in enumerate(players):
      player_ranked_stats = await fetch_player_ranked_stats(player['brawlhalla_id'])
      player_object = __extract_player_stats_into_player_object_1v1(player_ranked_stats)
      team_object = __extract_player_stats_into_team_object_2v2(clan, player_ranked_stats)
      if __check_if_name_is_blank(clan, player_object) and __check_if_name_is_blank(clan, team_object):
          continue
      player_object_array.append(player_object)
      team_object_array.append(team_object)
      print('%s %s/%s' % (clan.name, str(i+1), str(len(players))))
      print('1s: ' + player_object.name)
      print('2s: ' + team_object.name)
  return player_object_array, team_object_array



###################### PUT PLAYER DATA IN PYTHON OBJECTS #######################


def __extract_player_stats_into_player_object_1v1(player):
  """Takes player data and turns it into a `Player` object"""
  player_object = Player(player['name'], player['rating'], player['peak_rating'])
  player_object.name = __give_empty_name_a_placeholder_name(player_object.name)
  player_object.name = __try_decode(player_object.name)
  return player_object


def __extract_player_stats_into_team_object_2v2(clan, player):
  """Takes player data and turns it into a `Team` object"""
  team_object = __find_best_team(clan, player)
  team_object.name = __format_teamname(player, team_object)
  team_object.name = __give_empty_name_a_placeholder_name(team_object.name)
  team_object.name = __try_decode(team_object.name)
  return team_object


############################ USEFUL FUNCTIONS ######################### 

# testse
def __try_decode(name):
  """Tries to decode unicode symbols"""
  try:
      new_name = name.encode("charmap").decode()
      return new_name
  except:
      return name


def __change_order_team_name(team_object):  
  best_team_name = team_object.name
  if '+' in best_team_name:
    name_plus_index = best_team_name.find('+')
    team_name_length = len(best_team_name)
    name_1 = best_team_name[0:name_plus_index]     
    name_2 = best_team_name[name_plus_index+1:team_name_length]
    new_best_team_name = name_2 + '+' + name_1
    team_object.name = new_best_team_name      
    return team_object
  else:
    return team_object



def __format_teamname(player, team_object):  
  """Puts 2 asterisks after name 1, and 2 asterisks before name 2. Necessary for making the names bold when sending the embed (consider putting this in embed.py)"""
  best_team_name = team_object.name
  if '+' in best_team_name:
    name_plus_index = best_team_name.find('+')
    name_length = len(best_team_name)
    name_1 = best_team_name[0:name_plus_index]
    name_2 = best_team_name[name_plus_index+1:name_length]
    new_name = name_1 + '** + **' + name_2
    return new_name
  else:
    return best_team_name


def __check_order_team_name(player, brawl_id_one, brawl_id_two, team_obj):
  if player["brawlhalla_id"] == brawl_id_one:
    return team_obj
  else:
    return __change_order_team_name(team_obj)


def __find_best_team(clan, player):
  """Finds the best team of the player using `sorting_method` and returns a `Team` object"""
  all_my_2v2_teams = player['2v2']
  best_team = None
  best_team_name = player["name"]
  brawl_id_one = player["brawlhalla_id"]
  brawl_id_two = 0
  best_current = 0
  best_peak = 0
  # Find best team
  if clan.sorting_method == "current":
      # FIND BEST TEAM CURRENT ELO
      for team in all_my_2v2_teams:
          rating = team["rating"]
          if rating > best_current:
            best_team = team
            best_current = rating
  elif clan.sorting_method == "peak":
      # FIND BEST TEAM PEAK ELO
      for team in all_my_2v2_teams:
          peak = team["peak_rating"]
          if peak > best_peak:
              best_team = team
              best_peak = peak

  # format name
  if best_team != None:
    best_team_name = best_team["teamname"]
    best_current = best_team["rating"]
    best_peak = best_team["peak_rating"]
    brawl_id_one = best_team["brawlhalla_id_one"]
    brawl_id_two = best_team["brawlhalla_id_two"]
    
  team_obj = Team(best_team_name, best_current, best_peak)
  team_obj = __check_order_team_name(player, brawl_id_one, brawl_id_two, team_obj)
    
  return team_obj


def __give_empty_name_a_placeholder_name(player_name):
  if (player_name) == "":
      return 'N/A'
  else:
      return player_name


def __check_if_elo_is_zero(clan, player_object):
    if clan.no_elo_players == 'hide':
        if player_object.current == 0 and player_object.peak == 0:
            return True
    else:
        return False


def __check_if_name_is_blank(clan, player_object):
    if clan.no_elo_players == 'hide':
        if player_object.name == 'N/A' or player_object.name == "":
            return True
    else:
        return False
