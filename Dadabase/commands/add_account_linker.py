import json
from Dadabase.classes.Account import Account
from Dadabase.modules.console_data import load_data, DATA_LOCATION
from Dadabase.modules.account_linker_data import NAME_FOR_REMOVE_PLAYERS

async def add_account_linker(interaction, bh_id, bh_name):
    if __validate_id(bh_id):
        account = __create_account(bh_id, bh_name)
        data = load_data(interaction.guild.id)
        __add_al_player(interaction, account, data)
        await interaction.response.send_message(bh_name + ' was added')
    else:
        await interaction.response.send_message(str(bh_id) + " is not a valid brawlhalla_id")


def __add_al_player(interaction, account, data):
    data[NAME_FOR_REMOVE_PLAYERS].append(account.__dict__)
    with open(DATA_LOCATION + str(interaction.guild.id) + '.json', 'w') as file:
        json.dump(data, file)


def __create_account(brawlhalla_id, brawlhalla_name):
    account = Account(brawlhalla_id, brawlhalla_name)
    return account

def __validate_id(id):
    if isinstance(id, int):
        return True
    else:
        return False
