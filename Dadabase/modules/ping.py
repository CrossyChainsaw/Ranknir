import random

async def ping(ctx):
  num = random.randrange(0, 8192)
  if num == 1:
    msg = ("bong")
  else:
    msg = ('pong')
  await ctx.channel.send(msg)

  
  