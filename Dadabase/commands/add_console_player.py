import json
from Dadabase.classes.BrawlhallaAccount import BrawlhallaAccount
from Dadabase.modules.data_management import read_data, add_player_to_clan_data, CLANS_DATA_LOCATION, DATA_KEY_FOR_CONSOLE_PLAYERS


async def add_console_player(interaction, bh_id, bh_name):
    if __validate_id(bh_id):
        brawlhalla_account = __create_brawlhalla_account(bh_id, bh_name)
        clan_data = read_data(CLANS_DATA_LOCATION, interaction.guild.id)
        add_player_to_clan_data(interaction, clan_data, brawlhalla_account, CLANS_DATA_LOCATION, DATA_KEY_FOR_CONSOLE_PLAYERS)
        await interaction.response.send_message(bh_name + ' was added')
    else:
        await interaction.response.send_message(str(bh_id) + " is not a valid brawlhalla_id")


def __create_brawlhalla_account(brawlhalla_id, brawlhalla_name):
    account = BrawlhallaAccount(brawlhalla_id, brawlhalla_name)
    return account


def __validate_id(id):
    if isinstance(id, int):
        return True
    else:
        return False
