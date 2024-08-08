import aiohttp
import asyncio
import json
from Ranknir.modules.env import env_variable
import requests

BRAWLHALLA_API_KEY = env_variable("BRAWLHALLA_API_KEY")
DADABASE_API_KEY = env_variable("DADABASE_API_KEY")
HOST_PORT = env_variable("HOST_PORT")
HOST_IP = env_variable("HOST_IP")
API_WAIT_TIME = 10  # 8 possible if only ranknir


async def fetch_clan(clan_id):
    await asyncio.sleep(API_WAIT_TIME)  # 0.10 might be possible
    url = f"https://api.brawlhalla.com/clan/{clan_id}/?api_key={BRAWLHALLA_API_KEY}"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()


async def fetch_player_ranked_stats(brawlhalla_id):
    await asyncio.sleep(API_WAIT_TIME)
    url = f"https://api.brawlhalla.com/player/{brawlhalla_id}/ranked?api_key={BRAWLHALLA_API_KEY}"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()
        
async def request_clan_data_from_dadabase(id: int):
    json_object = requests.get(f"http://{HOST_IP}:{HOST_PORT}/get_clan_data?api_key={DADABASE_API_KEY}&id={id}")      
    data = json.loads(json_object.content)
    return data

async def request_server_data_from_dadabase(id: int):
    json_object = requests.get(f"http://{HOST_IP}:{HOST_PORT}/get_server_data?api_key={DADABASE_API_KEY}&id={id}")      
    data = json.loads(json_object.content)
    return data

# Deprecated


# def fetch_console_players(id):
#     json_object = requests.get(
#         "http://game-node01.jetstax.com:27046//get_ps4_players/api_key="+os.environ[4]+'?id=' + str(id))
#     data = json.loads(json_object.content)
#     return data['ps4_players']


# test api
# https://api.brawlhalla.com/player/7364605/ranked?api_key=
# https://api.brawlhalla.com/clan/84648/?api_key=
