import json
from modules.api import get_ps4_players_api

def get_ps4_players(clan_repl, clan, clan_members):
  try: 
    ps4_players = get_ps4_players_api(clan_repl.server_id)
    print("Amount of ps4 players in " + clan['clan_name'] + ": " + str(len(ps4_players)))
    while len(ps4_players) > 0:
      clan_members.append(ps4_players.pop(0))
  except:
    print(clan['clan_name'] + " doesn't have any ps4 players")
  return clan_members

def __get_ps4_players_data(clan):
    with open('data/ps4_players/' + clan['clan_name'] + '_ps4_players.json') as file:
      ps4_players = json.load(file)
      return ps4_players