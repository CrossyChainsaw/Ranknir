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
    TEST_SERVER = 705783420189671458
    M30W = 1076670210678992936
    BHNL = 1047987261905584128
    BRAWL_HUNGARY = 1209624739635531857
    PANDATION = 889594104873377812
    TEWS = 160098918032605184
    FROST = 167001986359754752
    KRYPTX = 1162733824527048774
    GRANT = 1208569714784342099
    EMPIRE_UNITED = 1057780084582387793
    AURA = 1215668996012245043
    DIVISION_9 = 1207304690862129233
    CLIENT = 1244055902730981436
# Player IDs
class PlayerIDs(IntEnum):
    CROSSYCHAINSAW = 7364605
    SHAW = 395872
    DISCARDS = 15554673
# Region Emojis (Ranknir)
class RegionFlagEmojis(Enum):
    EU = "<:EU:1270782273998028810>"
    USE = "<:USE:1270783240130789509>"
    USW = "<:USW:1270784536837492766>"
    BRS = "<:BR:1270784806304878746>"
    JPN = "<:JP:1270785580397105268>"
    SEA = "<:SG:1270785589549072515>"
    AUS = "<:AU:1270785838883536926>"
    MDE = "<:BH:1270786197341470762>"
    SAF = "<:SAF:1270786210914369577>"
class CountryFlagEmojis(Enum):
    NL = "<:NL:1271501670462914622>"
    BE = "<:BE:1271501685302231143>"
    TR = "<:TR:1271501963569270946>"
    MA = "<:MA:1271502296399872050>"
    ES = "<:ES:1271502528508596264>"
    IQ = "<:IQ:1271502667683856405>"
    DZ = "<:DZ:1271502856201048094>"
    VN = "<:VN:1271503050837590138>"
    DO = "<:DO:1271503819460575232>"
    SR = "<:SR:1271504221644001332>"
    CW = "<:CW:1271504740630401177>"
    SY = "<:SY:1271504880305180714>"
    IT = "<:IT:1271505073901539479>"
    ID = "<:ID:1271505213106421922>"
    DE = "<:DE:1271505206701588570>"
    JP = "<:JP:1270785580397105268>"
    BR = "<:BRS:1270784806304878746>"
    SG = "<:SG:1270785589549072515>"
    AU = "<:AU:1270785838883536926>"
    BH = "<:BH:1270786197341470762>"


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