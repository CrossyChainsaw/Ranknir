# Last Update: 16/10/2023
# Way Ahead of master as always

import discord
import os
from discord.ext import commands
from modules2.keep_alive import keep_alive
from modules2.ping import ping
from modules2.spit_fire import spit_fire
from modules2.elo_list import clan_console_mix_1v1_elo_list, clan_console_mix_1v1_and_2v2_elo_list, server_1v1_and_2v2_elo_list
from data.clan_data import test_clan, Obsessive, Pandation, Excalibur, Tews, Tews1, Frost, sword, ChinaT0wn, Skyward, GuiIIotine
from data.server_data import Brawlhalla_NL
from modules2.turn import next_turn, get_turn, reset_turn, prev_turn

intents = discord.Intents().all()
bot = commands.Bot(command_prefix=['r!', 'R!'], intents=intents)


@bot.event
async def on_ready():
  print(f'We have logged in as {bot.user}')
  channel = bot.get_channel(test_clan.channel_1v1_id)
  await channel.send("I'm back online!")

  while True:
    turn = get_turn()
    print("current turn: " + str(turn))

    if turn == 1:
      await clan_console_mix_1v1_and_2v2_elo_list(Pandation, bot)
    elif turn == 2:
      await clan_console_mix_1v1_and_2v2_elo_list(Excalibur, bot)
    elif turn == 3:
      await clan_console_mix_1v1_and_2v2_elo_list(Tews, bot)
    elif turn == 5:
      await clan_console_mix_1v1_and_2v2_elo_list(Frost, bot)
    elif turn == 7:
      await server_1v1_and_2v2_elo_list(Brawlhalla_NL, bot)
    elif turn == 8:
      await clan_console_mix_1v1_and_2v2_elo_list(ChinaT0wn, bot)
      
    elif turn == 69:
      await clan_console_mix_1v1_and_2v2_elo_list(test_clan, bot)
      prev_turn()
    elif turn == 101:
      print("Entered Debugging")
      break;
      
    elif turn == 9:
      await clan_console_mix_1v1_and_2v2_elo_list(GuiIIotine, bot)
      reset_turn()
    next_turn()


@bot.command(name='ping')
async def command_ping(ctx):
  await ping(ctx)

@bot.command(name='spit')
async def command_spit_fire(ctx):
  await spit_fire(bot)

keep_alive()
bot.run(os.environ['RANKNIR_TOKEN'])
