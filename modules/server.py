import json

def get_server_players(server, members):
  try:
    server_players = server.get_players_data()
    print("Amount of players in " + server.name)
    while len(server_players) > 0:
      members.append(server_players.pop(0))
  except:
    print(str(server.name) + " doesn't have any players")
  return members  

