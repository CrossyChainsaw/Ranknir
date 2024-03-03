from Ranknir.modules.api import fetch_console_players, fetch_clan
import json

# get console players
DATA_LOCATION = 'Dadabase/data/clans/'


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
    with open(DATA_LOCATION + str(server_id) + '.json', 'r') as file:
        data = json.load(file)  # error
        return data['rm_players']



def __load_ps4_players(server_id):
    with open(DATA_LOCATION + str(server_id) + '.json', 'r') as file:
        data = json.load(file)  # error
        return data['ps4_players']
    


# get server players


def get_server_players(server):  # server object
    print(server.name)
    server_data = []
    try:
        server_data = server.get_data()
        print(server_data)
        print(
            f"Amount of players in {server_data['name']}: {len(server_data['links'])}")
    except:
        print(f"{server_data['name']} doesn't have any players")
    return server_data['links']
