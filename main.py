# Last Update: 16/10/2023
# Way Ahead of master as always
# last added: way to individual elo

import discord
import os
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions
from modules2.keep_alive import keep_alive
from modules2.ping import ping
from modules2.spit_fire import spit_fire
from modules2.elo_list import clan_console_mix_1v1_elo_list, clan_console_mix_1v1_and_2v2_elo_list, clan_console_mix_1v1_and_2v2_and_rotating_elo_list, server_1v1_and_2v2_and_rotating_elo_list
from data.clan_data import test_clan, Pandation, Excalibur, Tews, Frost, ChinaT0wn, GuiIIotine, KryptX
from data.server_data import Brawlhalla_NL
from modules2.turn import next_turn, get_turn, reset_turn, prev_turn
from modules2.all_legends_elo import send_all_legends_elo
from modules2.leave_server import leave_server

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

        # Clans / Servers
        if turn == 0:
            await clan_console_mix_1v1_and_2v2_and_rotating_elo_list(Pandation, bot)
        elif turn == 1:
            await clan_console_mix_1v1_and_2v2_elo_list(Excalibur, bot)
        elif turn == 2:
            await clan_console_mix_1v1_and_2v2_and_rotating_elo_list(Tews, bot)
        elif turn == 3:
            await clan_console_mix_1v1_and_2v2_elo_list(Frost, bot)
        elif turn == 4:
            await server_1v1_and_2v2_and_rotating_elo_list(Brawlhalla_NL, bot)
        elif turn == 5:
            await clan_console_mix_1v1_and_2v2_elo_list(ChinaT0wn, bot)
        elif turn == 6:
            await clan_console_mix_1v1_and_2v2_elo_list(KryptX, bot)
        elif turn == 7:
            ...  # empty
        # Test Clan
        elif turn == 69:
            await clan_console_mix_1v1_and_2v2_and_rotating_elo_list(test_clan, bot)
            prev_turn
        # Debugging
        elif turn == 101:
            print("Entered Debugging")
            break
        # Reset Q
        else:
            reset_turn()
            await send_all_legends_elo(7364605, 1165233774305493012, bot)
            await send_all_legends_elo(395872, 1166526510526631998, bot)
            await send_all_legends_elo(4244083, 1166648209368686642, bot)
            await send_all_legends_elo(15554673, 1173667369160298506, bot)
        next_turn()


@bot.command(name='ping')
async def command_ping(ctx):
    await ping(ctx)


@bot.command(name='spit')
@has_permissions(manage_roles=True, ban_members=True)
async def command_spit_fire(ctx):
    await spit_fire(bot)


@bot.command(name='leave')
async def leave_server_command(ctx, server_id):
    await leave_server(bot, ctx, server_id)

keep_alive()
bot.run(os.environ['RANKNIR_BOT_KEY'])
