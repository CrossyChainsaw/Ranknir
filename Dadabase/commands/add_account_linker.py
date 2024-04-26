import json
from Dadabase.classes.BrawlhallaAccount import BrawlhallaAccount
from Dadabase.modules.data_management import read_data, add_player_to_clan_data, CLANS_DATA_PATH, DATA_KEY_FOR_ACCOUNT_LINKERS
from Dadabase.modules.validate_type import id_is_int

async def add_account_linker(interaction, brawlhalla_id, brawlhalla_name):
    if id_is_int(brawlhalla_id):
        brawlhalla_account = BrawlhallaAccount(brawlhalla_id, brawlhalla_name)
        clan_data = read_data(CLANS_DATA_PATH, interaction.guild.id)
        add_player_to_clan_data(interaction, clan_data, brawlhalla_account, CLANS_DATA_PATH, DATA_KEY_FOR_ACCOUNT_LINKERS)
        await interaction.response.send_message(brawlhalla_name + ' was added')
    else:
        await interaction.response.send_message(str(brawlhalla_id) + " is not a valid brawlhalla_id")
