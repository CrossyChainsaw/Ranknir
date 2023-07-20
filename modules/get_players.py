import json
from modules.api import fetch_console_players, fetch_clan

# get console playeres


def get_console_players(server_id):
    console_players = {}
    try:
        console_players = fetch_console_players(server_id)  # requires id
        print("Console player amount: " + str(len(console_players)))
    except:
        print("No console players")
    return console_players

# get clan players


def get_clan_players(clan_id):
    clan_players = fetch_clan()
    return clan_players


# get server players


def get_server_players(server):  # server object
    print(server.name)
    server_players = []
    try:
        server_players = server.get_players_data()
        print(server_players)
        print("Amount of players in " + server.name)
    except:
        print(str(server.name) + " doesn't have any players")
    return server_players
