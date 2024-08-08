from Ranknir.classes.Clan import Clan
from Ranknir.classes.Server import Server
from enum import Enum, IntEnum
import json
from Ranknir.modules.api import request_clan_data_from_dadabase, request_server_data_from_dadabase

# Paths
DADABASE_PATH = "Dadabase/"
DADABASE_SERVER_DATA_PATH = f"{DADABASE_PATH}data/servers/"
DADABASE_CLAN_DATA_PATH = f"{DADABASE_PATH}data/clans/"
# Data Keys
DATA_KEY_FOR_ACCOUNT_LINKERS = 'account_linkers' # account linkers / remove players / crossplayers
DATA_KEY_FOR_CONSOLE_PLAYERS = 'console_players' # console players
DATA_KEY_FOR_FLAG_TYPE = 'flag_type'
# Flag Type Values
class FlagType(Enum):
    NONE = None
    REGION = 'region'
    COUNTRY = 'country'
    ETHNICITY = 'ethnicity' 
# Server_IDs
class ServerIDs(IntEnum):
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
    DIVISION_SERVER_ID = 1207304690862129233
    CLIENT_SERVER_ID = 1244055902730981436
# Player IDs
CROSSYCHAINSAW_ID = 7364605
SHAW_ID = 395872
DISCARDS_ID = 15554673
# Region Emojis (Ranknir)
class RegionFlagEmojis(Enum):
    EU_FLAG = "<:EU:1270782273998028810>"
    USE_FLAG = "<:USE:1270783240130789509>"
    USW_FLAG = "<:USW:1270784536837492766>"
    BRS_FLAG = "<:BRS:1270784806304878746>"
    JPN_FLAG = "<:JPN:1270785580397105268>"
    SEA_FLAG = "<:SEA:1270785589549072515>"
    AUS_FLAG = "<:AUS:1270785838883536926>"
    MDE_FLAG = "<:MDE:1270786197341470762>"
    SAF_FLAG = "<:SAF:1270786210914369577>"

async def load_clan_v2(server_id):
    clan_data = await request_clan_data_from_dadabase(server_id)
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
        show_member_count=clan_data['show_member_count'],
        show_xp=clan_data['show_xp'],
        show_no_elo_players=clan_data['show_no_elo_players'],
        channel_rotating_id=clan_data['channel_rotating_id'],
        account_linkers=clan_data[DATA_KEY_FOR_ACCOUNT_LINKERS],
        console_players=clan_data[DATA_KEY_FOR_CONSOLE_PLAYERS]
    )
    return clan

async def load_server_v2(server_id):
    server_data = await request_server_data_from_dadabase(server_id)
    server = Server(
        id=server_data['id'],
        name=server_data['name'],
        leaderboard_title=server_data['leaderboard_title'],
        sorting_method=server_data['sorting_method'],
        show_member_count=server_data['show_member_count'],
        show_no_elo_players=server_data['show_no_elo_players'],
        channel_1v1_id=server_data['channel_1v1_id'],
        channel_2v2_id=server_data['channel_2v2_id'],
        channel_rotating_id=server_data['channel_rotating_id'],
        color=int(server_data['color'], 16),
        image=server_data['image'],
        flag_type=server_data[DATA_KEY_FOR_FLAG_TYPE],
        links=server_data['links']
    )
    return server

def load_json_file(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data