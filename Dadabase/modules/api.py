import json
import requests
from Dadabase.modules.env import env_variable
BRAWLHALLA_API_KEY = env_variable("BRAWLHALLA_API_KEY")

def fetch_player_ranked_stats(brawlhalla_id):
    json_object = requests.get("https://api.brawlhalla.com/player/{brawlhalla_id}/ranked?api_key={BRAWLHALLA_API_KEY}")
    return json.loads(json_object.content)


def fetch_player_stats(brawlhalla_id):
    json_object = requests.get("https://api.brawlhalla.com/player/{brawlhalla_id}/stats?api_key={BRAWLHALLA_API_KEY}")
    return json.loads(json_object.content)
