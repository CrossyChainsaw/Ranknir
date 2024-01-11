from data.clan_data import Pandation, Tews, KryptX, Empire_United
from data.server_data import Brawlhalla_NL


async def spit_fire(bot):
    msg = ('🔥')
    channel = bot.get_channel(Empire_United.channel_1v1_id)
    await channel.send(msg)
    # channel = bot.get_channel(KryptX.channel_2v2_id)
    # await channel.send(msg)
