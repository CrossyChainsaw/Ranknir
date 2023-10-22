from data.clan_data import Pandation, Tews
from data.server_data import Brawlhalla_NL

async def spit_fire(bot):
  channel = bot.get_channel(Brawlhalla_NL.channel_rotating_id)
  msg = ('🔥')
  await channel.send(msg)
