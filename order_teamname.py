from api import fetch_player_ranked_stats
from api import fetch_clan
import json


def ArrangeTeamName(teamName):
    player1_ID = teamName["brawlhalla_id_one"]
    player2_ID = teamName["brawlhalla_id_two"]
    try:
        player1 = json.loads(fetch_player_ranked_stats(player1_ID).content)
        player2 = json.loads(fetch_player_ranked_stats(player2_ID).content)
        print('p1: ' + player1['name'])
        print('p2: ' + player2['name'])

        inSkyward = False
        json_object = json.loads(fetch_clan().content)
        members = json_object['clan']
        for member in members:
            if player1['name'] == member['name']:
                inSkyward = True

        print('ordered')
        if inSkyward == True:
            res = player1['name'] + "+" + player2['name']
        else:
            res = player2['name'] + "+" + player1['name']
            print(res)
        return res
    except:
        print('not ordered')
        print(teamName['teamname'])
        return teamName['teamname']
