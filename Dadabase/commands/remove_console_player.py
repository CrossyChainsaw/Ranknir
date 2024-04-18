import json
from Dadabase.modules.data_management import read_data, CLANS_DATA_LOCATION


async def remove_console_player(interaction, bh_id):
    data = read_data(CLANS_DATA_LOCATION, interaction.guild.id)
    bh_name = __remove_ps4_player(interaction, bh_id, data)
    await interaction.resopnse.send_message(bh_name + " was removed")


def __remove_ps4_player(interaction, bh_id, data):
    bh_name = ""
    index = 0
    for player in data['ps4_players']:
        if player['brawlhalla_id'] == str(bh_id):
            bh_name = data['ps4_players'].pop(index)['brawlhalla_name']
            with open(CLANS_DATA_LOCATION + str(interaction.guild.id) + '.json', 'w') as file:
                json.dump(data, file)
        index += 1
    return bh_name
