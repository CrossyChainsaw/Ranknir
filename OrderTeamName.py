from api import getPlayerStats
from api import getClan
import json

def ArrangeTeamName(teamName):
  player1_ID = teamName["brawlhalla_id_one"]
  player2_ID = teamName["brawlhalla_id_two"]
  player1 = json.loads(getPlayerStats(player1_ID).content)
  player2 = json.loads(getPlayerStats(player2_ID).content)
  print('p1: ' + player1['name'])
  print('p2: ' + player2['name'])

  inSkyward = False
  json_object = json.loads(getClan().content)
  members = json_object['clan']
  for member in members:
    if player1['name'] == member['name']:
      inSkyward = True
      
  if inSkyward == True:
    res = player1['name'] + "+" + player2['name']
  else:
    res = player2['name'] + "+" + player1['name']
    print(res)
  return res
