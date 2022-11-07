import os
import discord
from discord.ext import commands
from keep_alive import keep_alive
from embed import send_embeds2
from sort_elo import sort_elo_1v1, sort_2v2_elo
from wait import wait
from turn import get_turn, next_turn, reset_turn
from clan import Clan
from get_members_elo import get_clans

#TODO FIX PREAPRE EMBEDS

Skyward = Clan("NO ACCESS", 976552050953437194, '84648', 0x289fb4, 'https://cdn.discordapp.com/attachments/841405262023884820/841405879496212530/Skyward-1.png')

lnsomnia = Clan(988484998799716423, 1006780905131614280, '1919781', 0x301834, "https://cdn.discordapp.com/attachments/967468594285924382/1006783742179823646/Insomnia_Logo_Concept_Purple.png")
Parasomnia = Clan("N/A", "N/A", '1927502', "N/A", "N/A")
Hypnosia = Clan("N/A", "N/A", '2022800', "N/A", "N/A")

Pandation = Clan(990292557386899527, 1016402549491912794, '1702413', 0x212226, "https://cdn.discordapp.com/attachments/954800788130136064/1016402444810453012/logo_final.jpg")
Pandace = Clan("N/A", "N/A", '1868949', "N/A", "N/A")
Panhalla = Clan("N/A", "N/A", '1709279', "N/A", "N/A")
PanhaIIa = Clan("N/A", "N/A", '1722822', "N/A", "N/A")


Dair = Clan("NO ACCESS", 1029669276363280414, '1357965', 0x349feb,        'https://cdn.discordapp.com/attachments/994165604602880031/1024740143015399424/unknown.png')

Cybers = Clan(1039202472536834108, 1039202527398334514, '1983079', 0xD10000, " ")
Cybers_II = Clan("N/A", "N/A", '1983274', "N/A", "N/A")

# Testing
test_channel_id = 973594560368373820
wanak1n_clan_id = '1363653'
test2_clan_id = '2021161'
test3_clan_id = '2023962'

# insomnia_clan_id, insomnia_elo_channel_id, insomnia_image
# skyward_clan_id, skyward_elo_channel_id, skyward_image

bot = commands.Bot(command_prefix=['r', 'R'])


@bot.event
async def on_ready():
    # I'm back online!
    print(f'We have logged in as {bot.user}')
    skyward_log_channel_id = bot.get_channel(973594560368373820)
    await skyward_log_channel_id.send("I'm back online!")

    # main, send 1v1 / 2v2 elo list
    while True:
        turn = get_turn()
        print("current turn: " + str(turn))
        if turn == 0:
            await main_2v2_crazy([Dair.clan_id],
                           Dair.channel_2v2_id,
                           Dair.image,
                           Dair.color,
                           sorting_method="current")
        elif turn == 1:
            await main_1v1_crazy([Pandation.clan_id,
                                 Pandace.clan_id, Panhalla.clan_id, PanhaIIa.clan_id],
                                 Pandation.channel_1v1_id,
                                 Pandation.image,
                                 Pandation.color,
                                 sorting_method="peak")
        elif turn == 2:
            await main_2v2_crazy([Pandation.clan_id,
                           Pandace.clan_id],
                           Pandation.channel_2v2_id,
                           Pandation.image,
                           Pandation.color,
                           sorting_method="peak")
        elif turn == 3:
            await main_2v2_crazy([lnsomnia.clan_id,
                           Parasomnia.clan_id, Hypnosia.clan_id],
                           lnsomnia.channel_2v2_id,
                           lnsomnia.image,
                           lnsomnia.color,
                           sorting_method="peak")

        elif turn == 4:
            await main_1v1_crazy([lnsomnia.clan_id,
                           Parasomnia.clan_id, Hypnosia.clan_id],
                           lnsomnia.channel_1v1_id,
                           lnsomnia.image,
                           lnsomnia.color,
                           sorting_method="peak")
        elif turn == 21:
            await main_2v2_crazy([wanak1n_clan_id],
                           test_channel_id,
                           lnsomnia.image,
                           lnsomnia.color,
                           sorting_method="current")
        elif turn == 5:
            await main_1v1_crazy([Cybers.clan_id,
                           Cybers_II.clan_id],
                           Cybers.channel_1v1_id,
                           Cybers.image,
                           Cybers.color,
                           sorting_method="current")
        elif turn == 6:
            await main_2v2_crazy([Cybers.clan_id,
                           Cybers_II.clan_id],
                           Cybers.channel_2v2_id,
                           Cybers.image,
                           Cybers.color,
                           sorting_method="current")
            reset_turn()
        next_turn()
        #wait(2500)
def prepare_embeds_new(clan_array, names, current_ratings, peak_ratings, clan_color):

  print('start preparing embeds')
  print('clan array')
  print(len(clan_array))
  print('')
  print(clan_array[0])
  
  if len(clan_array) == 1:
    
    embed2 = discord.Embed(title=clan_array[0]['clan_name'], description="Total Exp: " + str(clan_array[0]['clan_xp']), color=clan_color)
    print('h')
    
  elif len(clan_array) > 1:
    embed2 = discord.Embed(
      title="", description="", color=clan_color)
    
    # Title
    count = 0
    for clan in clan_array:
      if count == 0:
        embed2.title += clan['clan_name'] 
      else:
        embed2.title += " & " + clan_array[count]['clan_name']
      count+=1

    print('test')
    # Description
    count = 0
    for clan in clan_array:
      if count == 0:
        embed2.description += clan['clan_name'] + " Exp: " + str(clan['clan_xp']) 
      else:
        embed2.description += "\n" + clan_array[count]['clan_name'] + " Exp: " + str(clan_array[count]['clan_xp'])
      count+=1

    print('hi ')
    # total xp in desc.
    total_xp = 0
    i = 0
    while i < count:
      total_xp += int(clan_array[i]['clan_xp'])
      i+=1
    embed2.description += "\nTotal Exp: " + str(total_xp)
    
    

  embed_array = []
  global rank
  rank = 1
  count = 0
  embed = discord.Embed(description="", color=clan_color)
  
  print(len(names))
  for (name, current, peak) in zip(names, current_ratings, peak_ratings):
    if count == 0:
      print('creating dc embed')
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

async def main_1v1_crazy(clan_id_array, channel_id, clan_image, clan_color, sorting_method):

  # get players elo sorted
  names, current_ratings, peak_ratings = sort_elo_1v1(clan_id_array, sorting_method)
  print(names)

  # get clans
  clans = get_clans(clan_id_array)

  # prep embeds
  embed2, embed_array = prepare_embeds_new(clans , names, current_ratings, peak_ratings, clan_color)
  
  await send_embeds2(embed2, embed_array,
                    bot=bot,
                    channel_id=channel_id,
                    clan_image=clan_image)

  # clear arrays
  names.clear()
  current_ratings.clear()
  peak_ratings.clear()




async def main_2v2_crazy(clan_id_array, channel_id, clan_image, clan_color, sorting_method):
  
  # get players elo sorted
  names, current_ratings, peak_ratings = sort_2v2_elo(clan_id_array, sorting_method)

  # get clans
  clans = get_clans(clan_id_array)

  # prep embeds
  embed2, embed_array = prepare_embeds_new(clans, names, current_ratings, peak_ratings, clan_color)

  await send_embeds2(embed2, embed_array, bot=bot, channel_id=channel_id, clan_image=clan_image)
  
  # clear arrays
  names.clear()
  current_ratings.clear()
  peak_ratings.clear()


keep_alive()
bot.run(os.environ['BOT_KEY'])
