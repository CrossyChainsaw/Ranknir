import json
import os
from Dadabase.modules.data_management import SERVERS_DATA_PATH
from Dadabase.modules.command import EDIT_SERVER_COMMAND
from Dadabase.classes.Server import Server

async def initialise_server(interaction, leaderboard_title, sorting_method, show_member_count, show_no_elo_players, channel_1v1_id, channel_2v2_id, channel_rotating_id, color, image, flag_type):
    # Logic
    server = Server(interaction.guild.id, interaction.guild.name, leaderboard_title, sorting_method, show_member_count, show_no_elo_players, channel_1v1_id, channel_2v2_id, channel_rotating_id, color, image, flag_type)
    if os.path.exists(f"{SERVERS_DATA_PATH}{interaction.guild.id}.json"):
        await interaction.response.send_message(f"Oops! This server already exists. Consider running `{EDIT_SERVER_COMMAND}` to update data.")
    else:
        __create_data_file(interaction, server)
        await interaction.response.send_message(f"Succes! Created data for {interaction.guild.name}")

def __create_data_file(interaction, server: Server):
    file_path = f"{SERVERS_DATA_PATH}{interaction.guild.id}.json"
    with open(file_path, 'w') as file:
        server_data = json.dumps(server.__dict__, indent=4)
        file.write(server_data)
