import discord
from discord.ext import commands
from modules.keep_alive import keep_alive
from modules.ping import ping
from modules.elo_list import clan_console_mix_1v1_elo_list, server_1v1_elo_list, clan_console_mix_2v2_elo_list, server_2v2_elo_list, clan_console_mix_1v1_and_2v2_elo_list, server_1v1_and_2v2_elo_list
from classes.Xos import Xos
from data.clan_data import test_clan, Obsessive
from data.server_data import Brawlhalla_NL, Test_Server

intents = discord.Intents().all()
bot = commands.Bot(command_prefix=['!r', '!R'], intents=intents)


@bot.event
async def on_ready():
    # I'm back online!
    print(f'We have logged in as {bot.user}')
    await server_1v1_and_2v2_elo_list(Brawlhalla_NL, bot)
    # await clan_console_mix_1v1_and_2v2_elo_list(Obsessive, bot)
    # await server_2v2_elo_list(Brawlhalla_NL, bot)
    # await clan_console_mix_2v2_elo_list(test_clan, bot) # i hope this works
    # await server_1v1_elo_list(Brawlhalla_NL, bot)
    # await clan_console_mix_1v1_elo_list(test_clan, bot)


@bot.command(name='ping')
async def command_ping(ctx):
    await ping(ctx)


# keep_alive()
bot.run(Xos().environ[1])
