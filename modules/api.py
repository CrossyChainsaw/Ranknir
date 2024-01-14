import requests
import time
import json
import asyncio
from classes.Xos import Xos
os = Xos()

# VARIABLES
API_WAIT_TIME = 8.5  # 9

# METHODS


async def fetch_clan(clan_id):
    await asyncio.sleep(API_WAIT_TIME)  # 0.10 might be possible
    json_object = requests.get(
        "https://api.brawlhalla.com/clan/" + str(clan_id) + "/?api_key=" + os.environ[0])
    return json.loads(json_object.content)


async def fetch_player_ranked_stats(brawlhalla_id):
    await asyncio.sleep(API_WAIT_TIME)
    json_object = requests.get("https://api.brawlhalla.com/player/" +
                               str(brawlhalla_id) + "/ranked?api_key="+os.environ[0])
    return json.loads(json_object.content)

# Deprecated


def fetch_console_players(id):
    json_object = requests.get(
        "http://game-node01.jetstax.com:27046//get_ps4_players/api_key="+os.environ[4]+'?id=' + str(id))
    data = json.loads(json_object.content)
    return data['ps4_players']


# test api
# https://api.brawlhalla.com/player/7364605/ranked?api_key=
# https://api.brawlhalla.com/clan/84648/?api_key=
