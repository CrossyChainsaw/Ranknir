from secrets import get_keys
import os
import requests
import time
import json

# VARIABLES
lilly_clan_id = '864398'
poopy_blender_clan_id = '1923622'

# METHODS
def fetch_clan(clan_id):
  time.sleep(0.10)  # 0.10 might be possible
  json_object = requests.get("https://api.brawlhalla.com/clan/" + clan_id + "/?api_key=" + os.environ['API_KEY'])
  return json.loads(json_object.content)


def fetch_player_ranked_stats(brawlhalla_id):
  time.sleep(10)
  json_object = requests.get("https://api.brawlhalla.com/player/" +
                        str(brawlhalla_id) + "/ranked?api_key="+os.environ['API_KEY'])
  return json.loads(json_object.content)

def get_ps4_players_api(id):
  json_object = requests.get("http://game-node01.jetstax.com:27046//get_ps4_players/api_key="+os.environ['API_KEY_DADABASE']+'?id=' + id)
  data = json.loads(json_object.content)  
  return data['ps4_players']
# test api
# https://api.brawlhalla.com/player/7364605/ranked?api_key=
# https://api.brawlhalla.com/clan/84648/?api_key=
