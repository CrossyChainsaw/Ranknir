import random as rnd

async def leave_server(bot, ctx, server_id):
  author_id = ctx.author.id
  CrossyChainsaw_id = 413070742591373314
  if author_id == CrossyChainsaw_id:
    guild = bot.get_guild(int(server_id))
    await ctx.channel.send(f"leaving {guild.name} *(Ranknir sd'd by slide charging {get_random_sig()} for too long)*")
    await guild.leave()

def get_random_sig():
  r = rnd.randint(1, 6)
  if r == 1:
    return 'axe nsig'
  elif r == 2:
    return 'axe ssig'
  elif r == 3:
    return 'axe dsig'
  elif r == 4:
    return 'katar nsig'
  elif r == 5:
    return 'katar ssig'
  elif r == 6:
    return 'katar dsig'