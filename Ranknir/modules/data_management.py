from Ranknir.classes.Server import Server
import json

# Paths
DADABASE_PATH = "Dadabase/"
DADABASE_SERVER_DATA_PATH = f"{DADABASE_PATH}data/servers"
DADABASE_CLAN_DATA_PATH = f"{DADABASE_PATH}data/clans"
# Server_IDs
TEST_SERVER_ID = 705783420189671458
M30W_SERVER_ID = 1076670210678992936
BHNL_SERVER_ID = 1047987261905584128
BHHU_SERVER_ID = 1209624739635531857
# Player IDs
CROSSYCHAINSAW_ID = 7364605
SHAW_ID = 395872
DISCARDS_ID = 15554673


def load_server(server_id):
    server_path = f"{DADABASE_SERVER_DATA_PATH}{server_id}.json"
    server_data = load_json_file(server_path)
    print(server_data)
    server = Server(server_data['id'],
                        server_data['name'],
                        server_data['leaderboard_title'],
                        server_data['sorting_method'],
                        server_data['member_count'],
                        server_data['no_elo_players'],
                        server_data['channel_1v1_id'],
                        server_data['channel_2v2_id'],
                        server_data['channel_rotating_id'],
                        int(server_data['color'], 16),
                        server_data['image'])
    return server

def load_json_file(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data