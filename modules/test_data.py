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
    Player('Lionheart', 2200, 2400, "USE", "FR", "DE"),
    Player('Whirlwind', 2050, 2550, "USW", "ES", "IT"),
    Player('Stardust', 2350, 2500, "EU", "RU", "PT"),
    Player('Thunderbolt', 2150, 2600, "SEA", "CN", "JP"),
    Player('Evergreen', 2350, 2600, "AU", "IN", "AU"),
    Player('Moonlight', 2050, 2550, "BR", "MX", "BR"),
    Player('Firefly', 2150, 2350, "JP", "US", "CA"),
    Player('Sunshine', 2100, 2500, "MDE", "NL", "GB"),
    Player('Wildfire', 2050, 2300, "SAF", "FI", "SE"),
    Player('Dragonfly', 2200, 2600, "USE", "DK", "NO"),
    Player('Silverwing', 2050, 2550, "USW", "GR", "PL"),
    Player('Oceanwave', 2200, 2550, "EU", "TW", "KR"),
    Player('Raindrop', 2100, 2600, "SEA", "MY", "SG"),
    Player('Thunderstorm', 2250, 2450, "AU", "VN", "TH"),
    Player('Starlight', 2150, 2500, "BR", "PH", "ID"),
    Player('Avalanche', 2200, 2600, "JP", "AE", "SA"),
    Player('Blizzard', 2050, 2600, "MDE", "EG", "ZA"),
    Player('Wildflower', 2200, 2500, "SAF", "CL", "AR"),
    Player('Whirlpool', 2150, 2600, "USW", "PE", "CO"),
    Player('Mountainpeak', 2100, 2550, "EU", "CR", "UY"),
    Player('Eclipse', 2250, 2450, "SEA", "KW", "QA"),
    Player('Tornado', 2350, 2600, "AU", "NO", "FI"),
    Player('Sunrise', 2250, 2500, "BR", "SE", "DK"),
    Player('Blossom', 2300, 2550, "USE", "PL", "GR"),
    Player('Phoenix', 2150, 2400, "EU", "KR", "TW"),
    Player('Rainbow', 2250, 2550, "USW", "JP", "CN"),
    Player('Meadow', 2150, 2350, "SEA", "AU", "IN"),
    Player('Seastorm', 2200, 2500, "AU", "PT", "RU"),
    Player('Twilight', 2050, 2350, "BR", "IT", "ES"),
    Player('Frostbite', 2100, 2450, "JP", "DE", "FR"),
    Player('Starfish', 2200, 2550, "USW", "BR", "MX"),
    Player('Thunderbird', 2250, 2600, "USE", "CA", "US"),
    Player('Everest', 2150, 2500, "MDE", "GB", "NL"),
    Player('Wilderness', 2050, 2400, "SAF", "NO", "FI"),
    Player('Tidalwave', 2100, 2600, "SEA", "DK", "SE"),
    Player('Sundown', 2200, 2450, "USW", "GR", "PL"),
    Player('Comet', 2050, 2550, "EU", "KR", "TW"),
    Player('Firestorm', 2250, 2600, "SEA", "CN", "JP"),
    Player('Rainforest', 2150, 2500, "BR", "MY", "SG"),
    Player('Moonstone', 2050, 2400, "MDE", "VN", "TH"),
    Player('Sunflower', 2200, 2500, "MDE", "PH", "ID"),
    Player('Stormcloud', 2150, 2600, "SAF", "AE", "SA"),
    Player('Skylight', 2100, 2400, "SAF", "EG", "ZA"),
    Player('Riverbed', 2250, 2500, "USE", "CL", "AR"),
    Player('Whitewater', 2200, 2600, "USW", "PE", "CO"),
    Player('Sunset', 2150, 2450, "EU", "CR", "UY"),
    Player('Aurora', 2050, 2400, "SEA", "KW", "QA"),
    Player('Canyon', 2100, 2550, "AU", "NO", "FI"),
    Player('Thunderhead', 2250, 2500, "EU", "SE", "DK"),
    Player('Starburst', 2200, 2450, "SAF", "PL", "GR")
]





AL_PLAYERS = [{"brawlhalla_id": "7013979", "brawlhalla_name": "CrossyChris"}]