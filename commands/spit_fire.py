from classes.Clan import Clan
from modules.data_management import load_clan


async def spit_fire(bot, server_id):
    msg = ('🔥')
    clan:Clan = load_clan(server_id)
    
    # 1v1 Channel
    try:
        channel = bot.get_channel(clan.channel_1v1_id)
        await channel.send(msg)
    except:
        await bot.response.send_message('No access to 1v1 channel')
    # 2v2 Channel
    try:
        channel = bot.get_channel(clan.channel_2v2_id)
        await channel.send(msg)
    except:
        await bot.response.send_message('No access to 2v2 channel')
    # Rotational Channel
    try:
        channel = bot.get_channel(clan.channel_rotating_id)
        await channel.send(msg)
    except:
        await bot.response.send_message('No access to Rotational channel')