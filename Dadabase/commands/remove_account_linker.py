import json
from Dadabase.modules.data_management import read_data, CLANS_DATA_LOCATION, DATA_KEY_FOR_ACCOUNT_LINKERS

async def remove_account_linker(interaction, bh_id):
    data = read_data(CLANS_DATA_LOCATION, interaction.guild.id)
    bh_name = __remove_account_linker_from_data(interaction, bh_id, data)
    await interaction.response.send_message(bh_name + " was removed")


def __remove_account_linker_from_data(interaction, bh_id, data):
    bh_name = ""
    for index, player in enumerate(data[DATA_KEY_FOR_ACCOUNT_LINKERS]):
        if player['brawlhalla_id'] == str(bh_id):
            bh_name = data[DATA_KEY_FOR_ACCOUNT_LINKERS].pop(index)['brawlhalla_name']
            with open(CLANS_DATA_LOCATION + str(interaction.guild.id) + '.json', 'w') as file:
                json.dump(data, file)
            break
    return bh_name
