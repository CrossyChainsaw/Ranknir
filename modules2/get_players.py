from modules2.api import fetch_console_players, fetch_clan

# get console playeres


def get_console_players(clan):
    console_players = {}
    try:
        console_players = fetch_console_players(clan.server_id)  # requires id
        print("Console player amount in %s: %s" %
              (clan.name, str(len(console_players))))
    except:
        print("No console players in " + clan.name)
    return console_players


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
