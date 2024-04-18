## hey i was refactoring dadabase to be structured like queen spy folderwise


import discord
from discord import app_commands
from discord.ext import commands
from Global.Xos import Xos
from Dadabase.commands.claim import claim
from Dadabase.commands.check import check
from Dadabase.commands.ping import ping
from Dadabase.commands.configure_clan import configure_clan
from Dadabase.commands.add_console_player import add_console_player
from Dadabase.commands.console_player_list import console_player_list
from Dadabase.commands.remove_console_player import remove_console_player
from discord.ext.commands import has_permissions
from Dadabase.commands.configure_server import configure_server
from Dadabase.modules.server.add_server_player import add_server_player
from Dadabase.modules.server.remove_server_player import remove_server_player
from Dadabase.modules.account_linkers.add_account_linker import add_account_linker
from Dadabase.commands.account_linker_list import account_linker_list
from Dadabase.modules.account_linkers.remove_account_linker import remove_account_linker
from Ranknir.data.server_data import Brawlhalla_NL, M3OW, Test_Server
from Ranknir.data.clan_data import Pandation, test_clan
os = Xos()

benelux_countries = [    
    app_commands.Choice(name="Netherlands", value="NL"),
    app_commands.Choice(name="Belgium", value="BE"),
    app_commands.Choice(name="Luxembourg", value="LU")]
all_countries = [
    app_commands.Choice(name="Netherlands", value="NL"),
    app_commands.Choice(name="Belgium", value="BE"),
    app_commands.Choice(name="Luxembourg", value="LU"),
    app_commands.Choice(name="Turkey", value="TR"),
    app_commands.Choice(name="Morocco", value="MA"),
    app_commands.Choice(name="Dominican Republic", value="DO"),
    app_commands.Choice(name="Spain", value="ES"),
    app_commands.Choice(name="Vietnam", value="VN"),
    app_commands.Choice(name="Algeria", value="DZ"),
    app_commands.Choice(name="Iraq", value="IQ"),
    app_commands.Choice(name="Suriname", value="SR"),
    app_commands.Choice(name="Japan", value="JP"),
    app_commands.Choice(name="Italy", value="IT"),
    app_commands.Choice(name="Curacao", value="CW"),
    app_commands.Choice(name="Indonesia", value="ID"),
    app_commands.Choice(name="Germany", value="DE"),
	app_commands.Choice(name="Canada", value="CA"),
	app_commands.Choice(name="United States of America", value="US"),
	app_commands.Choice(name="Brazil", value="BR"),
	app_commands.Choice(name="Argentina", value="AR"),
	app_commands.Choice(name="Chile", value="CL")]


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

@tree.command(name='check', description='Check your linked Brawlhalla account')
async def check_command(interaction):
    await check(interaction)


@tree.command(name='claim', description='Link your Brawlhalla account to Discord')
@app_commands.describe(country_of_residence="Which country do you live in?")
@app_commands.choices(country_of_residence=all_countries)
@app_commands.describe(nationality="What is your nationality?")
@app_commands.choices(nationality=all_countries)
async def claim_command(interaction, brawlhalla_id:int, country_of_residence: app_commands.Choice[str], nationality: app_commands.Choice[str]):
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
        await claim(interaction, brawlhalla_id, country_of_residence.value, nationality.value)
    else:
        await interaction.response.send_message(f'{member.name} does not have permission to use this command')

@tree.command(name='ping')
async def ping_command(interaction):
    await ping(interaction)



@tree.command(name='add_account_linker', description='Specify a player to remove from the leaderboard')
@app_commands.checks.has_permissions(administrator=True)
async def add_account_linker_command(interaction, brawlhalla_id:int, brawlhalla_name:str):
    await add_account_linker(interaction, brawlhalla_id, brawlhalla_name)


@tree.command(name='account_linker_list', description='List all Account Linkers')
async def account_linker_list_command(interaction):
    await account_linker_list(interaction)


@tree.command(name='remove_account_linker', description='Remove an Account Linker')
@app_commands.checks.has_permissions(administrator=True)
async def remove_account_linker_command(interaction, brawlhalla_id:int):
    await remove_account_linker(interaction, brawlhalla_id)


@tree.command(name='add_server_player', description="(You aren't suposed to run this) Manually add a player to the server leaderboard")
@app_commands.checks.has_permissions(administrator=True)
@app_commands.describe(country_of_residence="Which country does the player live in?")
@app_commands.choices(country_of_residence=all_countries)
@app_commands.describe(nationality="Which country does the player live in?")
@app_commands.choices(nationality=all_countries)
async def add_server_player_command(interaction: discord.Interaction, brawlhalla_id:int, discord_id:str, discord_name:str, country_of_residence: app_commands.Choice[str]="", nationality: app_commands.Choice[str]=""):
    discord_id = int(discord_id)
    await add_server_player(interaction, brawlhalla_id, discord_id, discord_name, country_of_residence, nationality)


@tree.command(name='remove_server_player', description="(You aren't suposed to run this) Manually removes a player off the server leaderboard")
@app_commands.checks.has_permissions(administrator=True)
async def remove_server_player_command(interaction, brawlhalla_id:int):
    await remove_server_player(interaction, brawlhalla_id)


@tree.command(name='add_console_player', description='Add a console player')
@app_commands.checks.has_permissions(administrator=True)
async def add_console_player_command(interaction, brawlhalla_id:int, brawlhalla_name:str):
    await add_console_player(interaction, brawlhalla_id, brawlhalla_name)


@tree.command(name='console_player_list', description='List all console players')
async def console_player_list_command(interaction):
    await console_player_list(interaction)


@tree.command(name='remove_console_player', description='Remove a console player')
@app_commands.checks.has_permissions(administrator=True)
async def remove_console_player_command(interaction, brawlhalla_id:int):
    await remove_console_player(interaction, brawlhalla_id)


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
    print(f'We have logged in as {client.user}')

def run_dadabase():
    client.run(os.environ[3])
    # client.run(os.environ[2]) # Testing
    return