from data.clan_data import Pandation

async def spit_fire(bot):
  channel = bot.get_channel(Pandation.channel_rotating_id)
  msg = ('🔥')
  await channel.send(msg)
