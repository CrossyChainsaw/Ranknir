from Ranknir.data.clan_data import Pandation, Tews, KryptX
from Ranknir.data.server_data import Brawlhalla_NL, M3OW


async def spit_fire(bot):
    msg = ('🔥')
    channel = bot.get_channel(M3OW.channel_1v1_id)
    await channel.send(msg)
    channel = bot.get_channel(M3OW.channel_2v2_id)
    await channel.send(msg)
    channel = bot.get_channel(M3OW.channel_rotating_id)
    await channel.send(msg)
