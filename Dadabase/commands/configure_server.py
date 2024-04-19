import json
from Dadabase.modules.data_management import SERVERS_DATA_LOCATION

async def configure_server(interaction):
    try:
        __create_data_file(interaction)
        __edit_data_file(interaction)
        await interaction.response.send_message('Succes! Created a single id data file for ' + interaction.guild.name)
    except Exception as ex:
        print(ex)
        await interaction.response.send_message('Something went wrong...')


def __create_data_file(interaction):
    open(SERVERS_DATA_LOCATION + str(interaction.guild.id) + '.json', 'x')


def __edit_data_file(interaction):
    file_path = SERVERS_DATA_LOCATION + str(interaction.guild.id) + '.json'
    with open(file_path, 'a') as file:
        guild_data = {
            "name": interaction.guild.name,
            "title": interaction.guild.name + " Leaderboard",
            "links": []
        }
        file.write(json.dumps(guild_data, indent=4))
