import discord
from discord.ext import commands
from Global.Xos import Xos
from Dadabase.modules.claim import claim
from Dadabase.modules.check import check
from Dadabase.modules.ping import ping
from Dadabase.modules.keep_alive import keep_alive
from Dadabase.modules.configure_clan import configure_clan
from Dadabase.modules.ps4.ps4_add import ps4_add
from Dadabase.modules.ps4.ps4_list import ps4_list
from Dadabase.modules.ps4.ps4_remove import ps4_remove
from discord.ext.commands import has_permissions
from Dadabase.modules.configure_server import configure_server
from Dadabase.modules.frost_commands.create_player import create_player
from Dadabase.modules.frost_commands.legend_list import legend_list
from Dadabase.modules.frost_commands.legend_help import legend_help
from Dadabase.modules.server.server_add_player import server_add_player
os = Xos()

intents = discord.Intents().all()
bot = commands.Bot(command_prefix=['d!'], intents=intents)


@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')


@bot.command(name='ping')
async def say(ctx):
    await ping(ctx)


@bot.command(name='claim')
async def claim_command(ctx, brawlhalla_id):
    print('Someone called claim')
    
    member = ctx.author
    role_name1 = "M30W"
    role_name2 = "Verified ✔"
    role_name2 = "M3W"
    
    if discord.utils.get(member.roles, name=role_name1) is not None or discord.utils.get(member.roles, name=role_name2) is not None or discord.utils.get(member.roles, name=role_name3) is not None:
        await claim(ctx, brawlhalla_id)
    else:
        await ctx.send(f'{member.name} does not have permission to use this command')


@claim_command.error
async def claim_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('format your message like the following\n`'+bot.command_prefix[0]+'claim brawlhalla_id`')


# @commands.has_role("Verified ✔")
@bot.command(name='check')
async def check_command(ctx):
    await check(ctx)


@has_permissions(administrator=True)
@bot.command(name='ps4add')
async def ps4_add_command(ctx, brawlhalla_id, brawlhalla_name):
    await ps4_add(ctx, brawlhalla_id, brawlhalla_name)


@has_permissions(administrator=True)
@bot.command(name='serveraddplayer', aliases=['sadplayer', 'sap'])
async def server_add_player_command(ctx, brawlhalla_id, discord_id, discord_name):
    await server_add_player(ctx, brawlhalla_id, discord_id, discord_name)

# @has_permissions(administrator=True)


@bot.command(name='ps4list', aliases=['ps4ls', 'psls'])
async def ps4_list_command(ctx):
    await ps4_list(ctx)


@has_permissions(administrator=True)
@bot.command(name='ps4remove', aliases=['ps4rm'])
async def ps4_remove_command(ctx, brawlhalla_id):
    await ps4_remove(ctx, brawlhalla_id)


@has_permissions(administrator=True)
@bot.command(name='configureclan', aliases=['configclan'])
async def configure_clan_command(ctx):
    await configure_clan(ctx)


@has_permissions(administrator=True)
@bot.command(name='configureserver', aliases=['configserver'])
async def configure_server_command(ctx):
    await configure_server(ctx)


@commands.has_role("Special Snowflakes")
@bot.command(name='createplayer', aliases=['cp'])
async def create_player_command(ctx, brawlhalla_id_list, nickname):
    await create_player(ctx, brawlhalla_id_list, nickname)


@commands.has_role("Special Snowflakes")
@bot.command(name='legendlist', aliases=['lls'])
async def legend_list_command(ctx, legend_id):
    await legend_list(ctx, legend_id)


@bot.command(name='legendhelp', aliases=['lhelp'])
async def legend_help_command(ctx):
    await legend_help(ctx)

# keep_alive()


def run_dadabase():
    bot.run(os.environ[3])
