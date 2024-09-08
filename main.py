import asyncio
import discord
from discord.ext import commands, tasks
from discord.ext.commands import has_permissions, MissingPermissions, Context
from Ranknir.modules.data_management import ServerIDs, load_clan_v2, load_server_v2
from Ranknir.commands.ping import ping
from Ranknir.commands.spit_fire import spit_fire
from Ranknir.modules.elo_list import clan_console_mix_1v1_elo_list, clan_console_mix_1v1_and_2v2_elo_list, clan_console_mix_1v1_and_2v2_and_rotating_elo_list, server_1v1_and_2v2_and_rotating_elo_list, server_1v1_and_2v2_elo_list
# from Ranknir.data.clan_data import test_clan, Pandation, Tews, Frost, KryptX, Empire_United, Grant, aura
from Ranknir.modules.data_management import PlayerIDs
from Ranknir.modules.turn import next_turn, get_turn, reset_turn, prev_turn
from Ranknir.modules.all_legends_elo import send_all_legends_elo
from Ranknir.modules.get_current_order import print_current_order
from Ranknir.commands.test_clan import test_clan_console_mix_1v1_elo_list
from Ranknir.commands.test_server import test_server
from Ranknir.modules.env import env_variable
import json

intents = discord.Intents().all()
bot = commands.Bot(command_prefix=['r!', 'R!'], intents=intents)


@tasks.loop(hours=48)
async def leaderboards_loop():
    try:
        # get turn
        print('getting turn...')
        turn = get_turn()
        print("current turn: " + str(turn))

        # Clans / Servers
        if turn == 0:
            await clan_console_mix_1v1_and_2v2_and_rotating_elo_list(await load_clan_v2(ServerIDs.PANDATION), bot)
        elif turn == 1:
            await clan_console_mix_1v1_and_2v2_elo_list(await load_clan_v2(ServerIDs.VCNTY), bot)
        elif turn == 2:
            await clan_console_mix_1v1_and_2v2_elo_list(await load_clan_v2(ServerIDs.FROST), bot)
        elif turn == 3:
            await server_1v1_and_2v2_and_rotating_elo_list(await load_server_v2(ServerIDs.M30W), bot)
        elif turn == 4:
            await clan_console_mix_1v1_and_2v2_and_rotating_elo_list(await load_clan_v2(ServerIDs.TEWS), bot)
        elif turn == 5:
            await clan_console_mix_1v1_elo_list(await load_clan_v2(ServerIDs.EMPIRE_UNITED), bot)
        elif turn == 6:
            await server_1v1_and_2v2_and_rotating_elo_list(await load_server_v2(ServerIDs.BHNL), bot)
        elif turn == 7:
            await clan_console_mix_1v1_and_2v2_elo_list(await load_clan_v2(ServerIDs.GRANT), bot)
        elif turn == 8:        
            await server_1v1_and_2v2_elo_list(await load_server_v2(ServerIDs.BRAWL_HUNGARY), bot)
        elif turn == 9:
            await clan_console_mix_1v1_and_2v2_elo_list(await load_clan_v2(ServerIDs.DIVISION_9), bot)    
        elif turn == 10:
            await clan_console_mix_1v1_and_2v2_elo_list(await load_clan_v2(ServerIDs.AURA), bot)    
        # Test Clan
        elif turn == 69:
            await clan_console_mix_1v1_elo_list(await load_clan_v2(ServerIDs.TEST_SERVER), bot)
            prev_turn
        elif turn == 420:
            await server_1v1_and_2v2_and_rotating_elo_list(await load_server_v2(ServerIDs.TEST_SERVER), bot)
            prev_turn
        # Debugging
        elif turn == 101:
            print("Debugging doesn't work anymore")
        # Reset Q
        else:
            reset_turn()
            await send_all_legends_elo(PlayerIDs.CROSSYCHAINSAW, 1165233774305493012, bot)
        next_turn()
    except Exception as e:
        print(e)
        await asyncio.sleep(3)
                
@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    leaderboards_loop.start()


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
    await clan_console_mix_1v1_elo_list(await load_clan_v2(ServerIDs.TEST_SERVER), bot)

@bot.command(name='ts2')
@has_permissions(manage_roles=True, ban_members=True)
async def test_server_1v1_and_2v2_and_rotating_elo_list_command(ctx):
    await server_1v1_and_2v2_and_rotating_elo_list(await load_server_v2(ServerIDs.M30W), bot)

def run_ranknir():
    bot.run(env_variable("RANKNIR_BOT_TOKEN"))
    #bot.run(env_variable("RANKNIR_TESTING_BOT_TOKEN"))
    return