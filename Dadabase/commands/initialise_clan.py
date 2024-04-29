import json
import os
from Dadabase.modules.data_management import CLANS_DATA_PATH 
from Dadabase.modules.command import EDIT_CLAN_COMMAND
from Dadabase.classes.Clan import Clan

async def initialise_clan(interaction, clan_names: str, channel_1v1_id:str, channel_2v2_id:str, clan_id:str, color:str, image:str, sorting_method:str, show_member_count:bool, show_xp:bool, show_no_elo_players:bool, channel_rotating_id:str, server_id=None, server_name=None):
    # Convert Fields
    server_id = server_id if server_id is not None else interaction.guild.id
    server_name = server_name if server_name is not None else interaction.guild.name

    # Logic
    clan = Clan(server_name, clan_names, channel_1v1_id, channel_2v2_id, clan_id, color, image, str(server_id), sorting_method, show_member_count, show_xp, show_no_elo_players, channel_rotating_id)
    if os.path.exists(f"{CLANS_DATA_PATH}{server_id}.json"):
        await interaction.response.send_message(f"Oops! This server already exists. Consider running `{EDIT_CLAN_COMMAND}` to update data.")
    else:
        __create_data_file(server_id, clan)
        await interaction.response.send_message(f"Succes! Created data for {server_name}")

def __create_data_file(server_id, clan: Clan):
    file_path = f"{CLANS_DATA_PATH}{server_id}.json"
    with open(file_path, 'w') as file:
        clan = json.dumps(clan.__dict__, indent=4)
        file.write(clan)
