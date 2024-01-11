from modules2.api import fetch_console_players, fetch_clan
import json

# get console players


def get_console_players(clan):
    console_players = {}
    try:
        #console_players = fetch_console_players(clan.server_id) # Dadabase discontinued
        console_players = __load_ps4_players(clan.server_id)
        print("Console player amount in %s: %s" %
              (clan.name, str(len(console_players))))
    except:
        print("No console players in " + clan.name)
    return console_players

DATA_LOCATION = 'data/clans/'
def __load_ps4_players(server_id):
  with open(DATA_LOCATION + str(server_id) + '.json', 'r') as file:
    data = json.load(file) # error
    return data['ps4_players']


# get server players


def get_server_players(server):  # server object
    print(server.name)
    server_players = []
    try:
        server_players = server.get_players_data()
        print(server_players)
        print('Amount of players in %s: %s' %
              (server.name, str(len(server_players))))
    except:
        print(str(server.name) + " doesn't have any players")
    return server_players
