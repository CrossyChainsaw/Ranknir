from secrets import get_keys
import os
import discord
from discord.ext import commands
from keep_alive import keep_alive
from embed import send_embeds, send_embeds2
from sort_elo import sort_teams_elo, sort_players_elo, sort_players_elo_multi, sort_teams_elo_multi, sort_elo_1v1
from wait import wait
from turn import get_turn, next_turn, reset_turn
from clan import Clan
from get_members_elo import get_clans

#TODO FIX PREAPRE EMBEDS

skyward = Clan("NO ACCESS", 976552050953437194, '84648', 0x289fb4, 'https://cdn.discordapp.com/attachments/841405262023884820/841405879496212530/Skyward-1.png')
insomnia = Clan(988484998799716423, 1006780905131614280, '1919781', 0x301834, "https://cdn.discordapp.com/attachments/967468594285924382/1006783742179823646/Insomnia_Logo_Concept_Purple.png")
parasomnia = Clan("N/A", "N/A", '1927502', "N/A", "N/A")
pandation = Clan(990292557386899527, 1016402549491912794, '1702413', 0x212226, "https://cdn.discordapp.com/attachments/954800788130136064/1016402444810453012/logo_final.jpg")
pandace = Clan("N/A", "N/A", '1868949', "N/A", "N/A")
dair = Clan("NO ACCESS", 1029669276363280414, '1357965', 0x349feb, 'https://cdn.discordapp.com/attachments/994165604602880031/1024740143015399424/unknown.png')

# Skyward
skyward_2v2_elo_channel_id = 976552050953437194
skyward_clan_id = '84648'
skyward_color = 0x289fb4
skyward_image = 'https://cdn.discordapp.com/attachments/841405262023884820/841405879496212530/Skyward-1.png'

# Insomnia
insomnia_1v1_elo_channel_id = 988484998799716423
insomnia_2v2_elo_channel_id = 1006780905131614280
insomnia_clan_id = '1919781'
insomnia_color = 0x301834
insomnia_image = "https://cdn.discordapp.com/attachments/967468594285924382/1006783742179823646/Insomnia_Logo_Concept_Purple.png"

# Parasomnia
parasomnia_clan_id = '1927502'

# Hypnosia
hypnosia_clan_id = '2022800'

# Pandation
pandation_1v1_elo_channel_id = 990292557386899527
pandation_2v2_elo_channel_id = 1016402549491912794
pandation_clan_id = '1702413'
pandation_color = 0x212226
pandation_image = "https://cdn.discordapp.com/attachments/954800788130136064/1016402444810453012/logo_final.jpg"

# Pandace
pandace_clan_id = '1868949'

# Blossom | Test Clan
blossom_1v1_elo_channel_id = 973594560368373820
blossom_2v2_elo_channel_id = 973594560368373820
blossom_clan_id = '1998475'
blossom_color = 0xfebdff
blossom_image = "this_clan_has_no_image"

# Dair
dair_2v2_elo_channel_id = 1029669276363280414
dair_clan_id = '1357965'
dair_color = 0x349feb
dair_image = 'https://cdn.discordapp.com/attachments/994165604602880031/1024740143015399424/unknown.png'

# Testing
boo_clan_id = '2'
test_channel_id = 973594560368373820
unsung_zeroes_clan_id = '7'
wanak1n_clan_id = '1363653'
stop_teleporting_clan_id = '2021163'
idiosyncrasy_clan_id = '2023963'

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
            await main_1v1_multi(pandation_clan_id,
                                 pandace_clan_id,
                                 pandation_1v1_elo_channel_id,
                                 pandation_image,
                                 pandation_color,
                                 sorting_method="peak")
        elif turn == 1:
            await main_2v2_multi(insomnia_clan_id,
                           parasomnia_clan_id,
                           insomnia_2v2_elo_channel_id,
                           insomnia_image,
                           insomnia_color,
                           sorting_method="peak")
        elif turn == 2:
            await main_2v2(dair_clan_id,
                           dair_2v2_elo_channel_id,
                           dair_image,
                           dair_color,
                           sorting_method="current")
        elif turn == 3:
            await main_2v2_multi(pandation_clan_id,
                           pandace_clan_id,
                           pandation_2v2_elo_channel_id,
                           pandation_image,
                           pandation_color,
                           sorting_method="peak")
        elif turn == 4:
            await main_1v1_crazy([insomnia_clan_id,
                           parasomnia_clan_id, hypnosia_clan_id],
                           insomnia_1v1_elo_channel_id,
                           insomnia_image,
                           insomnia_color,
                           sorting_method="peak")
        elif turn == 5:
            await main_1v1(unsung_zeroes_clan_id,
                           test_channel_id,
                           insomnia_image,
                           insomnia_color,
                           sorting_method="peak")
            reset_turn()
        next_turn()
        wait(2500)
def prepare_embeds_new(clan_array, names, current_ratings, peak_ratings, clan_color):

  
  
  if len(clan_array) == 1:
    embed2 = discord.Embed(title=clan_array[0]['clan_name'], description="Total Exp: " + str(clan_array[0]['clan_xp']), color=clan_color)
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

    # Description
    count = 0
    for clan in clan_array:
      if count == 0:
        embed2.description += clan['clan_name'] + " Exp: " + str(clan['clan_xp']) 
      else:
        embed2.description += "\n" + clan_array[count]['clan_name'] + " Exp: " + str(clan_array[1]['clan_xp'])
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

    print(len(names))
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
    return embed2, embed_array

def prepare_embeds(clan, names_sorted, current_sorted, peak_sorted, clan_color):
  embed2 = discord.Embed(title=clan['clan_name'], description="Total Exp: " + str(clan['clan_xp']), color=clan_color)
  embed3 = discord.Embed(description="", color=clan_color)
  embed4 = discord.Embed(description="", color=clan_color)
  embed5 = discord.Embed(description="", color=clan_color)
  embed6 = discord.Embed(description="", color=clan_color)
  embed7 = discord.Embed(description="", color=clan_color)
  global num
  num = 1

  for (name, current, peak) in zip(names_sorted, current_sorted, peak_sorted):
    if num <= 20:
        embed3.description += "**" + \
            str(num) + ". " + name + "**: current: **" + str(current) + "** peak: **" + str(peak) + '**\n'
    elif num <= 40:
        embed4.description += "**" + \
            str(num) + ". " + name + "**: current: **" + str(current) + "** peak: **" + str(peak) + '**\n'
    elif num <= 60:
        embed5.description += "**" + \
            str(num) + ". " + name + "**: current: **" + str(current) + "** peak: **" + str(peak) + '**\n'
    elif num <= 80:
        embed6.description += "**" + \
            str(num) + ". " + name + "**: current: **" + str(current) + "** peak: **" + str(peak) + '**\n'
    else:
        embed7.description += "**" + \
            str(num) + ". " + name + "**: current: **" + str(current) + "** peak: **" + str(peak) + '**\n'
    num += 1
  return embed2, embed3, embed4, embed5, embed6, embed7


def prepare_embeds_multi(clan_1, clan_2, names_sorted, current_sorted, peak_sorted, clan_color):
  # prepare embeds - make this a diff method
  embed2 = discord.Embed(
      title=clan_1['clan_name'] + " & " + clan_2['clan_name'],
      description=clan_1['clan_name'] + " Exp: " + str(clan_1['clan_xp']) +
      "\n" + clan_2['clan_name'] + " Exp: " + str(clan_2['clan_xp']) +
      "\nTotal Exp: " + str(int(clan_1['clan_xp']) + int(clan_2['clan_xp'])),
      color=clan_color)
  embed3 = discord.Embed(description="", color=clan_color)
  embed4 = discord.Embed(description="", color=clan_color)
  embed5 = discord.Embed(description="", color=clan_color)
  embed6 = discord.Embed(description="", color=clan_color)
  embed7 = discord.Embed(description="", color=clan_color)
  global num
  num = 1

  for (name, current, peak) in zip(names_sorted, current_sorted,
                                   peak_sorted):
    if num <= 20:
      embed3.description += "**" + \
            str(num) + ". " + name + "**: current: **" + str(current) + "** peak: **" + str(peak) + '**\n'
    elif num <= 40:
      embed4.description += "**" + \
            str(num) + ". " + name + "**: current: **" + str(current) + "** peak: **" + str(peak) + '**\n'
    elif num <= 60:
      embed5.description += "**" + \
                          str(num) + ". " + name + "**: current: **" + str(current) + "** peak: **" + str(peak) + '**\n'
    elif num <= 80:
      embed6.description += "**" + \
            str(num) + ". " + name + "**: current: **" + str(current) + "** peak: **" + str(peak) + '**\n'
    else:
      embed7.description += "**" + \
            str(num) + ". " + name + "**: current: **" + str(current) + "** peak: **" + str(peak) + '**\n'

    num += 1
  return embed2, embed3, embed4, embed5, embed6, embed7
async def main_1v1(clan_id, channel_id, clan_image, clan_color, sorting_method):
  # get players elo sorted
  names_sorted, current_sorted, peak_sorted, clan = sort_players_elo(clan_id, sorting_method=sorting_method)
  # prepare embeds
  embed2, embed3, embed4, embed5, embed6, embed7 = prepare_embeds(clan, names_sorted, current_sorted, peak_sorted, clan_color)

  # send embeds
  await send_embeds(embed2=embed2, embed3=embed3, embed4=embed4, embed5=embed5, embed6=embed6, embed7=embed7, bot=bot, channel_id=channel_id, clan_image=clan_image)

  # clear arrays
  names_sorted.clear()
  current_sorted.clear()
  peak_sorted.clear()


async def main_2v2(clan_id, channel_id, clan_image, clan_color,
                   sorting_method):
  # get teams, current and peak elo's sorted
  teamnames_sorted, current_sorted, peak_sorted, clan = sort_teams_elo(
      clan_id, sorting_method)

  print('start preparing embeds')
  # prepare embeds
  embed2, embed3, embed4, embed5, embed6, embed7 = prepare_embeds(clan, teamnames_sorted, current_sorted, peak_sorted, clan_color)

  await send_embeds(embed2=embed2,
                      embed3=embed3,
                      embed4=embed4,
                      embed5=embed5,
                      embed6=embed6,
                      embed7=embed7,
                      bot=bot,
                      channel_id=channel_id,
                      clan_image=clan_image)

  # clear arrays
  current_sorted.clear()
  peak_sorted.clear()
  teamnames_sorted.clear()


async def main_1v1_multi(clan_id_1, clan_id_2, channel_id, clan_image,
                         clan_color, sorting_method):
  # get players elo sorted
  names_sorted, current_sorted, peak_sorted, clan_1, clan_2 = sort_players_elo_multi(
      clan_id_1, clan_id_2, sorting_method=sorting_method)

  embed2, embed3, embed4, embed5, embed6, embed7 = prepare_embeds_multi(clan_1, clan_2, names_sorted, current_sorted, peak_sorted, clan_color)
                         
  await send_embeds(embed2=embed2,
                    embed3=embed3,
                    embed4=embed4,
                    embed5=embed5,
                    embed6=embed6,
                    embed7=embed7,
                    bot=bot,
                    channel_id=channel_id,
                    clan_image=clan_image)

  # clear arrays
  names_sorted.clear()
  current_sorted.clear()
  peak_sorted.clear()

async def main_2v2_multi(clan_id_1, clan_id_2, channel_id, clan_image, clan_color, sorting_method):
    
  # get players elo sorted
  names_sorted, current_sorted, peak_sorted, clan_1, clan_2 = sort_teams_elo_multi(
      clan_id_1, clan_id_2, sorting_method=sorting_method)

  embed2, embed3, embed4, embed5, embed6, embed7 = prepare_embeds_multi(clan_1, clan_2, names_sorted, current_sorted, peak_sorted, clan_color)
  await send_embeds(embed2=embed2,
                    embed3=embed3,
                    embed4=embed4,
                    embed5=embed5,
                    embed6=embed6,
                    embed7=embed7,
                    bot=bot,
                    channel_id=channel_id,
                    clan_image=clan_image)

  # clear arrays
  names_sorted.clear()
  current_sorted.clear()
  peak_sorted.clear()


async def main_1v1_crazy(clan_id_array, channel_id, clan_image, clan_color, sorting_method):

  # get players elo sorted
  names, current_ratings, peak_ratings = sort_elo_1v1(clan_id_array, sorting_method)
  print(names)
  
  clans = get_clans(clan_id_array)

  embed2, embed_array = prepare_embeds_new(clans , names, current_ratings, peak_ratings, clan_color)
  
  await send_embeds2(embed2, embed_array,
                    bot=bot,
                    channel_id=channel_id,
                    clan_image=clan_image)

  # clear arrays
  names.clear()
  current_ratings.clear()
  peak_ratings.clear()




keep_alive()
bot.run(os.environ['BOT_KEY'])
