from Ranknir.classes.Clan import Clan
from Ranknir.classes.Server import Server
from Ranknir.modules.get_elo import get_players_elo_1v1_and_2v2, get_players_elo_1v1_and_2v2_and_rotating
from Ranknir.modules.sort_elo import sort_elo
from Ranknir.modules.embed import send_embeds, prepare_embeds_clan_mix_console, prepare_embeds_server
from Ranknir.modules.clan import get_clan_data

# -----------------------------------------------------------------#
#                          CLAN & CONSOLE                         #
# ----------------------------------------------------------------#


async def clan_console_mix_1v1_elo_list(clan:Clan, bot):
    # structure -> all_players_array = [[console_players], [clan1_players], [clan2_players], [clan3_players]]
    all_player_objects_array = []
    # Get Console Players
    console_players = clan.console_players
    console_player_objects, _ = await get_players_elo_1v1_and_2v2(clan, console_players, f"{clan.server_name} (Console)", is_console_players=True)
    all_player_objects_array.append(console_player_objects)
    # Get Clan
    clan_data_array = []
    for i in range(len(clan.id_array)):
        # Get Clan Data
        clan_data = await get_clan_data(clan.id_array[i])
        clan_data_array.append(clan_data)
        # Get Clan Players
        clan_players = clan_data['clan']
        # Remove rm Players
        rm_players = clan.account_linkers
        rm_player_ids = [player['brawlhalla_id'] for player in rm_players]
        clan_players = [player for player in clan_players if player['brawlhalla_id'] not in rm_player_ids]
        # Get Elo
        print("Starting")
        clan_player_objects, _ = await get_players_elo_1v1_and_2v2(clan, clan_players, clan.clan_names[i])
        all_player_objects_array.append(clan_player_objects)
        print('Completed!')
    # Restructure the array with all players
    all_player_objects_array_restructured = __fix_structure(all_player_objects_array)
    all_player_objects_array_sorted = sort_elo(clan.sorting_method, all_player_objects_array_restructured)
    embed_title, embed_array = prepare_embeds_clan_mix_console(
        clan,
        all_player_objects_array_sorted,
        clan_data_array,
        console_player_amount=len(console_players))
    await send_embeds(embed_title, embed_array, bot, clan, clan.channel_1v1_id)


async def clan_console_mix_2v2_elo_list(clan:Clan, bot):
    # structure -> all_players_array = [[console_players], [clan1_players], [clan2_players], [clan3_players]]
    all_team_objects_array = []
    # Get Console Players
    console_players = clan.console_players
    _, console_team_objects = await get_players_elo_1v1_and_2v2(clan, console_players, f"{clan.server_name} (Console)", is_console_players=True)
    all_team_objects_array.append(console_team_objects)
    # Get Clan
    clan_data_array = []
    for i in range(len(clan.id_array)):
        # Get Clan Data
        clan_data = await get_clan_data(clan.id_array[i])
        clan_data_array.append(clan_data)
        # Get Clan Players
        clan_players = clan_data['clan']
        # Remove rm Players
        rm_players = clan.account_linkers
        rm_player_ids = [player['brawlhalla_id'] for player in rm_players]
        clan_players = [player for player in clan_players if player['brawlhalla_id'] not in rm_player_ids]
        # Get Elo
        _, clan_team_objects = await get_players_elo_1v1_and_2v2(clan, clan_players, clan.clan_names[i])
        all_team_objects_array.append(clan_team_objects)
    # Restructure the array with all players
    all_team_objects_array_restructured = __fix_structure(
        all_team_objects_array)
    all_team_objects_array_sorted = sort_elo(
        clan.sorting_method, all_team_objects_array_restructured)
    embed_title, embed_array = prepare_embeds_clan_mix_console(
        clan,
        all_team_objects_array_sorted,
        clan_data_array,
        console_player_amount=len(console_players))
    await send_embeds(embed_title, embed_array, bot, clan, clan.channel_2v2_id)


async def clan_console_mix_1v1_and_2v2_elo_list(clan:Clan, bot, x=0):
    all_player_objects_array = []
    all_team_objects_array = []
    # Get Console Players
    console_players = clan.console_players
    console_player_objects, console_team_objects = await get_players_elo_1v1_and_2v2(clan, console_players, f"{clan.server_name} (Console)", is_console_players=True)
    all_player_objects_array.append(console_player_objects)
    all_team_objects_array.append(console_team_objects)
    # Foreach Clan...
    clan_data_array = []
    for i in range(len(clan.id_array)):
        # Get Clan Data
        clan_data = await get_clan_data(clan.id_array[i])
        clan_data_array.append(clan_data)
        # Get Clan Players and Teams
        clan_players = clan_data['clan']
        # Remove rm Players
        rm_players = clan.account_linkers
        rm_player_ids = [player['brawlhalla_id'] for player in rm_players]
        clan_players = [player for player in clan_players if str(player['brawlhalla_id']) not in rm_player_ids]
        # Get Elo
        clan_player_objects, clan_team_objects = await get_players_elo_1v1_and_2v2(clan, clan_players, clan.clan_names[i], x=x)
        all_player_objects_array.append(clan_player_objects)
        all_team_objects_array.append(clan_team_objects)
    # Restructure Players and Teams
    all_player_objects_array_restructured = __fix_structure(
        all_player_objects_array)
    all_team_objects_array_restructured = __fix_structure(
        all_team_objects_array)
    # Sort Players and Teams
    all_player_objects_array_sorted = sort_elo(
        clan.sorting_method, all_player_objects_array_restructured)
    all_team_objects_array_sorted = sort_elo(
        clan.sorting_method, all_team_objects_array_restructured)
    # Send 1v1 Elo List
    embed_title, embed_array = prepare_embeds_clan_mix_console(
        clan,
        all_player_objects_array_sorted,
        clan_data_array,
        console_player_amount=len(console_players))
    await send_embeds(embed_title, embed_array, bot, clan, clan.channel_1v1_id)
    # Send 2v2 Elo List
    embed_title, embed_array = prepare_embeds_clan_mix_console(
        clan,
        all_team_objects_array_sorted,
        clan_data_array,
        console_player_amount=len(console_players))
    await send_embeds(embed_title, embed_array, bot, clan, clan.channel_2v2_id)


async def clan_console_mix_1v1_and_2v2_and_rotating_elo_list(clan:Clan, bot):
    all_player_objects_array = []
    all_team_objects_array = []
    all_rotating_objects_array = []  # p3
    # Get Console Players
    console_players = clan.console_players
    # p1
    console_player_objects, console_team_objects, console_rotating_objects = await get_players_elo_1v1_and_2v2_and_rotating(clan, console_players, f"{clan.server_name} (Console)", is_console_players=True)
    all_player_objects_array.append(console_player_objects)
    all_team_objects_array.append(console_team_objects)
    all_rotating_objects_array.append(console_rotating_objects)
    # Foreach Clan...
    clan_data_array = []
    for i in range(len(clan.id_array)):
        # Get Clan Data
        clan_data = await get_clan_data(clan.id_array[i])
        clan_data_array.append(clan_data)
        # Get Clan Players, Teams and Rotating
        clan_players = clan_data['clan']
        # Remove rm Players
        rm_players = clan.account_linkers
        rm_player_ids = [player['brawlhalla_id'] for player in rm_players]
        clan_players = [player for player in clan_players if player['brawlhalla_id'] not in rm_player_ids]
        # Get Elo
        # p2
        clan_player_objects, clan_team_objects, clan_rotating_objects = await get_players_elo_1v1_and_2v2_and_rotating(clan, clan_players, clan.clan_names[i])
        all_player_objects_array.append(clan_player_objects)
        all_team_objects_array.append(clan_team_objects)
        all_rotating_objects_array.append(clan_rotating_objects)
    # Restructure Players and Teams
    all_player_objects_array_restructured = __fix_structure(
        all_player_objects_array)
    all_team_objects_array_restructured = __fix_structure(
        all_team_objects_array)
    all_rotating_objects_array_restructured = __fix_structure(
        all_rotating_objects_array)
    # Sort Players and Teams
    all_player_objects_array_sorted = sort_elo(
        clan.sorting_method, all_player_objects_array_restructured)
    all_team_objects_array_sorted = sort_elo(
        clan.sorting_method, all_team_objects_array_restructured)
    all_rotating_objects_array_sorted = sort_elo(
        clan.sorting_method, all_rotating_objects_array_restructured)
    # Send 1v1 Elo List
    embed_title, embed_array = prepare_embeds_clan_mix_console(
        clan,
        all_player_objects_array_sorted,
        clan_data_array,
        console_player_amount=len(console_players))
    await send_embeds(embed_title, embed_array, bot, clan, clan.channel_1v1_id)
    # Send 2v2 Elo List
    embed_title, embed_array = prepare_embeds_clan_mix_console(
        clan,
        all_team_objects_array_sorted,
        clan_data_array,
        console_player_amount=len(console_players))
    await send_embeds(embed_title, embed_array, bot, clan, clan.channel_2v2_id)
    # Send Rotating Elo List
    embed_title, embed_array = prepare_embeds_clan_mix_console(
        clan,
        all_rotating_objects_array_sorted,
        clan_data_array,
        console_player_amount=len(console_players))
    await send_embeds(embed_title, embed_array, bot, clan, clan.channel_rotating_id)

# -------------------------------------------------------------------#
#                               SERVER                              #
# ------------------------------------------------------------------#


async def server_1v1_elo_list(server: Server, bot):
    print("Server 1v1 elo list for " + server.name)
    print(f"Amount of players in {server.name}: {len(server.links)}")
    brawlhalla_nl_players = server.links
    all_player_objects_array, _ = await get_players_elo_1v1_and_2v2(server, brawlhalla_nl_players, server.name)
    all_player_objects_sorted = sort_elo(server.sorting_method, all_player_objects_array)
    embed_title, embed_array = prepare_embeds_server(server, all_player_objects_sorted)
    await send_embeds(embed_title, embed_array, bot, server,server.channel_1v1_id)


async def server_2v2_elo_list(server:Server, bot):
    print("Server 2v2 elo list for " + server.name)
    print(f"Amount of players in {server.name}: {len(server.links)}")
    brawlhalla_nl_players = server.links
    _, all_teams_array = await get_players_elo_1v1_and_2v2(server, brawlhalla_nl_players, server.name)
    all_team_objects_sorted = sort_elo(server.sorting_method, all_teams_array)
    embed_title, embed_array = prepare_embeds_server(server, all_team_objects_sorted)
    await send_embeds(embed_title, embed_array, bot, server, server.channel_2v2_id)


async def server_1v1_and_2v2_elo_list(server:Server, bot):
    print("Server 1v1 and 2v2 elo list for " + server.name)
    print(f"Amount of players in {server.name}: {len(server.links)}")
    brawlhalla_nl_players = server.links
    # Get Elo
    all_players_array, all_teams_array = await get_players_elo_1v1_and_2v2(server, brawlhalla_nl_players, server.name)
    # Sort Elo
    all_players_sorted = sort_elo(server.sorting_method, all_players_array)
    all_teams_sorted = sort_elo(server.sorting_method, all_teams_array)
    # Send 1v1 Elo List
    embed_title, embed_array = prepare_embeds_server(server, all_players_sorted)
    await send_embeds(embed_title, embed_array, bot, server, server.channel_1v1_id)
    # Send 2v2 Elo List
    embed_title, embed_array = prepare_embeds_server(server, all_teams_sorted)
    await send_embeds(embed_title, embed_array, bot, server, server.channel_2v2_id)


async def server_1v1_and_2v2_and_rotating_elo_list(server: Server, bot):
    print("Server 1v1 and 2v2 and rotating elo list for " + server.name)
    print(f"Amount of players in {server.name}: {len(server.links)}")
    server_players = server.links
    # Get Elo
    all_players_array, all_teams_array, all_rotating_array = await get_players_elo_1v1_and_2v2_and_rotating(server, server_players, server.name)
    print('test')
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


# ---------------------------------------------------------------------------#
#                            USEFULL FUNCTIONS                              #
# --------------------------------------------------------------------------#


# def __try_update_data(server):
#     print("updating data...")
#     try:
#         server.update_data()
#     except:
#         print("couldn't update data, make sure Dadabase is running")


def __fix_structure(all_players_array):
    # new structure -> restructured_player_array = [console players + clan1_players + clan2_players + clan3_players]
    restructured_player_array = []
    for player_array in all_players_array:
        for player in player_array:
            restructured_player_array.append(player)
    return restructured_player_array
