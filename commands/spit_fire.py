from Ranknir.classes.Clan import Clan
from Ranknir.modules.data_management import load_clan

PURGE_LIMIT = 5

async def spit_fire(bot, ctx, server_id):
    msg = ('🔥')
    clan:Clan = await load_clan(server_id)
    
    # 1v1 Channel
    try:
        channel = bot.get_channel(clan.channel_1v1_id)
        await channel.purge(limit=PURGE_LIMIT)
        await channel.send(msg)
    except:
        await ctx.channel.send('No access to 1v1 channel')
    # 2v2 Channel
    try:
        channel = bot.get_channel(clan.channel_2v2_id)
        await channel.purge(limit=PURGE_LIMIT)        
        await channel.send(msg)
    except:
        await ctx.channel.send('No access to 2v2 channel')
    # Rotational Channel
    try:
        channel = bot.get_channel(clan.channel_rotating_id)
        await channel.purge(limit=PURGE_LIMIT)
        await channel.send(msg)
    except:
        await ctx.channel.send('No access to Rotational channel')