import json
from Dadabase.modules.data_management import SERVERS_DATA_LOCATION
from Dadabase.classes.Server import Server

async def configure_server(interaction, 
                           leaderboard_title, 
                           sorting_method, 
                           member_count,
                           no_elo_players, 
                           channel_1v1_id, 
                           channel_2v2_id, 
                           channel_rotating_id, 
                           color, 
                           image):
    server = Server(interaction.guild.id, interaction.guild.name, leaderboard_title, sorting_method, member_count, no_elo_players, channel_1v1_id, channel_2v2_id, channel_rotating_id, color, image)
    try:
        __create_data_file(interaction, server)
        await interaction.response.send_message('Succes! Created a data file for ' + interaction.guild.name)
    except Exception as ex:
        print(ex)
        await interaction.response.send_message('Something went wrong...')


def __create_data_file(interaction, server: Server):
    file_path = f"{SERVERS_DATA_LOCATION}{interaction.guild.id}.json"
    with open(file_path, 'w+') as file:
        server_data = json.dumps(server.__dict__, indent=4)
        file.write(server_data)
