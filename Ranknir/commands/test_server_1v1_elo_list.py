from Ranknir.modules.test_data import SERVER_OBJECT, SERVER_PLAYER_OBJECT_DATA
from Ranknir.modules.sort_elo import sort_elo
from Ranknir.modules.embed import send_embeds, prepare_embeds_server

async def test_server_1v1_elo_list(bot):
    server = SERVER_OBJECT
    all_player_objects_array = SERVER_PLAYER_OBJECT_DATA[:21]
    all_player_objects_sorted = sort_elo(server.sorting_method, all_player_objects_array)
    embed_title, embed_array = prepare_embeds_server(server, all_player_objects_sorted)
    await send_embeds(embed_title, embed_array, bot, server,server.channel_1v1_id)