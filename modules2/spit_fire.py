from data.clan_data import Pandation

async def spit_fire(bot):
  channel = bot.get_channel(Pandation.channel_2v2_id)
  msg = ('🔥')
  await channel.send(msg)
