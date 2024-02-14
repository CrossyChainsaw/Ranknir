from Dadabase.modules.data import read_data, read_link_data

DATA_LINKS_LOCATION_SERVER_FROST = 'Dadabase/data/Frost/'
DATA_SINGLE_PLAYER_LOCATION = 'Dadabase/data/Frost/player_stats/'
FROST_SERVER_ID = 167001986359754752


def get_all_player_ids():
    link_data = read_link_data(
        DATA_LINKS_LOCATION_SERVER_FROST, FROST_SERVER_ID)
    all_ids = []
    for entry in link_data:
        all_ids.append(entry['brawlhalla_id'])
    return all_ids
