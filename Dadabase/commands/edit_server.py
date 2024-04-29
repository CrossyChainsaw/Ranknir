from Dadabase.modules.data_management import DATA_KEY_FOR_COLOR, DATA_KEY_FOR_IMAGE, DATA_KEY_FOR_SHOW_MEMBER_COUNT, DATA_KEY_FOR_CHANNEL_1V1_ID, DATA_KEY_FOR_CHANNEL_2V2_ID, DATA_KEY_FOR_CHANNEL_ROTATING_ID, DATA_KEY_FOR_LEADERBOARD_TITLE, DATA_KEY_FOR_FLAG_TYPE, DATA_KEY_FOR_SERVER_ID, DATA_KEY_FOR_SERVER_NAME, DATA_KEY_FOR_SHOW_NO_ELO_PLAYERS, DATA_KEY_FOR_SHOW_XP, DATA_KEY_FOR_SORTING_METHOD, DATA_KEY_FOR_SHOW_MEMBER_COUNT, DATA_KEY_FOR_SHOW_NO_ELO_PLAYERS, SERVERS_DATA_PATH, FlagType, read_data, write_data, DATA_KEY_FOR_SHOW_XP
from Dadabase.modules.format import bool_to_show_hide, format_color
from Dadabase.classes.Server import Server


async def edit_server(interaction, leaderboard_title, sorting_method:str, show_member_count:bool,show_no_elo_players:bool,
                      channel_1v1_id:str, channel_2v2_id:str, channel_rotating_id:str, image:str, color:str, flag_type:str):
    # load data
    server_data = read_data(SERVERS_DATA_PATH, interaction.guild.id)
    # Check if any parameter has been filled in
    if any([leaderboard_title is not None, sorting_method is not None, show_member_count is not None,
        show_no_elo_players is not None, channel_1v1_id is not None, channel_2v2_id is not None,
        channel_rotating_id is not None, image is not None, color is not None, flag_type is not None]):

        if leaderboard_title:
            server_data[DATA_KEY_FOR_LEADERBOARD_TITLE] = leaderboard_title
        if sorting_method:
            server_data[DATA_KEY_FOR_SORTING_METHOD] = sorting_method.value
        if show_member_count is not None:
            server_data[DATA_KEY_FOR_SHOW_MEMBER_COUNT] = show_member_count
        if show_no_elo_players is not None:
            server_data[DATA_KEY_FOR_SHOW_NO_ELO_PLAYERS] = show_no_elo_players

        if channel_1v1_id:
            server_data[DATA_KEY_FOR_CHANNEL_1V1_ID] = int(channel_1v1_id)
        if channel_2v2_id:
            server_data[DATA_KEY_FOR_CHANNEL_2V2_ID] = int(channel_2v2_id)
        if channel_rotating_id:
            server_data[DATA_KEY_FOR_CHANNEL_ROTATING_ID] = int(channel_rotating_id)

        if image:
            server_data[DATA_KEY_FOR_IMAGE] = image
        if color:
            server_data[DATA_KEY_FOR_COLOR] = color
        if flag_type:
            server_data[DATA_KEY_FOR_FLAG_TYPE] = flag_type.value
        write_data(SERVERS_DATA_PATH, server_data, interaction.guild.id)
        await interaction.response.send_message("Update clan data")
    else:
        await interaction.response.send_message("No parameter has been provided")