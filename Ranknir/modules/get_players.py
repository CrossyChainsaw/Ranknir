from Ranknir.classes.Server import Server
from Ranknir.modules.api import fetch_clan
import json

# get console players
CLAN_DATA_LOCATION = 'Dadabase/data/clans/'
SERVER_DATA_LOCATION = 'Dadabase/data/servers/'

def get_console_players(clan):
    console_players = {}
    try:
        # console_players = fetch_console_players(clan.server_id) # Dadabase discontinued
        console_players = __load_ps4_players(clan.server_id)
        print("Console player amount in %s: %s" %
              (clan.name[0], str(len(console_players))))
    except:
        print("No console players in " + clan.name[0])
    return console_players

def load_rm_players(server_id):
    with open(CLAN_DATA_LOCATION + str(server_id) + '.json', 'r') as file:
        data = json.load(file)
        rm_players = data['al_players']
        rm_player_ids = []
        for x in rm_players:
            rm_player_ids.append(int(x["brawlhalla_id"]))
        print('returning')
        print(rm_player_ids)
        return rm_player_ids # should return an array with ids



def __load_ps4_players(server_id):
    with open(CLAN_DATA_LOCATION + str(server_id) + '.json', 'r') as file:
        data = json.load(file)  # error
        return data['ps4_players']
    

def get_server_players(server: Server):
    print(server.name)
    server_data = __read_data(SERVER_DATA_LOCATION, server.id)
    print(f"Amount of players in {server_data['name']}: {len(server_data['links'])}")
    return server_data['links']
     

def __read_data(path, id):
  """Read clan or server data"""
  with open(path + str(id) + '.json') as file:
    data = json.load(file)
    return data
