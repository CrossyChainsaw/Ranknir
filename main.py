import asyncio
import discord
from discord.ext import commands, tasks
from discord.ext.commands import has_permissions, MissingPermissions, Context
from Ranknir.modules.data_management import ServerIDs, load_clan, load_server
from Ranknir.commands.ping import ping
from Ranknir.commands.spit_fire import spit_fire
from Ranknir.modules.elo_list import clan_console_mix_1v1_elo_list, clan_console_mix_1v1_and_2v2_elo_list, clan_console_mix_1v1_and_2v2_and_rotating_elo_list, server_1v1_and_2v2_and_rotating_elo_list, server_1v1_and_2v2_elo_list
# from Ranknir.data.clan_data import test_clan, Pandation, Tews, Frost, KryptX, Empire_United, Grant, aura
from Ranknir.modules.data_management import PlayerIDs
from Ranknir.modules.turn import next_turn, get_turn, reset_turn, prev_turn
from Ranknir.modules.all_legends_elo import send_all_legends_elo
from Ranknir.modules.get_current_order import print_current_order
from Ranknir.commands._test_clan import test_clan_console_mix_1v1_elo_list
from Ranknir.commands._test_server import test_server
from Ranknir.modules.env import env_variable
import json
import logging
from Ranknir.modules.env import env_variable

RANKNIR_ACTIVE = env_variable("RANKNIR_ACTIVE")
RANKNIR_TESTING = env_variable("RANKNIR_TESTING")

logging.basicConfig(level=logging.INFO)
intents = discord.Intents().all()
bot = commands.Bot(command_prefix=['r!', 'R!'], intents=intents)


@tasks.loop(seconds=30)
async def leaderboards_loop():
    try:
        # get turn
        turn = get_turn()
        print("current turn: " + str(turn))

        # Clans / Servers
        if turn == 0:
            await clan_console_mix_1v1_and_2v2_and_rotating_elo_list(await load_clan(ServerIDs.PANDATION), bot)
        elif turn == 1:
            await server_1v1_and_2v2_and_rotating_elo_list(await load_server(ServerIDs.LEGION), bot)
        elif turn == 2:
            await clan_console_mix_1v1_and_2v2_elo_list(await load_clan(ServerIDs.FROST), bot)
        elif turn == 3:
            await clan_console_mix_1v1_and_2v2_elo_list(await load_clan(ServerIDs.IMPERIO_ANONIMO), bot)
        elif turn == 4:
            await clan_console_mix_1v1_and_2v2_and_rotating_elo_list(await load_clan(ServerIDs.TEWS), bot)
        elif turn == 5:
            await clan_console_mix_1v1_and_2v2_elo_list(await load_clan(ServerIDs.CLIENT), bot)
        elif turn == 6:
            await server_1v1_and_2v2_and_rotating_elo_list(await load_server(ServerIDs.BHNL), bot)
        elif turn == 7:        
            await server_1v1_and_2v2_elo_list(await load_server(ServerIDs.BRAWL_HUNGARY), bot)
        elif turn == 8:
            await clan_console_mix_1v1_and_2v2_elo_list(await load_clan(ServerIDs.DIVISION_9), bot)    
        elif turn == 9:
            await clan_console_mix_1v1_and_2v2_elo_list(await load_clan(ServerIDs.AURA), bot)  
        elif turn == 10:
            await clan_console_mix_1v1_and_2v2_elo_list(await load_clan(ServerIDs.EISEN), bot) 
        elif turn == 11:
            await clan_console_mix_1v1_and_2v2_elo_list(await load_clan(ServerIDs.HAMM3R), bot) 
        # Test Clan
        elif turn == 69:
            await clan_console_mix_1v1_elo_list(await load_clan(ServerIDs.TEST_SERVER), bot, x=1)
            prev_turn
        elif turn == 420:
            await server_1v1_and_2v2_and_rotating_elo_list(await load_server(ServerIDs.TEST_SERVER), bot)
            prev_turn
        # Debugging
        elif turn == 101:
            print("Entered Debugging")
            prev_turn()
            leaderboards_loop.stop()
        # Reset Q
        else:
            reset_turn()
            await send_all_legends_elo(PlayerIDs.CROSSYCHAINSAW, 1165233774305493012, bot)
        next_turn()
    except Exception as e:
        print(e)
        next_turn()
        await asyncio.sleep(3)

#  ┌───────────────────┐
#  │       EVENTS      │
#  └───────────────────┘

@bot.event
async def on_ready():
    print(f"Bot reconnected as {bot.user}")
    if not leaderboards_loop.is_running():
        leaderboards_loop.start()

@bot.event
async def on_disconnect():
    print("Bot disconnected. Attempting to reconnect...")

@bot.event
async def on_resumed():
    print("Bot reconnected successfully!")
    if not leaderboards_loop.is_running():
        leaderboards_loop.start()

#  ┌───────────────────┐
#  │      COMMANDS     │
#  └───────────────────┘

@bot.command(name='ping')
async def ping_command(ctx):
    await ping(ctx)

@bot.command(name='spit')
@has_permissions(manage_roles=True, ban_members=True)
async def spit_fire_command(ctx, server_id):
    await spit_fire(bot, ctx, server_id)

@bot.command(name='tc')
@has_permissions(manage_roles=True, ban_members=True)
async def test_clan_command(ctx):
    await test_clan_console_mix_1v1_elo_list(bot)

@bot.command(name='ts')
@has_permissions(manage_roles=True, ban_members=True)
async def test_server_command(ctx):
    await test_server(bot)

@bot.command(name='tc2')
@has_permissions(manage_roles=True, ban_members=True)
async def test_clan_console_mix_1v1_elo_list_command(ctx):
    await clan_console_mix_1v1_and_2v2_and_rotating_elo_list(await load_clan(ServerIDs.TEST_SERVER), bot, x=1)

@bot.command(name='ts2')
@has_permissions(manage_roles=True, ban_members=True)
async def test_server_1v1_and_2v2_and_rotating_elo_list_command(ctx):
    await server_1v1_and_2v2_elo_list(await load_server(ServerIDs.TEST_SERVER), bot, x=2)

def run_ranknir():
    if RANKNIR_ACTIVE:
        bot.run(env_variable("RANKNIR_BOT_TOKEN"))
    if RANKNIR_TESTING:
        bot.run(env_variable("RANKNIR_TESTING_BOT_TOKEN"))