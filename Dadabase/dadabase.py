## hey i was refactoring dadabase to be structured like queen spy folderwise
## and cleaning functions cleaning modules making them more independant

import discord
from discord import app_commands
from Dadabase.commands.claim import claim
from Dadabase.commands.check import check
from Dadabase.commands.ping import ping
from Dadabase.commands.initialise_clan import initialise_clan
from Dadabase.commands.add_console_player import add_console_player
from Dadabase.commands.console_player_list import console_player_list
from Dadabase.commands.remove_console_player import remove_console_player
from Dadabase.commands.initialise_server import initialise_server
from Dadabase.commands.add_server_player import add_server_player
from Dadabase.commands.remove_server_player import remove_server_player
from Dadabase.commands.add_account_linker import add_account_linker
from Dadabase.commands.account_linker_list import account_linker_list
from Dadabase.commands.remove_account_linker import remove_account_linker
from Dadabase.modules.command import ALL_COUNTRIES, BRAWL_SERVERS, CHECK_COMMAND, CLAIM_COMMAND, INITIALISE_CLAN_COMMAND, INITIALISE_SERVER_COMMAND, CONSOLE_PLAYER_LIST, FLAG_TYPE_OPTIONS, REMOVE_ACCOUNT_LINKER_COMMAND, SERVER_PLAYER_LIST, SORTING_METHOD_OPTIONS, ACCOUNT_LINKER_LIST_COMMAND, ADD_ACCOUNT_LINKER_COMMAND, PING_COMMAND, EDIT_CLAN_COMMAND, ADD_SERVER_PLAYER_COMMAND, EDIT_SERVER_COMMAND, ADD_CONSOLE_PLAYER_COMMAND, REMOVE_SERVER_PLAYER_COMMAND, REMOVE_CONSOLE_PLAYER_COMMAND
from Dadabase.modules.env import env_variable
from Dadabase.modules.check_permission import has_permission
from Dadabase.commands.server_player_list import server_player_list
from Dadabase.commands.edit_clan import edit_clan
from Dadabase.commands.edit_server import edit_server
from Dadabase.modules.data_management import FlagType


intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


@tree.command(name=ACCOUNT_LINKER_LIST_COMMAND[1:], description='List all Account Linkers')
async def account_linker_list_command(interaction):
    await account_linker_list(interaction)


@tree.command(name=ADD_ACCOUNT_LINKER_COMMAND[1:], description='Specify a player to remove from the leaderboard')
@app_commands.checks.has_permissions(administrator=True)
async def add_account_linker_command(interaction, brawlhalla_id:int, brawlhalla_name:str):
    await add_account_linker(interaction, brawlhalla_id, brawlhalla_name)


@tree.command(name=ADD_CONSOLE_PLAYER_COMMAND[1:], description='Add a console player')
@app_commands.checks.has_permissions(administrator=True)
async def add_console_player_command(interaction, brawlhalla_id:int, brawlhalla_name:str):
    await add_console_player(interaction, brawlhalla_id, brawlhalla_name)


@tree.command(name=ADD_SERVER_PLAYER_COMMAND[1:], description="(You aren't suposed to run this) Manually add a player to the server leaderboard")
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


@tree.command(name=CHECK_COMMAND[1:], description='Check your linked Brawlhalla account')
async def check_command(interaction):
    await check(interaction)


@tree.command(name=CLAIM_COMMAND[1:], description='Link your Brawlhalla account to Discord')
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




@tree.command(name=CONSOLE_PLAYER_LIST[1:], description='List all console players')
async def console_player_list_command(interaction):
    await console_player_list(interaction)


@tree.command(name=EDIT_CLAN_COMMAND[1:], description='Edit clan data')
@app_commands.checks.has_permissions(administrator=True)
@app_commands.describe(sorting_method="What elo should be prioritised?")
@app_commands.choices(sorting_method=SORTING_METHOD_OPTIONS)
async def edit_clan_command(interaction, channel_1v1_id:str=None, channel_2v2_id:str=None, color:str=None, image:str=None, sorting_method:str=None, show_member_count:bool=None, show_xp:bool=None, show_no_elo_players:bool=None, channel_rotating_id:str = None):
    await edit_clan(interaction, channel_1v1_id, channel_2v2_id, color, image, sorting_method, show_member_count, show_xp, show_no_elo_players, channel_rotating_id)


@tree.command(name=EDIT_SERVER_COMMAND[1:], description='Edit server data')
@app_commands.checks.has_permissions(administrator=True)
@app_commands.describe(sorting_method="What elo should be prioritised?")
@app_commands.choices(sorting_method=SORTING_METHOD_OPTIONS)
@app_commands.describe(flag_type="What flag should be shown next to each player?")
@app_commands.choices(flag_type=FLAG_TYPE_OPTIONS)
async def edit_server_command(interaction, 
                              leaderboard_title:str=None, 
                              sorting_method:app_commands.Choice[str]=None, 
                              show_member_count:bool=None, 
                              show_no_elo_players:bool=None, 
                              channel_1v1_id:str=None, 
                              channel_2v2_id:str=None, 
                              channel_rotating_id:str = None, 
                              image:str=None, 
                              color:str=None, 
                              flag_type:app_commands.Choice[str]=None):
    await edit_server(interaction, leaderboard_title, sorting_method, show_member_count, show_no_elo_players, channel_1v1_id, channel_2v2_id, channel_rotating_id, image, color, flag_type)


@tree.command(name=INITIALISE_CLAN_COMMAND[1:], description="(You aren't suposed to run this) Generate a file with clan data for the current clan server")
@app_commands.checks.has_permissions(administrator=True)
@app_commands.describe(sorting_method="What elo should be prioritised?")
@app_commands.choices(sorting_method=SORTING_METHOD_OPTIONS)
@app_commands.describe(color = "Provide a Hex color code")
# @app_commands.describe(member_count="Show or Hide the amount of players in the leaderboard?")
# @app_commands.describe(show_no_elo_players="Show or Hide the amount of players in the leaderboard?")
# @app_commands.describe(show_xp="Show or Hide the amount of clan xp?")
async def initialise_clan_command(interaction, 
                                  clan_names:str, 
                                  channel_1v1_id:str, 
                                  channel_2v2_id:str, 
                                  clan_id:str, 
                                  color:str,
                                  sorting_method: app_commands.Choice[str], 
                                  show_member_count: bool, 
                                  show_no_elo_players: bool, 
                                  show_xp: bool, 
                                  channel_rotating_id:str=None, 
                                  image:str="", 
                                  server_id:str=None, 
                                  server_name:str=None):
    await initialise_clan(interaction, clan_names, channel_1v1_id, channel_2v2_id, clan_id, color, image, 
                         sorting_method.value, show_member_count, show_xp, show_no_elo_players, channel_rotating_id, server_id, server_name)


@tree.command(name=INITIALISE_SERVER_COMMAND[1:], description="(You aren't suposed to run this) Generate a file with clan data for the current server")
@app_commands.checks.has_permissions(administrator=True)
@app_commands.describe(sorting_method="What elo should be prioritised?")
@app_commands.choices(sorting_method=SORTING_METHOD_OPTIONS)
@app_commands.describe(flag_type="What flag should be shown next to each player?")
@app_commands.choices(flag_type=FLAG_TYPE_OPTIONS)
@app_commands.describe(color = "Provide a Hex color code")
async def initialise_server_command(interaction, 
                                   leaderboard_title:str,
                                   sorting_method: app_commands.Choice[str], 
                                   show_member_count: bool,
                                   show_no_elo_players: bool,
                                   channel_1v1_id:str,
                                   channel_2v2_id:str,
                                   channel_rotating_id:str,
                                   flag_type:app_commands.Choice[str],
                                   color:str="0xFFFFFF",
                                   image:str=""):
    await initialise_server(interaction, leaderboard_title, sorting_method.value, show_member_count, show_no_elo_players, channel_1v1_id, channel_2v2_id, channel_rotating_id, color, image, flag_type.value)


@tree.command(name=PING_COMMAND[1:])
async def ping_command(interaction):
    await ping(interaction)


@tree.command(name=REMOVE_ACCOUNT_LINKER_COMMAND[1:], description='Remove an Account Linker')
@app_commands.checks.has_permissions(administrator=True)
async def remove_account_linker_command(interaction, brawlhalla_id:int):
    await remove_account_linker(interaction, brawlhalla_id)


@tree.command(name=REMOVE_CONSOLE_PLAYER_COMMAND[1:], description='Remove a console player')
@app_commands.checks.has_permissions(administrator=True)
async def remove_console_player_command(interaction, brawlhalla_id:int):
    await remove_console_player(interaction, brawlhalla_id)


@tree.command(name=REMOVE_SERVER_PLAYER_COMMAND[1:], description="(You aren't suposed to run this) Manually removes a player off the server leaderboard")
@app_commands.checks.has_permissions(administrator=True)
async def remove_server_player_command(interaction, brawlhalla_id:int):
    await remove_server_player(interaction, brawlhalla_id)

@tree.command(name=SERVER_PLAYER_LIST[1:], description="(List all server players")
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
    #client.run(env_variable("TEST_BOT_TOKEN"))
    # return
