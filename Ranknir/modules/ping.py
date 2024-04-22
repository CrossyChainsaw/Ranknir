import random

async def ping(ctx):
  rnd = random.randint(1, 3)
  if rnd == 1:
    msg = ("Please be assured that I will do my best to address any urgent tasks remotely, if possible. However, I also need to take some time off to attend to personal matters. As per our company's policy and my accrued leave entitlement, I have decided to utilize my vacation days. This decision was made after careful consideration of personal well-being and the need for rejuvenation.")
  elif rnd == 2:
    msg = ('I hope this message finds you well. I am writing to inform you of an unexpected incident that has unfortunately rendered me unable to fulfill my work duties today. Regrettably, my dog has managed to get a hold of and, quite literally, devoured my tie. Despite my best efforts to prevent this, the situation escalated unexpectedly. As a result, I find myself without a suitable attire to present myself professionally at work.')
  else:
    msg = ("As you may know, my nature as a dragon comes with its own unique set of challenges. Unfortunately, during my routine nest maintenance, I experienced a distressing incident – my baby egg accidentally slipped from its nest and fell into the depths of the volcano. Understandably, retrieving the egg is of utmost priority to me. I am currently coordinating efforts with the local volcano authorities and enacting emergency protocols to ensure the safe retrieval of my offspring. I deeply apologize for any inconvenience my absence may cause and assure you that I am committed to resolving this situation as swiftly as possible. I will keep you updated on any developments and my estimated return to work.")
  await ctx.channel.send(msg)
