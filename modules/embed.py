import discord
from modules.wait import wait

# Public

async def send_embeds2(embed2, embed_array, bot, channel_id, clan_image):
  channel = bot.get_channel(channel_id)
  print('channel')
  print(channel)

  # Remove last 20 messages in channel
  await channel.purge(limit=30)

  # Send Image
  try:
    await channel.send(clan_image)
    print("sent 1")
  except:
    print('NO IMAGE PROVIDED')

  # Send Embed 2
  await channel.send(embed=embed2)
  print("sent 2")

  num = 3
  for embed in embed_array:
    # Send Embed (if possible)
    if len(embed.description) > 0:
      await channel.send(embed=embed)
      print('sent ' + str(num))
      wait(0.5)
    num += 1

def prepare_embeds_new(clan_array, players_sorted, clan_color):
  print('start preparing embeds')
  names, current_ratings, peak_ratings = players_sorted[0], players_sorted[1], players_sorted[2]
  
  if len(clan_array) == 1:
    
    embed2 = discord.Embed(title=clan_array[0]['clan_name'], description="Total Members: " + str(len(clan_array[0]['clan'])), color=clan_color)
    
  elif len(clan_array) > 1:
    embed2 = discord.Embed(title="", description="", color=clan_color)
    
    # Title
    count = 0
    for clan in clan_array:
      if count == 0:
        embed2.title += clan['clan_name'] 
      else:
        embed2.title += " & " + clan_array[count]['clan_name']
      count+=1

    # Description
    count = 0
    for clan in clan_array:
      if count == 0:
        test = len(clan['clan'])
        embed2.description += clan['clan_name'] + ": " + str(test) + ' members' 
      else:
        embed2.description += "\n" + clan_array[count]['clan_name'] + ": " + str(test) + ' members'
      count+=1
    i = 0
    while i < count:
      test = len(clan_array[i]['clan'])
      #total_xp += int(clan_array[i]['clan_xp'])
      i+=1
    embed2.description += "\nTotal Members: " + str(test)
    
    
  # Variables
  embed_array = []
  global rank
  rank = 1
  count = 0
  embed = discord.Embed(description="", color=clan_color)

  # Format Embeds
  for (name, current, peak) in zip(names, current_ratings, peak_ratings):
    if count == 0:
      embed = discord.Embed(description="", color=clan_color)
    if count <= 20:
        embed.description += "**" + \
            str(rank) + ". " + name + "**: current: **" + str(current) + "** peak: **" + str(peak) + '**\n'
    rank += 1
    count += 1
    if count == 21:
      embed_array.append(embed)
      count = 0
  embed_array.append(embed)
  return embed2, embed_array

def prepare_embeds_new_server(server, names, current_ratings, peak_ratings, clan_color):

  print('start preparing embeds')
  
  embed2 = discord.Embed(title=server.name, color=server.color)

  # Variables
  embed_array = []
  global rank
  rank = 1
  count = 0
  embed = discord.Embed(description="", color=server.color)

  # Format Embeds
  print(len(names))
  for (name, current, peak) in zip(names, current_ratings, peak_ratings):
    if count == 0:
      embed = discord.Embed(description="", color=server.color)
    if count <= 20:
        embed.description += "**" + \
            str(rank) + ". " + name + "**: current: **" + str(current) + "** peak: **" + str(peak) + '**\n'
    rank += 1
    count += 1
    if count == 21:
      embed_array.append(embed)
      count = 0
  embed_array.append(embed)
  return embed2, embed_array

# Private