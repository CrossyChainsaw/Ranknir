from Ranknir.data.clan_data import test_clan
from Ranknir.classes.Player import Player
from Ranknir.modules.tests.test_data import CLAN_DATA, CLAN_OBJECT, AL_PLAYERS, PLAYER_OBJECT_DATA, SERVER_OBJECT, SERVER_PLAYER_OBJECT_DATA
from Ranknir.modules.sort_elo import sort_elo
from Ranknir.modules.embed import prepare_embeds_clan_mix_console, send_embeds, prepare_embeds_server

async def test_clan_console_mix_1v1_elo_list(bot, ctx):
    clan = CLAN_OBJECT

    # structure -> all_players_array = [[console_players], [clan1_players], [clan2_players], [clan3_players]]
    all_player_objects_array = []
    
    # Get Console Players
    console_players = []
    console_player_objects = []
    all_player_objects_array.append(console_player_objects)
    
    # Get Clan
    clan_data_array = []
    for i in range(len(clan.id_array)):
        # Get Clan Data
        clan_data = CLAN_DATA
        clan_data_array.append(clan_data)
        # Get Clan Players
        clan_players = clan_data['clan']
        # Remove rm Players
        if clan.has_rm_players:
            rm_players = AL_PLAYERS
            clan_players = [p for p in clan_players if p['brawlhalla_id'] not in rm_players]
        # Get Elo
        clan_player_objects = PLAYER_OBJECT_DATA[:21]
        all_player_objects_array.append(clan_player_objects)
    
    # Restructure the array with all players
    all_player_objects_array_restructured = __fix_structure(all_player_objects_array)
    all_player_objects_array_sorted = sort_elo(clan.sorting_method, all_player_objects_array_restructured)
    embed_title, embed_array = prepare_embeds_clan_mix_console(
        clan,
        all_player_objects_array_sorted,
        clan_data_array,
        console_player_amount=len(console_players))
    await send_embeds(embed_title, embed_array, bot, clan, clan.channel_1v1_id)

async def test_server_1v1_elo_list(bot, ctx):
    server = SERVER_OBJECT

    #print("Server 1v1 elo list for " + server.get_server_name())
    # __try_update_data(server)
    # brawlhalla_nl_players = _
    all_player_objects_array = SERVER_PLAYER_OBJECT_DATA[:21]
    all_player_objects_sorted = sort_elo(server.sorting_method, all_player_objects_array)
    embed_title, embed_array = prepare_embeds_server(server, all_player_objects_sorted)
    await send_embeds(embed_title, embed_array, bot, server,server.channel_1v1_id)

async def test_server_1v1_and_2v2_and_rotating_elo_list(bot, ctx):
    server = SERVER_OBJECT
    # Get Elo
    all_players_array, all_teams_array, all_rotating_array = SERVER_PLAYER_OBJECT_DATA[:21], SERVER_PLAYER_OBJECT_DATA[:21], SERVER_PLAYER_OBJECT_DATA[:21]
    # Sort Elo
    all_players_sorted = sort_elo(server.sorting_method, all_players_array)
    all_teams_sorted = sort_elo(server.sorting_method, all_teams_array)
    all_rotating_array = sort_elo(server.sorting_method, all_rotating_array)
    # Send 1v1 Elo List
    embed_title, embed_array = prepare_embeds_server(server, all_players_sorted)
    await send_embeds(embed_title, embed_array, bot, server, server.channel_1v1_id)
    # Send 2v2 Elo List
    embed_title, embed_array = prepare_embeds_server(server, all_teams_sorted)
    await send_embeds(embed_title, embed_array, bot, server, server.channel_2v2_id)
    # Send Rotating Elo List
    embed_title, embed_array = prepare_embeds_server(server, all_rotating_array)
    await send_embeds(embed_title, embed_array, bot, server, server.channel_rotating_id)


def __fix_structure(all_players_array):
    # new structure -> restructured_player_array = [console players + clan1_players + clan2_players + clan3_players]
    restructured_player_array = []
    for player_array in all_players_array:
        for player in player_array:
            restructured_player_array.append(player)
    return restructured_player_array