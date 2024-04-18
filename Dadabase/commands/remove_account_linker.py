import json
from Dadabase.modules.data_management import read_data, CLANS_DATA_LOCATION, NAME_FOR_REMOVE_PLAYERS

async def remove_account_linker(interaction, bh_id):
    data = read_data(CLANS_DATA_LOCATION, interaction.guild.id)
    bh_name = __remove_rm_player(interaction, bh_id, data)
    await interaction.response.send_message(bh_name + " was removed")


def __remove_rm_player(interaction, bh_id, data):
    bh_name = ""
    index = 0
    for player in data[NAME_FOR_REMOVE_PLAYERS]:
        if player['brawlhalla_id'] == str(bh_id):
            bh_name = data[NAME_FOR_REMOVE_PLAYERS].pop(index)['brawlhalla_name']
            with open(CLANS_DATA_LOCATION + str(interaction.guild.id) + '.json', 'w') as file:
                json.dump(data, file)
        index += 1
    return bh_name
