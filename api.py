from secrets import get_keys
import os
import requests
import time

# VARIABLES
lilly_clan_id = '864398'
poopy_blender_clan_id = '1923622'

# METHODS
def fetch_clan(clan_id):
    time.sleep(0.10)  # 0.10 might be possible
    return requests.get("https://api.brawlhalla.com/clan/" + clan_id + "/?api_key=" + os.environ['API_KEY'])


def fetch_player_ranked_stats(brawlhalla_id):
    time.sleep(9)
    return requests.get("https://api.brawlhalla.com/player/" +
                        str(brawlhalla_id) + "/ranked?api_key="+os.environ['API_KEY'])

# test api
# https://api.brawlhalla.com/player/7364605/ranked?api_key=
# https://api.brawlhalla.com/clan/84648/?api_key=
