import aiohttp
import asyncio
import json

API_WAIT_TIME = 10  # don't change this variable, you might get temporary blocked


async def fetch_clan_from_open_api(clan_id):
    await asyncio.sleep(API_WAIT_TIME)  # 0.10 might be possible
    url = f"https://brawlhalla.fly.dev/v1/utils/clan?clan_id={clan_id}"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            response = await response.json()
            return response['data']


async def fetch_player_ranked_stats_from_open_api(brawlhalla_id):
    await asyncio.sleep(API_WAIT_TIME)
    url = f"https://brawlhalla.fly.dev/v1/ranked/id?brawlhalla_id={brawlhalla_id}"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            response = await response.json()
            return response['data']
        
        
# Deprecated


# def fetch_console_players(id):
#     json_object = requests.get(
#         "http://game-node01.jetstax.com:27046//get_ps4_players/api_key="+os.environ[4]+'?id=' + str(id))
#     data = json.loads(json_object.content)
#     return data['ps4_players']


# test api
# https://api.brawlhalla.com/player/7364605/ranked?api_key=
# https://api.brawlhalla.com/clan/84648/?api_key=
