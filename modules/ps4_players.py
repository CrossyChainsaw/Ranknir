import json
from modules.api import get_ps4_players_api

def get_ps4_players(clan_repl, clan_name):
  ps4_players = {}
  try: 
    ps4_players = get_ps4_players_api(clan_repl.server_id)
    print("Amount of ps4 players in "+ clan_name +": " + str(len(ps4_players)))
  except:
    print(clan_name + " doesn't have any ps4 players")
  return ps4_players

def __get_ps4_players_data(clan):
    with open('data/ps4_players/' + clan['clan_name'] + '_ps4_players.json') as file:
      ps4_players = json.load(file)
      return ps4_players