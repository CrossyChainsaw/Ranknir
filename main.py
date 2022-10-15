import os
import discord
from discord.ext import commands
from keep_alive import keep_alive
from embed import send_embeds
from sort_elo import sort_teams_elo, sort_players_elo, sort_players_elo_multi, sort_teams_elo_multi
from wait import wait
from turn import get_turn, next_turn, reset_turn

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

# BOO
boo_clan_id = '2'

# Testing
test_channel_id = 973594560368373820
test_clan_id = '7'

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
            await main_1v1_multi(insomnia_clan_id,
                           parasomnia_clan_id,
                           insomnia_1v1_elo_channel_id,
                           insomnia_image,
                           insomnia_color,
                           sorting_method="peak")
        elif turn == 5:
            await main_1v1(test_clan_id,
                           test_channel_id,
                           insomnia_image,
                           insomnia_color,
                           sorting_method="peak")
        elif turn == 6:
            await main_2v2(skyward_clan_id,
                           skyward_2v2_elo_channel_id,
                           skyward_image,
                           skyward_color,
                           sorting_method="current")
            reset_turn()
        next_turn()
        wait(2500)

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



keep_alive()
bot.run(os.environ['BOT_KEY'])
