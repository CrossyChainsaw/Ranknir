import discord
from discord import app_commands
from discord.ext import commands
from Global.Xos import Xos
from Dadabase.modules.claim import claim
from Dadabase.modules.check import check
from Dadabase.modules.ping import ping
from Dadabase.modules.configure_clan import configure_clan
from Dadabase.modules.console.console_add import console_add
from Dadabase.modules.console.console_list import console_list
from Dadabase.modules.console.console_remove import console_remove
from discord.ext.commands import has_permissions
from Dadabase.modules.configure_server import configure_server
from Dadabase.modules.server.server_add_player import server_add_player
from Dadabase.modules.server.server_rm_player import server_rm_player
from Dadabase.modules.account_linkers.al_add import al_add
from Dadabase.modules.account_linkers.al_list import al_list
from Dadabase.modules.account_linkers.al_remove import al_remove
from Ranknir.data.server_data import Brawlhalla_NL, M3OW, Test_Server
from Ranknir.data.clan_data import Pandation, test_clan
os = Xos()

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

server_based_server_ids = [Brawlhalla_NL.id, M3OW.id, Test_Server.id]
clan_based_server_ids = [Pandation.server_id, test_clan.server_id]

all_server_ids = server_based_server_ids.copy()
all_server_ids.extend(clan_based_server_ids)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


@tree.command(name='ping')
async def ping_command(interaction):
    await ping(interaction)


@tree.command(name='claim', description='Link your Brawlhalla account to Discord')
async def claim_command(interaction, brawlhalla_id:int):
    print('Someone called claim!')
    
    # niet netjes broeder
    brawlhalla_hungary_server_id = 1209624739635531857
    member = interaction.user
    role_name1 = "M30W"
    role_name2 = "Verified ✔"
    role_name3 = "M3W"
    print('help')
    print(interaction.guild.id)

    if discord.utils.get(member.roles, name=role_name1) is not None or discord.utils.get(member.roles, name=role_name2) is not None or discord.utils.get(member.roles, name=role_name3) is not None or interaction.guild.id == brawlhalla_hungary_server_id:
        await claim(interaction, brawlhalla_id)
    else:
        await interaction.send(f'{member.name} does not have permission to use this command')


@tree.command(name='check', description='Check your linked Brawlhalla account')
async def check_command(ctx):
    await check(ctx)


@tree.command(name='add_account_linker', description='Specify a player to remove from the leaderboard')
@app_commands.checks.has_permissions(administrator=True)
async def al_add_command(interaction, brawlhalla_id:int, brawlhalla_name:str):
    await al_add(interaction, brawlhalla_id, brawlhalla_name)


@tree.command(name='account_linkers_list', description='List all Account Linkers')
async def al_list_command(interaction):
    await al_list(interaction)


@tree.command(name='remove_account_linker', description='Remove an Account Linker')
@app_commands.checks.has_permissions(administrator=True)
async def al_remove_command(interaction, brawlhalla_id:int):
    await al_remove(interaction, brawlhalla_id)


@tree.command(name='add_server_player', description="(You aren't suposed to run this) Manually add a player to the server leaderboard")
@app_commands.checks.has_permissions(administrator=True)
async def server_add_player_command(ctx, brawlhalla_id:int, discord_id:str, discord_name:str):
    discord_id = int(discord_id)
    await server_add_player(ctx, brawlhalla_id, discord_id, discord_name)

@tree.command(name='remove_server_player', description="(You aren't suposed to run this) Manually removes a player off the server leaderboard")
@app_commands.checks.has_permissions(administrator=True)
async def server_remove_player_command(interaction, brawlhalla_id:int):
    await server_rm_player(interaction, brawlhalla_id)


@tree.command(name='add_console_player', description='Add a console player')
@app_commands.checks.has_permissions(administrator=True)
async def console_add_command(interaction, brawlhalla_id:int, brawlhalla_name:str):
    await console_add(interaction, brawlhalla_id, brawlhalla_name)


@tree.command(name='console_player_list', description='List all console players')
async def console_list_command(interaction):
    await console_list(interaction)


@tree.command(name='remove_console_player', description='Remove a console player')
@app_commands.checks.has_permissions(administrator=True)
async def console_remove_command(interaction, brawlhalla_id:int):
    await console_remove(interaction, brawlhalla_id)


@tree.command(name='configure_clan', description="(You aren't suposed to run this) Generate a file with clan data for the current clan server")
@app_commands.checks.has_permissions(administrator=True)
async def configure_clan_command(interaction):
    await configure_clan(interaction)


@tree.command(name='configure_server', description="(You aren't suposed to run this) Generate a file with clan data for the current server")
@app_commands.checks.has_permissions(administrator=True)
async def configure_server_command(interaction):
    await configure_server(interaction)


# sync everything up
@client.event
async def on_ready():
    await tree.sync()
    print("Bot is ready!")

def run_dadabase():
    # client.run(os.environ[3])
    client.run(os.environ[2]) # Testing
