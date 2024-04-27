import json
import os
from typing import List
from Dadabase.modules.data_management import CLANS_DATA_PATH, EDIT_CLAN_COMMAND
from Dadabase.classes.Server import Server
from Dadabase.modules.format import split_string, format_color
from Dadabase.classes.Clan import Clan
from Dadabase.modules.validate_type import cast_to_int

async def configure_clan(interaction, clan_names: str, channel_1v1_id:str, channel_2v2_id:str, clan_id:str, color:str, image:str, sorting_method:str, member_count:str, xp:str, no_elo_players:str, channel_rotating_id:str, has_account_linkers:bool):
    # Convert Fields
    channel_1v1_id = int(channel_1v1_id)
    channel_2v2_id = int(channel_2v2_id)
    channel_rotating_id = cast_to_int(channel_rotating_id)
    color = format_color(color)
    clan_names = split_string(clan_names)
    clan_id = split_string(clan_id)
    # Logic
    clan = Clan(interaction.guild.name, clan_names, channel_1v1_id, channel_2v2_id, clan_id, color, image, str(interaction.guild.id), sorting_method, member_count, xp, no_elo_players, channel_rotating_id, has_account_linkers)
    if os.path.exists(f"{CLANS_DATA_PATH}{interaction.guild.id}.json"):
        await interaction.response.send_message(f"Oops! This server already exists. Consider running `{EDIT_CLAN_COMMAND}` to update data.")
    else:
        __create_data_file(interaction, clan)
        await interaction.response.send_message(f"Succes! Created data for {interaction.guild.name}")

def __create_data_file(interaction, clan: Clan):
    file_path = f"{CLANS_DATA_PATH}{interaction.guild.id}.json"
    with open(file_path, 'w') as file:
        clan = json.dumps(clan.__dict__, indent=4)
        file.write(clan)
