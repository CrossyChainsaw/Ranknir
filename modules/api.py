import aiohttp
import asyncio
import json
from Ranknir.modules.env import env_variable
import requests

BRAWLHALLA_API_KEY = env_variable("BRAWLHALLA_API_KEY")
DADABASE_API_KEY = env_variable("DADABASE_API_KEY")
HOST_PORT = env_variable("HOST_PORT")
ACTIVE_IP = env_variable("ACTIVE_IP")

API_WAIT_TIME = 9.9  # 9.9 works // 8 possible if only ranknir


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
    json_object = requests.get(f"http://{ACTIVE_IP}:{HOST_PORT}/get_clan_data?api_key={DADABASE_API_KEY}&id={id}")      
    data = json.loads(json_object.content)
    return data

async def request_server_data_from_dadabase(id: int):
    json_object = requests.get(f"http://{ACTIVE_IP}:{HOST_PORT}/get_server_data?api_key={DADABASE_API_KEY}&id={id}")      
    data = json.loads(json_object.content)
    return data