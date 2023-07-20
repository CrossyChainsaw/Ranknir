from modules.get_elo import get_players_elo_1v1, get_players_elo_2v2
from modules.get_players import get_server_players
from modules.sort_elo import sort_elo
from modules.embed import send_embeds, prepare_embeds_clan_mix_console, prepare_embeds_server
from data.server_data import Brawlhalla_NL
from modules.get_players import get_console_players
from modules.clan import get_clan_data


async def clan_console_mix_1v1_elo_list(clan, bot):
    # structure -> all_players_array = [[console_players], [clan1_players], [clan2_players], [clan3_players]]
    all_players_array = []
    # Get Console Players
    console_players = get_console_players(clan.server_id)
    all_players_array.append(get_players_elo_1v1(console_players))
    # Get Clan
    clan_data_array = []
    for clan_id in clan.id_array:
        # Get Clan Data
        clan_data = get_clan_data(clan_id)
        clan_data_array.append(clan_data)
        # Get Clan Players
        clan_players = clan_data['clan']
        all_players_array.append(get_players_elo_1v1(clan_players))
    # Restructure the array with all players
    all_players_array_restructured = __fix_structure(all_players_array)
    all_players_sorted = sort_elo(clan, all_players_array_restructured)
    embed_title, embed_array = prepare_embeds_clan_mix_console(
        clan, all_players_sorted, clan_data_array, console_player_amount=len(console_players))
    await send_embeds(embed_title, embed_array, bot, clan, clan.channel_1v1_id)


async def clan_console_mix_2v2_elo_list(clan, bot):
    # structure -> all_players_array = [[console_players], [clan1_players], [clan2_players], [clan3_players]]
    all_teams_array = []
    # Get Console Players
    console_players = get_console_players(clan.server_id)
    all_teams_array.append(get_players_elo_2v2(clan, console_players))
    # Get Clan
    clan_data_array = []
    for clan_id in clan.id_array:
        # Get Clan Data
        clan_data = get_clan_data(clan_id)
        clan_data_array.append(clan_data)
        # Get Clan Players
        clan_players = clan_data['clan']
        all_teams_array.append(get_players_elo_2v2(clan, clan_players))
    # Restructure the array with all players
    all_teams_array_restructured = __fix_structure(all_teams_array)
    all_teams_sorted = sort_elo(clan, all_teams_array_restructured)
    embed_title, embed_array = prepare_embeds_clan_mix_console(
        clan, all_teams_sorted, clan_data_array, console_player_amount=len(console_players))
    await send_embeds(embed_title, embed_array, bot, clan, clan.channel_2v2_id)


async def clan_console_mix_1v1_and_2v2_elo_list(clan, bot):
    all_players_array = []
    all_teams_array = []

    console_players = get_console_players(clan.server_id)
    all_players_array.append(get_players_elo_1v1(console_players))
    all_teams_array.append(get_players_elo_2v2(clan, console_players))

    clan_data_array = []
    for clan_id in clan.id_array:
        # Get Clan Data
        clan_data = get_clan_data(clan_id)
        clan_data_array.append(clan_data)
        # Get Clan Players
        clan_players = clan_data['clan']
        all_players_array.append(get_players_elo_1v1(clan_players))
        all_teams_array.append(get_players_elo_2v2(clan, clan_players))
    all_players_array_restructured = __fix_structure(all_players_array)
    all_teams_array_restructured = __fix_structure(all_teams_array)

    all_players_sorted = sort_elo(clan, all_players_array_restructured)
    all_teams_sorted = sort_elo(clan, all_teams_array_restructured)

    embed_title, embed_array = prepare_embeds_clan_mix_console(
        clan, all_players_sorted, clan_data_array, console_player_amount=len(console_players))
    await send_embeds(embed_title, embed_array, bot, clan, clan.channel_1v1_id)

    embed_title, embed_array = prepare_embeds_clan_mix_console(
        clan, all_teams_sorted, clan_data_array, console_player_amount=len(console_players))
    await send_embeds(embed_title, embed_array, bot, clan, clan.channel_2v2_id)


async def server_1v1_elo_list(server, bot):
    print("Server 1v1 elo list for " + server.name)
    __try_update_data(server)
    brawlhalla_nl_players = get_server_players(server)
    all_players_array = get_players_elo_1v1(brawlhalla_nl_players)
    all_players_sorted = sort_elo(server, all_players_array)
    embed_title, embed_array = prepare_embeds_server(
        server, all_players_sorted)
    await send_embeds(embed_title, embed_array, bot, server, server.channel_1v1_id)


async def server_2v2_elo_list(server, bot):
    print("Server 2v2 elo list for " + server.name)
    __try_update_data(server)
    brawlhalla_nl_players = get_server_players(server)
    all_teams_array = get_players_elo_2v2(server, brawlhalla_nl_players)
    all_teams_sorted = sort_elo(server, all_teams_array)
    embed_title, embed_array = prepare_embeds_server(server, all_teams_sorted)
    await send_embeds(embed_title, embed_array, bot, server, server.channel_2v2_id)


async def server_1v1_and_2v2_elo_list(server, bot):
    print("Server 1v1 and 2v2 elo list for " + server.name)
    # __try_update_data(server)
    brawlhalla_nl_players = get_server_players(server)

    all_players_array = get_players_elo_1v1(brawlhalla_nl_players)
    all_teams_array = get_players_elo_2v2(server, brawlhalla_nl_players)

    all_players_sorted = sort_elo(server, all_players_array)
    all_teams_sorted = sort_elo(server, all_teams_array)

    embed_title, embed_array = prepare_embeds_server(
        server, all_players_sorted)
    await send_embeds(embed_title, embed_array, bot, server, server.channel_1v1_id)

    embed_title, embed_array = prepare_embeds_server(server, all_teams_sorted)
    await send_embeds(embed_title, embed_array, bot, server, server.channel_2v2_id)


def __try_update_data(server):
    print("updating data...")
    try:
        server.update_data()
    except:
        print("couldn't update data, make sure Dadabase is running")


# move this to get_elo.py?


def __fix_structure(all_players_array):
    # new structure -> restructured_player_array = [console players + clan1_players + clan2_players + clan3_players]
    restructured_player_array = []
    for player_array in all_players_array:
        for player in player_array:
            restructured_player_array.append(player)
    return restructured_player_array
