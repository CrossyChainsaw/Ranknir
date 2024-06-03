# Imports
import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions
from commands.ping import ping
from modules.elo_list import clan_console_mix_1v1_elo_list, clan_console_mix_2v2_elo_list, clan_console_mix_1v1_and_2v2_elo_list
from classes.Clan import Clan

# Discord Stuff
intents = discord.Intents().all()
bot = commands.Bot(command_prefix=['r!', 'R!'], intents=intents)

# Fill in with your own clan data!
discord_server_name = "YOUR_DISCORD_SERVER_NAME"
discord_server_id = 'YOUR_DISCORD_SERVER_ID' # Yes this has to be a string
clan_name = ["YOUR_CLAN_NAME"]
channel_1v1_id=0 # Replace with your 1v1 elo channel id
channel_2v2_id=0 # Replace with your 2v2 elo channel id
clan_id = ["YOUR_CLAN_ID"]
clan_image = 'YOUR_CLAN_IMAGE_SOURCE_LINK'
discord_bot_token = "YOUR_BOT_TOKEN" # DON'T SHARE THIS TOKEN WITH ANYONE!!!!!!!!!!!!!!!!!!!!!!

# Create clan object with your clan data
YOUR_CLAN = Clan(server_name=discord_server_name,
                 clan_names=clan_name,
                 channel_1v1_id=channel_1v1_id,
                 channel_2v2_id=channel_2v2_id,
                 id_array=clan_id,
                 color=0xFFFFFF, # You can edit this for custom color (Make sure it stays HEX. Example: 0x123456)
                 image=clan_image,
                 server_id=discord_server_id,
                 sorting_method='current', # current / peak
                 show_member_count=True, # True / False
                 show_xp=False # True / False
                 )

# Confirmation message that Ranknir is online
@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

# Run this command to check if Ranknir is running (r!ping)
@bot.command(name='ping')
async def ping_command(ctx):
    await ping(ctx)

# Run this command for 1v1 leaderboard (r!1)
@bot.command(name='1')
@has_permissions(manage_roles=True, ban_members=True)
async def clan_console_mix_1v1_elo_list_command(ctx):
    await clan_console_mix_1v1_elo_list(YOUR_CLAN, bot)

# Run this command for 2v2 leaderboard (r!2)
@bot.command(name='2')
@has_permissions(manage_roles=True, ban_members=True)
async def clan_console_mix_2v2_elo_list_command(ctx):
    await clan_console_mix_2v2_elo_list(YOUR_CLAN, bot)

# Run this command for both 1v1 and 2v2 leaderboard (r!12)
@bot.command(name='12')
@has_permissions(manage_roles=True, ban_members=True)
async def clan_console_mix_1v1_and_2v2_elo_list_command(ctx):
    await clan_console_mix_1v1_and_2v2_elo_list(YOUR_CLAN, bot)

bot.run(discord_bot_token)