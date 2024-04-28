from Dadabase.modules.data_management import DATA_KEY_FOR_SHOW_MEMBER_COUNT, DATA_KEY_FOR_SHOW_NO_ELO_PLAYERS, read_data, CLANS_DATA_PATH, write_data, DATA_KEY_FOR_SHOW_XP
from Dadabase.modules.format import bool_to_show_hide, format_color


async def edit_clan(interaction, channel_1v1_id:str, channel_2v2_id:str, color:str, image, sorting_method:str, show_member_count:bool, 
                    show_xp:bool, show_no_elo_players:bool, channel_rotating_id:str):
    # load data
    clan_data = read_data(CLANS_DATA_PATH, interaction.guild.id)
    # Check if any parameter has been filled in
    if any([channel_1v1_id is not None, channel_2v2_id is not None, color is not None, image is not None,
        sorting_method is not None, show_member_count is not None, show_xp is not None,
        show_no_elo_players is not None, channel_rotating_id is not None]):

        # Update clan_data with non-empty parameters
        if channel_1v1_id:
            clan_data['channel_1v1_id'] = int(channel_1v1_id)
        if channel_2v2_id:
            clan_data['channel_2v2_id'] = int(channel_2v2_id)
        if color:
            clan_data['color'] = format_color(color)
        if image:
            clan_data['image'] = image
        if sorting_method:
            clan_data['sorting_method'] = sorting_method
        if show_member_count:
            clan_data[DATA_KEY_FOR_SHOW_MEMBER_COUNT] = bool_to_show_hide(show_member_count)
        if show_xp:
            clan_data[DATA_KEY_FOR_SHOW_XP] = bool_to_show_hide(show_xp)
        if show_no_elo_players:
            clan_data[DATA_KEY_FOR_SHOW_NO_ELO_PLAYERS] = bool_to_show_hide(show_no_elo_players)
        if channel_rotating_id:
            clan_data['channel_rotating_id'] = int(channel_rotating_id)

        write_data(CLANS_DATA_PATH, clan_data, interaction.guild.id)
        await interaction.response.send_message("Update clan data")
    else:
        await interaction.response.send_message("No parameter has been provided")