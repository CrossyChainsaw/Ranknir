import asyncio
import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions
from Ranknir.classes.Server import Server
from Ranknir.commands.ping import ping
from Ranknir.commands.spit_fire import spit_fire
from Ranknir.modules.elo_list import clan_console_mix_1v1_elo_list, clan_console_mix_1v1_and_2v2_elo_list, clan_console_mix_1v1_and_2v2_and_rotating_elo_list, server_1v1_and_2v2_and_rotating_elo_list, server_1v1_and_2v2_elo_list
from Ranknir.data.clan_data import test_clan, Pandation, Tews, Frost, KryptX, Empire_United, Grant, aura
from Ranknir.data.server_data import Brawlhalla_NL, M30W, Brawlhalla_Hungary
from Ranknir.data.player_data import CROSSYCHAINSAW_ID
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

def load_json_file(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data


def load_new_server():
    Test_Server_path = "Dadabase/data/servers/705783420189671458.json"
    server_data = load_json_file(Test_Server_path)
    print(server_data)
    Test_Server = Server(server_data['id'],
                        server_data['name'],
                        server_data['leaderboard_title'],
                        server_data['sorting_method'],
                        server_data['member_count'],
                        server_data['no_elo_players'],
                        server_data['channel_1v1_id'],
                        server_data['channel_2v2_id'],
                        server_data['channel_rotating_id'],
                        int(server_data['color'], 16),
                        server_data['image'])
    return Test_Server

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    channel = bot.get_channel(test_clan.channel_1v1_id)
    await channel.send("I'm back online!")

    # new
    Test_Server = load_new_server()

    while True:
        try:
            # get turn
            print('getting turn...')
            turn = get_turn()
            print("current turn: " + str(turn))

            # print order
            order = [Pandation, Tews, Frost, Brawlhalla_NL, Empire_United, KryptX, M30W, Grant, aura, Brawlhalla_Hungary]
            print_current_order(order, turn)

            # Clans / Servers
            if turn == 0:
                await clan_console_mix_1v1_and_2v2_and_rotating_elo_list(Pandation, bot)
            elif turn == 1:
                await clan_console_mix_1v1_and_2v2_and_rotating_elo_list(Tews, bot)
            elif turn == 2:
                await clan_console_mix_1v1_and_2v2_elo_list(Frost, bot)
            elif turn == 3:
                await server_1v1_and_2v2_and_rotating_elo_list(Brawlhalla_NL, bot)
            elif turn == 4:
                await clan_console_mix_1v1_elo_list(Empire_United, bot)
            elif turn == 5:
                await clan_console_mix_1v1_and_2v2_and_rotating_elo_list(KryptX, bot)
            elif turn == 6:
                await server_1v1_and_2v2_and_rotating_elo_list(M30W, bot)
            elif turn == 7:
                await clan_console_mix_1v1_and_2v2_elo_list(Grant, bot)
            elif turn == 8:
                await clan_console_mix_1v1_and_2v2_elo_list(aura, bot)            
            elif turn == 9:
                await server_1v1_and_2v2_elo_list(Brawlhalla_Hungary, bot)
            # Test Clan
            elif turn == 69:
                await clan_console_mix_1v1_elo_list(test_clan, bot)
                prev_turn
            elif turn == 420:
                await server_1v1_and_2v2_and_rotating_elo_list(Test_Server, bot)
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

@bot.command(name='testclan1')
@has_permissions(manage_roles=True, ban_members=True)
async def test_clan_console_mix_1v1_elo_list_command(ctx):
    await test_clan_console_mix_1v1_elo_list(bot)

@bot.command(name='testserver1')
@has_permissions(manage_roles=True, ban_members=True)
async def test_server_1v1_elo_list_command(ctx):
    await test_server_1v1_elo_list(bot)

def run_ranknir():
    # bot.run(env_variable("RANKNIR_BOT_TOKEN"))
    bot.run(env_variable("TEST_BOT_TOKEN"))
    return