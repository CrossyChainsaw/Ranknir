import json
from Dadabase.modules.data_management import read_data, CLANS_DATA_LOCATION, NAME_FOR_CONSOLE_PLAYERS


async def remove_console_player(interaction, bh_id):
    data = read_data(CLANS_DATA_LOCATION, interaction.guild.id)
    bh_name = __remove_console_player_from_data(interaction, bh_id, data)
    await interaction.resopnse.send_message(bh_name + " was removed")


def __remove_console_player_from_data(interaction, bh_id, data):
    bh_name = ""
    for index, player in enumerate(data[NAME_FOR_CONSOLE_PLAYERS]):
        if player['brawlhalla_id'] == str(bh_id):
            bh_name = data[NAME_FOR_CONSOLE_PLAYERS].pop(index)['brawlhalla_name']
            with open(CLANS_DATA_LOCATION + str(interaction.guild.id) + '.json', 'w') as file:
                json.dump(data, file)
            break
    return bh_name
