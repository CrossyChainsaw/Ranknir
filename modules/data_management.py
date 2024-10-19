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
    DIVISION_9 = 1207304690862129233
    CLIENT = 1244055902730981436
    VCNTY = 1222232229002870855
    AURA = 1271719485887479818
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
class LegendEmojis(Enum):
    random = "<:random:1295156657747132476>"
    bodvar = "<:bodvar:1295142317044400140>"
    cassidy = "<:cassidy:1295142767470575669>"
    orion = "<:orion:1295142821396877422>"
    lordvraxx = "<:lordvraxx:1295142831748546661>"
    gnash = "<:gnash:1295142839126196264>"
    queennai = "<:queennai:1295142867022512198>"
    hattori = "<:hattori:1295142873867616286>"
    sirroland = "<:sirroland:1295142882713403442>"
    scarlet = "<:scarlet:1295143813358161981>"
    thatch = "<:thatch:1295143831578083360>"
    ada = "<:ada:1295143845989974047>"
    sentinel = "<:sentinel:1295144096129749083>"
    lucien = "<:lucien:1295144110260359208>"
    teros = "<:teros:1295144119051485254>"
    brynn = "<:brynn:1295144132557148241>"
    asuri = "<:asuri:1295144158863822900>"
    barraza = "<:barraza:1295144208767910049>"
    ember = "<:ember:1295144232146829392>"
    azoth = "<:azoth:1295144242804555837>"
    koji = "<:koji:1295144252929474583>"
    ulgrim = "<:ulgrim:1295144263545389080>"
    diana = "<:diana:1295144273246683147>"
    jhala = "<:jhala:1295144284437090324>"
    kor = "<:kor:1295144479451516999>"
    wushang = "<:wushang:1295144488473198774>"
    val = "<:val:1295144502197092515>"
    ragnir = "<:ragnir:1295144509453111357>"
    cross = "<:cross:1295144518232051832>"
    mirage = "<:mirage:1295144589849657416>"
    nix = "<:nix:1295144633399120003>"
    mordex = "<:mordex:1295144640345014404>"
    yumiko = "<:yumiko:1295144647672201237>"
    artemis = "<:artemis:1295144655163232317>"
    caspian = "<:caspian:1295144662259990623>"
    sidra = "<:sidra:1295144671710019704>"
    xull = "<:xull:1295144682132602942>"
    kaya = "<:kaya:1295144689225433218>"
    isaiah = "<:isaiah:1295144735354261604>"
    jiro = "<:jiro:1295144742232916090>"
    linfei = "<:linfei:1295144753138237532>"
    zariel = "<:zariel:1295144758980644904>"
    rayman = "<:rayman:1295144768598315061>"
    dusk = "<:dusk:1295144776395522149>"
    fait = "<:fait:1295144788626112523>"
    thor = "<:thor:1295144795798241371>"
    petra = "<:petra:1295145039864791171>"
    vector = "<:vector:1295145046169092156>"
    volkov = "<:volkov:1295145065110568971>"
    onyx = "<:onyx:1295145073016569966>"
    jaeyun = "<:jaeyun:1295145081275285545>"
    mako = "<:mako:1295145090234454028>"
    magyar = "<:magyar:1295145096571916381>"
    reno = "<:reno:1295145105916690496>"
    munin = "<:munin:1295145114464686310>"
    arcadia = "<:arcadia:1295145122408697910>"
    ezio = "<:ezio:1295145131481239623>"
    tezca = "<:tezca:1295145138955485275>"
    thea = "<:thea:1295145147343962162>"
    redraptor = "<:redraptor:1295145154251849748>"
    loki = "<:loki:1295145162057580575>"
    seven = "<:seven:1295145169716379763>"
    vivi = "<:vivi:1295145176221745265>"
    imugi = "<:imugi:1295145187903012884>"
    kingzuva = "(i didnt add king zuva yet x crossy)"





async def load_clan_v2(server_id):
    clan_data = await request_clan_data_from_dadabase(server_id)
    clan = Clan(
        # Required
        server_name=clan_data['server_name'],
        clan_names=clan_data['clan_names'],
        server_id=clan_data['discord_server_id'],
        id_array=clan_data['id_array'],
        color=int(clan_data['color'], 16),
        image=clan_data['image'],
        channel_1v1_id=clan_data['channel_1v1_id'],
        channel_2v2_id=clan_data['channel_2v2_id'],

        # Optional
        channel_rotating_id=clan_data['channel_rotating_id'],
        sorting_method=clan_data['sorting_method'],
        show_member_count=clan_data['show_member_count'],
        show_xp=clan_data['show_xp'],
        show_no_elo_players=clan_data['show_no_elo_players'],
        show_win_loss=clan_data['show_win_loss'],
        show_legends=clan_data['show_legends'],

        # Arrays
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