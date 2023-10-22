from data.clan_data import Pandation, Tews

async def spit_fire(bot):
  channel = bot.get_channel(Tews.channel_rotating_id)
  msg = ('🔥')
  await channel.send(msg)
