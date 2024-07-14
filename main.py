# Imports
import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions
from commands.ping import ping
from modules.choose_file import choose_json_file
from modules.data_management import DATA_KEY_FOR_ACCOUNT_LINKERS, DATA_KEY_FOR_CONSOLE_PLAYERS, load_clan, load_json_file
from modules.elo_list import clan_console_mix_1v1_and_2v2_and_rotating_elo_list, clan_console_mix_1v1_elo_list, clan_console_mix_2v2_elo_list, clan_console_mix_1v1_and_2v2_elo_list
from classes.Clan import Clan

# Discord Stuff
intents = discord.Intents().all()
bot = commands.Bot(command_prefix=['r!', 'R!'], intents=intents)

clan_data = load_json_file(choose_json_file())
YOUR_CLAN = Clan(
    server_name=clan_data['server_name'],
    clan_names=clan_data['clan_names'],
    channel_1v1_id=clan_data['channel_1v1_id'],
    channel_2v2_id=clan_data['channel_2v2_id'],
    id_array=clan_data['id_array'],
    color=int(clan_data['color'], 16),
    image=clan_data['image'],
    server_id=clan_data['discord_server_id'],
    sorting_method=clan_data['sorting_method'],
    show_member_count=clan_data['show_member_count'],
    show_xp=clan_data['show_xp'],
    show_no_elo_players=clan_data['show_no_elo_players'],
    channel_rotating_id=clan_data['channel_rotating_id'],
    account_linkers=clan_data[DATA_KEY_FOR_ACCOUNT_LINKERS],
    console_players=clan_data[DATA_KEY_FOR_CONSOLE_PLAYERS]
)
DISCORD_BOT_TOKEN = clan_data['bot_token']

# Confirmation message that Ranknir is online
@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    while True:
        await clan_console_mix_1v1_and_2v2_elo_list(YOUR_CLAN, bot)

# Run this command to check if Ranknir is running (r!ping)
@bot.command(name='ping')
async def ping_command(ctx):
    await ping(ctx)

bot.run(DISCORD_BOT_TOKEN)
