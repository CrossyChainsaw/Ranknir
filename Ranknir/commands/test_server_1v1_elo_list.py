from Ranknir.modules.get_players import get_server_players
from Ranknir.modules.test_data import SERVER_OBJECT, SERVER_PLAYER_OBJECT_DATA
from Ranknir.modules.sort_elo import sort_elo
from Ranknir.modules.embed import send_embeds, prepare_embeds_server
from Ranknir.classes.Server import Server


async def test_server(bot):
    # Set Test Variables
    server = SERVER_OBJECT
    all_player_objects_array = SERVER_PLAYER_OBJECT_DATA[20:]
    # Logic - in best case this is the actual function, not a copy which is slightly modified
    await __test_server_1v1_elo_list(bot, server, all_player_objects_array)

async def __test_server_1v1_elo_list(bot, server, all_player_objects_array):
    print("Server 1v1 elo list for " + server.name)
    # __try_update_data(server)
    brawlhalla_nl_players = get_server_players(server)
    #all_player_objects_array, _ = await get_players_elo_1v1_and_2v2(server, brawlhalla_nl_players, server.name)
    all_player_objects_sorted = sort_elo(server.sorting_method, all_player_objects_array)
    embed_title, embed_array = prepare_embeds_server(server, all_player_objects_sorted)
    await send_embeds(embed_title, embed_array, bot, server,server.channel_1v1_id)
