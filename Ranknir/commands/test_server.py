from Ranknir.modules.data_management import TEST_SERVER_ID, load_server
from Ranknir.modules.get_players import get_server_players
from Ranknir.modules.test_data import SERVER_OBJECT, SERVER_PLAYER_OBJECT_DATA
from Ranknir.modules.sort_elo import sort_elo
from Ranknir.modules.embed import send_embeds, prepare_embeds_server
from Ranknir.classes.Server import Server


async def test_server(bot):
    # Set Test Variables
    server = load_server(TEST_SERVER_ID)
    all_player_objects_array = SERVER_PLAYER_OBJECT_DATA[:20]
    all_teams_array = SERVER_PLAYER_OBJECT_DATA[:20]
    # Logic - in best case this is the actual function, not a copy which is slightly modified
    await __test_server_2v2_elo_list(bot, server, all_player_objects_array)
    await __test_server_1v1_elo_list(bot, server, all_teams_array)

async def __test_server_1v1_elo_list(bot, server, all_player_objects_array):
    print("Server 1v1 elo list for " + server.name)
    # __try_update_data(server)
    brawlhalla_nl_players = get_server_players(server)
    #all_player_objects_array, _ = await get_players_elo_1v1_and_2v2(server, brawlhalla_nl_players, server.name)
    all_player_objects_sorted = sort_elo(server.sorting_method, all_player_objects_array)
    embed_title, embed_array = prepare_embeds_server(server, all_player_objects_sorted)
    await send_embeds(embed_title, embed_array, bot, server,server.channel_1v1_id)

async def __test_server_2v2_elo_list(bot, server:Server, all_teams_array):
    print("Server 2v2 elo list for " + server.name)
    brawlhalla_nl_players = get_server_players(server)
    #_, all_teams_array = await get_players_elo_1v1_and_2v2(server, brawlhalla_nl_players, server.name)
    all_team_objects_sorted = sort_elo(server.sorting_method, all_teams_array)
    embed_title, embed_array = prepare_embeds_server(server, all_team_objects_sorted)
    await send_embeds(embed_title, embed_array, bot, server, server.channel_2v2_id)
