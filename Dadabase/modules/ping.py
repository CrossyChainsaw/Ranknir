import random

async def ping(interaction):
  num = random.randrange(0, 8192)
  if num == 1:
    msg = ("bong")
  else:
    msg = ('pong')
  await interaction.response.send_message(msg)

  
  