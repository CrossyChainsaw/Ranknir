from Ranknir.classes.Server import Server
from Ranknir.classes.Clan import Clan
from Ranknir.modules.api import fetch_clan
from Ranknir.modules.data_management import DADABASE_CLAN_DATA_PATH, DADABASE_SERVER_DATA_PATH, DATA_KEY_FOR_ACCOUNT_LINKERS, DATA_KEY_FOR_CONSOLE_PLAYERS, load_json_file
import json

# manually merge this into data_management


def get_console_players(clan: Clan):
    console_players = {}
    try:
        # console_players = fetch_console_players(clan.server_id) # Dadabase discontinued
        clan_data = load_json_file(f"{DADABASE_CLAN_DATA_PATH}{clan.discord_server_id}.json")
        console_players = clan_data[DATA_KEY_FOR_CONSOLE_PLAYERS]
        print("Console player amount in %s: %s" %
              (clan.server_name, str(len(console_players))))
    except:
        print("No console players in " + clan.server_name)
    return console_players


def get_account_linker_players(server_id):
    with open(DADABASE_CLAN_DATA_PATH + str(server_id) + '.json', 'r') as file:
        data = json.load(file)
        rm_players = data[DATA_KEY_FOR_ACCOUNT_LINKERS]
        rm_player_ids = []
        for x in rm_players:
            rm_player_ids.append(int(x["brawlhalla_id"]))
        print('returning')
        print(rm_player_ids)
        return rm_player_ids # should return an array with ids
    

def get_server_players(server: Server):
    print(server.name)
    server_data = load_json_file(f"{DADABASE_SERVER_DATA_PATH}{server.id}.json")
    print(f"Amount of players in {server_data['name']}: {len(server_data['links'])}")
    return server_data['links']
    
