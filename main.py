import discord
from discord.ext import commands
from modules.keep_alive import keep_alive
from modules.ping import ping
from modules.elo_list import clan_console_mix_1v1_elo_list, server_1v1_elo_list, clan_console_mix_2v2_elo_list, server_2v2_elo_list, clan_console_mix_1v1_and_2v2_elo_list, server_1v1_and_2v2_elo_list
from classes.Xos import Xos
from data.clan_data import test_clan, Obsessive, Pandation, Excalibur, Tews, Frost, sword
from data.server_data import Brawlhalla_NL, Test_Server
from modules.turn import next_turn, get_turn, reset_turn

os = Xos()

intents = discord.Intents().all()
bot = commands.Bot(command_prefix=['!r', '!R'], intents=intents)


@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

    while True:
        turn = get_turn()
        print("current turn: " + str(turn))

        if turn == 1:
            await clan_console_mix_1v1_and_2v2_elo_list(Pandation, bot)
        elif turn == 2:
            await clan_console_mix_1v1_and_2v2_elo_list(Excalibur, bot)
        elif turn == 3:
            await clan_console_mix_1v1_and_2v2_elo_list(Tews, bot)
        elif turn == 4:
            await clan_console_mix_1v1_and_2v2_elo_list(Obsessive, bot)
        elif turn == 5:
            await clan_console_mix_1v1_and_2v2_elo_list(Frost, bot)
        elif turn == 6:
            await clan_console_mix_1v1_elo_list(sword, bot)
        elif turn >= 7:
            await server_1v1_and_2v2_elo_list(Brawlhalla_NL, bot)
            reset_turn()
        # next_turn()


@bot.command(name='ping')
async def command_ping(ctx):
    await ping(ctx)


# keep_alive()
bot.run(os.environ[2])

# todo, look github issues
