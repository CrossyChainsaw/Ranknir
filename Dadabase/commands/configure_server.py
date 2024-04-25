import json
from Dadabase.modules.data_management import SERVERS_DATA_LOCATION

async def configure_server(interaction, leaderboard_title, sorting_method, member_count, channel_1v1_id, channel_2v2_id, channel_rotating_id, color, image):
    try:
        __create_data_file(interaction)
        __edit_data_file(interaction, leaderboard_title, sorting_method, member_count, channel_1v1_id, channel_2v2_id, channel_rotating_id, color, image)
        await interaction.response.send_message('Succes! Created a data file for ' + interaction.guild.name)
    except Exception as ex:
        print(ex)
        await interaction.response.send_message('Something went wrong...')


def __create_data_file(interaction):
    open(SERVERS_DATA_LOCATION + str(interaction.guild.id) + '.json', 'x')


def __edit_data_file(interaction, leaderboard_title, sorting_method:str, member_count:str, no_elo_players:str, channel_1v1_id:int, channel_2v2_id:int, channel_rotating_id:int, color:str, image:str):
    file_path = SERVERS_DATA_LOCATION + str(interaction.guild.id) + '.json'
    with open(file_path, 'a') as file:
        server_data = {
            "id": interaction.guild.id,
            "name": interaction.guild.name,
            "leaderboard_title": leaderboard_title,
            "sorting_method": sorting_method,
            "channel_1v1_id": channel_1v1_id,
            "channel_2v2_id": channel_2v2_id,
            "channel_rotating_id": channel_rotating_id,
            "image": image,
            "member_count": member_count,
            "no_elo_players": no_elo_players,
            "color": int(color, 16),
            "links": []
        }
        file.write(json.dumps(server_data, indent=4))
