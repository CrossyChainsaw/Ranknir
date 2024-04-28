import asyncio
import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions
from Ranknir.modules.data_management import AURA_SERVER_ID, EMPIRE_UNITED_SERVER_ID, FROST_SERVER_ID, GRANT_SERVER_ID, KRYPTX_SERVER_ID, PANDATION_SERVER_ID, DIVISION_SERVER_ID, TEWS_SERVER_ID, load_clan
from Ranknir.modules.data_management import TEST_SERVER_ID, M30W_SERVER_ID, BHNL_SERVER_ID, BRAWL_HUNGARY_SERVER_ID, load_server
from Ranknir.commands.ping import ping
from Ranknir.commands.spit_fire import spit_fire
from Ranknir.modules.elo_list import clan_console_mix_1v1_elo_list, clan_console_mix_1v1_and_2v2_elo_list, clan_console_mix_1v1_and_2v2_and_rotating_elo_list, server_1v1_and_2v2_and_rotating_elo_list, server_1v1_and_2v2_elo_list
# from Ranknir.data.clan_data import test_clan, Pandation, Tews, Frost, KryptX, Empire_United, Grant, aura
from Ranknir.modules.data_management import CROSSYCHAINSAW_ID
from Ranknir.modules.turn import next_turn, get_turn, reset_turn, prev_turn
from Ranknir.modules.all_legends_elo import send_all_legends_elo
from Ranknir.commands.leave_server import leave_server
from Ranknir.modules.get_current_order import print_current_order
from Ranknir.commands.test_clan_console_mix_1v1_elo_list import test_clan_console_mix_1v1_elo_list
from Ranknir.commands.test_server_1v1_elo_list import test_server_1v1_elo_list
from Ranknir.modules.env import env_variable
import json

intents = discord.Intents().all()
bot = commands.Bot(command_prefix=['r!', 'R!'], intents=intents)



@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

    while True:
        try:
            # get turn
            print('getting turn...')
            turn = get_turn()
            print("current turn: " + str(turn))

            # Clans / Servers
            if turn == 0:
                await clan_console_mix_1v1_and_2v2_and_rotating_elo_list(load_clan(PANDATION_SERVER_ID), bot)
            elif turn == 1:
                await clan_console_mix_1v1_and_2v2_and_rotating_elo_list(load_clan(TEWS_SERVER_ID), bot)
            elif turn == 2:
                await clan_console_mix_1v1_and_2v2_elo_list(load_clan(FROST_SERVER_ID), bot)
            elif turn == 3:
                await server_1v1_and_2v2_and_rotating_elo_list(load_server(BHNL_SERVER_ID), bot)
            elif turn == 4:
                await clan_console_mix_1v1_elo_list(load_clan(EMPIRE_UNITED_SERVER_ID), bot)
            elif turn == 5:
                await clan_console_mix_1v1_and_2v2_and_rotating_elo_list(load_clan(KRYPTX_SERVER_ID), bot)
            elif turn == 6:
                await server_1v1_and_2v2_and_rotating_elo_list(load_server(M30W_SERVER_ID), bot)
            elif turn == 7:
                await clan_console_mix_1v1_and_2v2_elo_list(load_clan(GRANT_SERVER_ID), bot)
            elif turn == 8:        
                await server_1v1_and_2v2_elo_list(load_server(BRAWL_HUNGARY_SERVER_ID), bot)
            elif turn == 9:
                await clan_console_mix_1v1_and_2v2_elo_list(load_clan(DIVISION_SERVER_ID), bot)    
            # Test Clan
            elif turn == 69:
                await clan_console_mix_1v1_elo_list(load_clan(TEST_SERVER_ID), bot)
                prev_turn
            elif turn == 420:
                await server_1v1_and_2v2_and_rotating_elo_list(load_server(TEST_SERVER_ID), bot)
                prev_turn
            # Debugging
            elif turn == 101:
                print("Entered Debugging")
                break
            # Reset Q
            else:
                reset_turn()
                await send_all_legends_elo(CROSSYCHAINSAW_ID, 1165233774305493012, bot)
            next_turn()
        except Exception as e:
            print(e)


@bot.command(name='ping')
async def ping_command(ctx):
    await ping(ctx)


@bot.command(name='spit')
@has_permissions(manage_roles=True, ban_members=True)
async def spit_fire_command(ctx):
    await spit_fire(bot)

@bot.command(name='leave')
@has_permissions(manage_roles=True, ban_members=True)
async def leave_server_command(ctx, server_id):
    await leave_server(bot, ctx, server_id)

@bot.command(name='tc')
@has_permissions(manage_roles=True, ban_members=True)
async def test_clan_console_mix_1v1_elo_list_command(ctx):
    await test_clan_console_mix_1v1_elo_list(bot)

@bot.command(name='ts')
@has_permissions(manage_roles=True, ban_members=True)
async def test_server_1v1_elo_list_command(ctx):
    await test_server_1v1_elo_list(bot)

def run_ranknir():
    bot.run(env_variable("RANKNIR_BOT_TOKEN"))
    # bot.run(env_variable("TEST_BOT_TOKEN"))
    return