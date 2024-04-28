## hey i was refactoring dadabase to be structured like queen spy folderwise
## and cleaning functions cleaning modules making them more independant

import discord
from discord import app_commands
from Dadabase.commands.claim import claim
from Dadabase.commands.check import check
from Dadabase.commands.ping import ping
from Dadabase.commands.configure_clan import configure_clan
from Dadabase.commands.add_console_player import add_console_player
from Dadabase.commands.console_player_list import console_player_list
from Dadabase.commands.remove_console_player import remove_console_player
from Dadabase.commands.configure_server import configure_server
from Dadabase.commands.add_server_player import add_server_player
from Dadabase.commands.remove_server_player import remove_server_player
from Dadabase.commands.add_account_linker import add_account_linker
from Dadabase.commands.account_linker_list import account_linker_list
from Dadabase.commands.remove_account_linker import remove_account_linker
from Dadabase.modules.data_management import BENELUX_COUNTRIES, ALL_COUNTRIES, BRAWL_SERVERS, SORTING_METHOD_OPTIONS, SHOW_OR_HIDE
from Dadabase.modules.env import env_variable
from Dadabase.modules.check_permission import has_permission
from Dadabase.commands.server_player_list import server_player_list
from Dadabase.commands.edit_clan import edit_clan


intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


@tree.command(name='account_linker_list', description='List all Account Linkers')
async def account_linker_list_command(interaction):
    await account_linker_list(interaction)


@tree.command(name='add_account_linker', description='Specify a player to remove from the leaderboard')
@app_commands.checks.has_permissions(administrator=True)
async def add_account_linker_command(interaction, brawlhalla_id:int, brawlhalla_name:str):
    await add_account_linker(interaction, brawlhalla_id, brawlhalla_name)


@tree.command(name='add_console_player', description='Add a console player')
@app_commands.checks.has_permissions(administrator=True)
async def add_console_player_command(interaction, brawlhalla_id:int, brawlhalla_name:str):
    await add_console_player(interaction, brawlhalla_id, brawlhalla_name)


@tree.command(name='add_server_player', description="(You aren't suposed to run this) Manually add a player to the server leaderboard")
@app_commands.checks.has_permissions(administrator=True)
@app_commands.describe(region="What server do you play on?")
@app_commands.choices(region=BRAWL_SERVERS)
@app_commands.describe(country_of_residence="Which country does the player live in?")
@app_commands.choices(country_of_residence=ALL_COUNTRIES)
@app_commands.describe(ethnicity="Which country does the player live in?")
@app_commands.choices(ethnicity=ALL_COUNTRIES)
async def add_server_player_command(interaction: discord.Interaction, brawlhalla_id:int, discord_id:str, discord_name:str, region: app_commands.Choice[str]="", country_of_residence: app_commands.Choice[str]="", ethnicity: app_commands.Choice[str]=""):
    discord_id = int(discord_id)
    await add_server_player(interaction, brawlhalla_id, discord_id, discord_name, region, country_of_residence, ethnicity)


@tree.command(name='check', description='Check your linked Brawlhalla account')
async def check_command(interaction):
    await check(interaction)


@tree.command(name='claim', description='Link your Brawlhalla account to Discord')
@app_commands.describe(region="What server do you play on?")
@app_commands.choices(region=BRAWL_SERVERS)
@app_commands.describe(country_of_residence="Which country do you live in?")
@app_commands.choices(country_of_residence=ALL_COUNTRIES)
@app_commands.describe(ethnicity="What is your ethnicity?")
@app_commands.choices(ethnicity=ALL_COUNTRIES)
async def claim_command(interaction, brawlhalla_id:int, 
                        region: app_commands.Choice[str],
                        country_of_residence: app_commands.Choice[str], 
                        ethnicity: app_commands.Choice[str]):
    print(f'{interaction.user.name} called claim!')
    if has_permission(interaction):
        await claim(interaction, brawlhalla_id, region.value, country_of_residence.value, ethnicity.value)
    else:
        await interaction.response.send_message(f'{interaction.user.name} does not have permission to use this command')


@tree.command(name='configure_clan', description="(You aren't suposed to run this) Generate a file with clan data for the current clan server")
@app_commands.checks.has_permissions(administrator=True)
@app_commands.describe(sorting_method="What elo should be prioritised?")
@app_commands.choices(sorting_method=SORTING_METHOD_OPTIONS)
@app_commands.describe(member_count="Show or Hide the amount of players in the leaderboard?")
@app_commands.describe(no_elo_players="Show or Hide the amount of players in the leaderboard?")
@app_commands.describe(xp="Show or Hide the amount of clan xp?")
async def configure_clan_command(interaction, clan_names:str, channel_1v1_id:str, channel_2v2_id:str, clan_id:str, color:str,
                                 sorting_method: app_commands.Choice[str], show_member_count: bool, 
                                 show_no_elo_players: bool, show_xp: bool, channel_rotating_id:str=None, image:str=""):
    
    await configure_clan(interaction, clan_names, channel_1v1_id, channel_2v2_id, clan_id, color, image, 
                         sorting_method.value, show_member_count, show_xp, show_no_elo_players, channel_rotating_id)


@tree.command(name='configure_server', description="(You aren't suposed to run this) Generate a file with clan data for the current server")
@app_commands.checks.has_permissions(administrator=True)
@app_commands.describe(sorting_method="What elo should be prioritised?")
@app_commands.choices(sorting_method=SORTING_METHOD_OPTIONS)
async def configure_server_command(interaction, 
                                   leaderboard_title:str,
                                   sorting_method: app_commands.Choice[str], 
                                   show_member_count: bool,
                                   show_no_elo_players: bool,
                                   channel_1v1_id:str,
                                   channel_2v2_id:str,
                                   channel_rotating_id:str,
                                   color:str="0xFFFFFF",
                                   image:str=""):
    await configure_server(interaction, leaderboard_title, sorting_method.value, show_member_count, show_no_elo_players, channel_1v1_id, channel_2v2_id, channel_rotating_id, color, image)


@tree.command(name='console_player_list', description='List all console players')
async def console_player_list_command(interaction):
    await console_player_list(interaction)


@tree.command(name='edit_clan', description='Edit clan data')
@app_commands.checks.has_permissions(administrator=True)
@app_commands.describe(sorting_method="What elo should be prioritised?")
@app_commands.choices(sorting_method=SORTING_METHOD_OPTIONS)
async def edit_clan_command(interaction, channel_1v1_id:str=None, channel_2v2_id:str=None, color:str=None, image:str=None, sorting_method:str=None, show_member_count:bool=None, show_xp:bool=None, show_no_elo_players:bool=None, channel_rotating_id:str = None, has_account_linkers:bool=None):
    await edit_clan(interaction, channel_1v1_id, channel_2v2_id, color, image, sorting_method, show_member_count, show_xp, show_no_elo_players, channel_rotating_id, has_account_linkers)


@tree.command(name='ping')
async def ping_command(interaction):
    await ping(interaction)


@tree.command(name='remove_account_linker', description='Remove an Account Linker')
@app_commands.checks.has_permissions(administrator=True)
async def remove_account_linker_command(interaction, brawlhalla_id:int):
    await remove_account_linker(interaction, brawlhalla_id)


@tree.command(name='remove_console_player', description='Remove a console player')
@app_commands.checks.has_permissions(administrator=True)
async def remove_console_player_command(interaction, brawlhalla_id:int):
    await remove_console_player(interaction, brawlhalla_id)


@tree.command(name='remove_server_player', description="(You aren't suposed to run this) Manually removes a player off the server leaderboard")
@app_commands.checks.has_permissions(administrator=True)
async def remove_server_player_command(interaction, brawlhalla_id:int):
    await remove_server_player(interaction, brawlhalla_id)

@tree.command(name='server_player_list', description="(List all server players")
@app_commands.checks.has_permissions(administrator=True)
async def server_player_list_command(interaction):
    await server_player_list(interaction)
    

# sync everything up
@client.event
async def on_ready():
    await tree.sync()
    print(f'We have logged in as {client.user}')

def run_dadabase():
    client.run(env_variable("DADABASE_BOT_TOKEN"))
    # client.run(env_variable("TEST_BOT_TOKEN"))
    return