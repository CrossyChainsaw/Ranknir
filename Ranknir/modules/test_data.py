from Ranknir.classes.Clan import Clan
from Ranknir.classes.Player import Player
from Ranknir.classes.Server import Server
from Ranknir.modules.data_management import TEST_SERVER_ID, load_clan, load_server

CLAN_DATA = {
    "clan_id": 84648,
    "clan_name": "Skyward",
    "clan_create_date": 1469763610,
    "clan_xp": "16278123",
    "clan": [
        {
            "brawlhalla_id": 74662063,
            "name": "Courteous Crocodile 001163",
            "rank": "Leader",
            "join_date": 1647024356,
            "xp": 45981
        },
        {
            "brawlhalla_id": 9317622,
            "name": "Hitaku",
            "rank": "Officer",
            "join_date": 1653661551,
            "xp": 13368
        }
    ]
}

CLAN_OBJECT = load_clan(TEST_SERVER_ID)
SERVER_OBJECT = load_server(TEST_SERVER_ID)
CLAN_PLAYER_DATA = [{"brawlhalla_id": "12974529", "brawlhalla_name": "CrossyChris (PS4)"}, {"brawlhalla_id": "12974529", "brawlhalla_name": "CrossyChris (PS4)"}]
PLAYER_OBJECT_DATA = [
    Player('Lionheart', 2200, 2400),
    Player('Whirlwind', 2050, 2550),
    Player('Stardust', 2350, 2500),
    Player('Thunderbolt', 2150, 2600),
    Player('Evergreen', 2350, 2600),
    Player('Moonlight', 2050, 2550),
    Player('Firefly', 2150, 2350),
    Player('Sunshine', 2100, 2500),
    Player('Wildfire', 2050, 2300),
    Player('Dragonfly', 2200, 2600),
    Player('Silverwing', 2050, 2550),
    Player('Oceanwave', 2200, 2550),
    Player('Raindrop', 2100, 2600),
    Player('Thunderstorm', 2250, 2450),
    Player('Starlight', 2150, 2500),
    Player('Avalanche', 2200, 2600),
    Player('Blizzard', 2050, 2600),
    Player('Wildflower', 2200, 2500),
    Player('Whirlpool', 2150, 2600),
    Player('Mountainpeak', 2100, 2550),
    Player('Eclipse', 2250, 2450),
    Player('Tornado', 2350, 2600),
    Player('Sunrise', 2250, 2500),
    Player('Blossom', 2300, 2550),
    Player('Phoenix', 2150, 2400),
    Player('Rainbow', 2250, 2550),
    Player('Meadow', 2150, 2350),
    Player('Seastorm', 2200, 2500),
    Player('Twilight', 2050, 2350),
    Player('Frostbite', 2100, 2450),
    Player('Starfish', 2200, 2550),
    Player('Thunderbird', 2250, 2600),
    Player('Everest', 2150, 2500),
    Player('Wilderness', 2050, 2400),
    Player('Tidalwave', 2100, 2600),
    Player('Sundown', 2200, 2450),
    Player('Comet', 2050, 2550),
    Player('Firestorm', 2250, 2600),
    Player('Rainforest', 2150, 2500),
    Player('Moonstone', 2050, 2400),
    Player('Sunflower', 2200, 2500),
    Player('Stormcloud', 2150, 2600),
    Player('Skylight', 2100, 2400),
    Player('Riverbed', 2250, 2500),
    Player('Whitewater', 2200, 2600),
    Player('Sunset', 2150, 2450),
    Player('Aurora', 2050, 2400),
    Player('Canyon', 2100, 2550),
    Player('Thunderhead', 2250, 2500),
    Player('Starburst', 2200, 2450)
]

SERVER_PLAYER_OBJECT_DATA = [
    Player('Lionheart', 2200, 2400, "DE", "FR"),
    Player('Whirlwind', 2050, 2550, "IT", "ES"),
    Player('Stardust', 2350, 2500, "PT", "RU"),
    Player('Thunderbolt', 2150, 2600, "JP", "CN"),
    Player('Evergreen', 2350, 2600, "AU", "IN"),
    Player('Moonlight', 2050, 2550, "BR", "MX"),
    Player('Firefly', 2150, 2350, "CA", "US"),
    Player('Sunshine', 2100, 2500, "GB", "NL"),
    Player('Wildfire', 2050, 2300, "SE", "FI"),
    Player('Dragonfly', 2200, 2600, "NO", "DK"),
    Player('Silverwing', 2050, 2550, "PL", "GR"),
    Player('Oceanwave', 2200, 2550, "KR", "TW"),
    Player('Raindrop', 2100, 2600, "SG", "MY"),
    Player('Thunderstorm', 2250, 2450, "TH", "VN"),
    Player('Starlight', 2150, 2500, "ID", "PH"),
    Player('Avalanche', 2200, 2600, "SA", "AE"),
    Player('Blizzard', 2050, 2600, "ZA", "EG"),
    Player('Wildflower', 2200, 2500, "AR", "CL"),
    Player('Whirlpool', 2150, 2600, "CO", "PE"),
    Player('Mountainpeak', 2100, 2550, "UY", "CR"),
    Player('Eclipse', 2250, 2450, "QA", "KW"),
    Player('Tornado', 2350, 2600, "FI", "NO"),
    Player('Sunrise', 2250, 2500, "DK", "SE"),
    Player('Blossom', 2300, 2550, "GR", "PL"),
    Player('Phoenix', 2150, 2400, "TW", "KR"),
    Player('Rainbow', 2250, 2550, "CN", "JP"),
    Player('Meadow', 2150, 2350, "IN", "AU"),
    Player('Seastorm', 2200, 2500, "RU", "PT"),
    Player('Twilight', 2050, 2350, "ES", "IT"),
    Player('Frostbite', 2100, 2450, "FR", "DE"),
    Player('Starfish', 2200, 2550, "MX", "BR"),
    Player('Thunderbird', 2250, 2600, "US", "CA"),
    Player('Everest', 2150, 2500, "NL", "GB"),
    Player('Wilderness', 2050, 2400, "FI", "NO"),
    Player('Tidalwave', 2100, 2600, "SE", "DK"),
    Player('Sundown', 2200, 2450, "PL", "GR"),
    Player('Comet', 2050, 2550, "TW", "KR"),
    Player('Firestorm', 2250, 2600, "JP", "CN"),
    Player('Rainforest', 2150, 2500, "SG", "MY"),
    Player('Moonstone', 2050, 2400, "TH", "VN"),
    Player('Sunflower', 2200, 2500, "ID", "PH"),
    Player('Stormcloud', 2150, 2600, "SA", "AE"),
    Player('Skylight', 2100, 2400, "ZA", "EG"),
    Player('Riverbed', 2250, 2500, "AR", "CL"),
    Player('Whitewater', 2200, 2600, "CO", "PE"),
    Player('Sunset', 2150, 2450, "UY", "CR"),
    Player('Aurora', 2050, 2400, "QA", "KW"),
    Player('Canyon', 2100, 2550, "FI", "NO"),
    Player('Thunderhead', 2250, 2500, "DK", "SE"),
    Player('Starburst', 2200, 2450, "GR", "PL")
]



AL_PLAYERS = [{"brawlhalla_id": "7013979", "brawlhalla_name": "CrossyChris"}]