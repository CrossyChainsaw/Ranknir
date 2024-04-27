from Ranknir.classes.Clan import Clan
from Ranknir.classes.Server import Server
import json

# Paths
DADABASE_PATH = "Dadabase/"
DADABASE_SERVER_DATA_PATH = f"{DADABASE_PATH}data/servers/"
DADABASE_CLAN_DATA_PATH = f"{DADABASE_PATH}data/clans/"
# Data Keys
DATA_KEY_FOR_ACCOUNT_LINKERS = 'account_linkers' # account linkers / remove players / crossplayers
DATA_KEY_FOR_CONSOLE_PLAYERS = 'console_players' # console players
# Server_IDs
TEST_SERVER_ID = 705783420189671458
M30W_SERVER_ID = 1076670210678992936
BHNL_SERVER_ID = 1047987261905584128
BRAWL_HUNGARY_SERVER_ID = 1209624739635531857
PANDATION_SERVER_ID = 889594104873377812
TEWS_SERVER_ID = 160098918032605184
FROST_SERVER_ID = 167001986359754752
KRYPTX_SERVER_ID = 1162733824527048774
GRANT_SERVER_ID = 1208569714784342099
EMPIRE_UNITED_SERVER_ID = 1057780084582387793
AURA_SERVER_ID = 1215668996012245043
# Player IDs
CROSSYCHAINSAW_ID = 7364605
SHAW_ID = 395872
DISCARDS_ID = 15554673


def load_server(server_id):
    server_path = f"{DADABASE_SERVER_DATA_PATH}{server_id}.json"
    server_data = load_json_file(server_path)
    server = Server(
        server_data['id'],
        server_data['name'],
        server_data['leaderboard_title'],
        server_data['sorting_method'],
        server_data['member_count'],
        server_data['no_elo_players'],
        server_data['channel_1v1_id'],
        server_data['channel_2v2_id'],
        server_data['channel_rotating_id'],
        int(server_data['color'], 16),
        server_data['image'],
        server_data['links']
    )
    return server

def load_clan(server_id):
    clan_path = f"{DADABASE_CLAN_DATA_PATH}{server_id}.json"
    clan_data = load_json_file(clan_path)
    print(clan_data)
    clan = Clan(
        server_name=clan_data['server_name'],
        clan_names=clan_data['clan_names'],
        channel_1v1_id=clan_data['channel_1v1_id'],
        channel_2v2_id=clan_data['channel_2v2_id'],
        id_array=clan_data['id_array'],
        color=int(clan_data['color'], 16),
        image=clan_data['image'],
        server_id=clan_data['discord_server_id'],
        sorting_method=clan_data['sorting_method'],
        member_count=clan_data['member_count'],
        xp=clan_data['xp'],
        no_elo_players=clan_data['no_elo_players'],
        channel_rotating_id=clan_data['channel_rotating_id'],
        has_account_linkers=clan_data['has_account_linkers'],
        account_linkers=clan_data['account_linkers'],
        console_players=clan_data['console_players']
    )
    return clan

def load_json_file(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data