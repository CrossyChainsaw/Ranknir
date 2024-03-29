import discord
from Global.Xos import Xos
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions
from Ranknir.modules.keep_alive import keep_alive
from Ranknir.modules.ping import ping
from Ranknir.modules.spit_fire import spit_fire
from Ranknir.modules.elo_list import clan_console_mix_1v1_elo_list, clan_console_mix_1v1_and_2v2_elo_list, clan_console_mix_1v1_and_2v2_and_rotating_elo_list, server_1v1_and_2v2_and_rotating_elo_list
from Ranknir.data.clan_data import test_clan, Pandation, Excalibur, Tews, Frost, KryptX, Empire_United, Grant
from Ranknir.data.server_data import Brawlhalla_NL, Test_Server, M3OW
from Ranknir.data.player_data import CROSSYCHAINSAW_ID, SHAW_ID, DISCARDS_ID
from Ranknir.modules.turn import next_turn, get_turn, reset_turn, prev_turn
from Ranknir.modules.all_legends_elo import send_all_legends_elo
from Ranknir.modules.leave_server import leave_server
os = Xos()

intents = discord.Intents().all()
bot = commands.Bot(command_prefix=['r!', 'R!'], intents=intents)


@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    channel = bot.get_channel(test_clan.channel_1v1_id)
    await channel.send("I'm back online!")

    while True:
        try:
            print('getting turn...')
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
                await clan_console_mix_1v1_elo_list(Empire_United, bot)
            elif turn == 6:
                await clan_console_mix_1v1_and_2v2_elo_list(KryptX, bot)
            elif turn == 7:
                await server_1v1_and_2v2_and_rotating_elo_list(M3OW, bot)
            elif turn == 8:
                await clan_console_mix_1v1_and_2v2_elo_list(Grant, bot)
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
                await send_all_legends_elo(SHAW_ID, 1166526510526631998, bot)
                await send_all_legends_elo(DISCARDS_ID, 1173667369160298506, bot)
            next_turn()
        except Exception as e:
            print(e)


@bot.command(name='ping')
async def command_ping(ctx):
    await ping(ctx)


# @bot.command(name='spit')
# @has_permissions(manage_roles=True, ban_members=True)
@bot.command(name='spit')
async def command_spit_fire(ctx):
    await spit_fire(bot)


@bot.command(name='leave')
async def leave_server_command(ctx, server_id):
    await leave_server(bot, ctx, server_id)

# keep_alive()


def run_ranknir():
    bot.run(os.environ[1])
