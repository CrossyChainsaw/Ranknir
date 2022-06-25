import os
import requests
import time
from secrets import get_keys

# VARIABLES
skyward_clan_id = "84648"
lilly_clan_id = '864398'
poopy_blender_clan_id = '1923622'
using_clan = skyward_clan_id

# METHODS


def getClan():
    time.sleep(0.10)  # 0.10 might be possible
    return requests.get("https://api.brawlhalla.com/clan/" + using_clan + "/?api_key=" + get_keys(1))


def getPlayerStats(brawlhalla_id):
    time.sleep(10)
    return requests.get("https://api.brawlhalla.com/player/" +
                        str(brawlhalla_id) + "/ranked?api_key=" + get_keys(1))

# test api
# https://api.brawlhalla.com/player/7364605/ranked?api_key=
# https://api.brawlhalla.com/clan/84648/?api_key=
