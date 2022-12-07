import os
import discord
from discord.ext import commands
#from modules.keep_alive import keep_alive
from modules.embed import send_embeds2, prepare_embeds_new
from modules.sort_elo import sort_elo_1v1, sort_2v2_elo
from modules.wait import wait
from modules.turn import get_turn, next_turn, reset_turn
from modules.get_members_elo import get_clans
from classes.clan import Clan

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
Xybers = Clan("N/A", "N/A", '2041304', "N/A", "N/A")

Cherimoya = Clan(1042189651118674010, "N/A", '2024340', 0x19eb8f, " ")

# Testing
test_channel_id = 973594560368373820
wanak1n_clan_id = '1363653'
test2_clan_id = '2021161'
test3_clan_id = '2023962'

# insomnia_clan_id, insomnia_elo_channel_id, insomnia_image
# skyward_clan_id, skyward_elo_channel_id, skyward_image

intents = discord.Intents().all()
bot = commands.Bot(command_prefix=['r', 'R'], intents=intents)
turn = 6

@bot.event
async def on_ready():
    # I'm back online!
    print(f'We have logged in as {bot.user}')
    skyward_log_channel_id = bot.get_channel(973594560368373820)
    await skyward_log_channel_id.send("I'm back online!")

    # main, send 1v1 / 2v2 elo list
    while True:
        #turn = get_turn()
        global turn
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
                           Pandace.clan_id, Panhalla.clan_id, PanhaIIa.clan_id],
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
                           Cybers_II.clan_id, Xybers.clan_id],
                           Cybers.channel_1v1_id,
                           Cybers.image,
                           Cybers.color,
                           sorting_method="peak")
        elif turn == 6:
            await main_2v2_crazy([Cybers.clan_id,
                           Cybers_II.clan_id, Xybers.clan_id],
                           Cybers.channel_2v2_id,
                           Cybers.image,
                           Cybers.color,
                           sorting_method="current")
        elif turn == 7:
          await main_2v2_crazy([Skyward.clan_id],
                           Skyward.channel_2v2_id,
                           Skyward.image,
                           Skyward.color,
                           sorting_method="current")
        elif turn == 8:
            await main_1v1_crazy([Cherimoya.clan_id],
                           Cherimoya.channel_1v1_id,
                           Cherimoya.image,
                           Cherimoya.color,
                           sorting_method="peak")
            reset_turn()
        turn += 1
        if turn > 8:
            turn = 0
        #next_turn()
        #wait(300)

async def main_1v1_crazy(clan_id_array, channel_id, clan_image, clan_color, sorting_method):

  # get players elo sorted
  names, current_ratings, peak_ratings = sort_elo_1v1(clan_id_array, sorting_method)
  print(names)

  # get clans
  clans = get_clans(clan_id_array)

  # prep embeds
  embed2, embed_array = prepare_embeds_new(clans , names, current_ratings, peak_ratings, clan_color)
  
  await send_embeds2(embed2, embed_array, bot=bot, channel_id=channel_id, clan_image=clan_image)

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


#keep_alive()
bot.run("OTc2NTcxNzYyMTAxODc4ODk0.G6H0Gz.G7H0oPRDj-p5yJTOCP7L_vkAk7Pu0tRZw1M30k")
