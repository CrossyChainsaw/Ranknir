from classes.Player import Player
from classes.Team import Team
from modules.api import fetch_player_ranked_stats
from modules.get_players import get_console_players, get_server_players
from modules.clan import get_clan_data

# There are different functions for 1v1, 2v2 and 1v1&2v2. I made an extra one for 1v1&2v2 because it halves the api requests.


async def get_players_elo_1v1(clan, players):
    player_object_array = []
    for player in players:
        player_ranked_stats = await fetch_player_ranked_stats(player['brawlhalla_id'])
        player_object = __extract_player_stats_into_player_object_1v1(
            player_ranked_stats)
        if __check_if_name_is_blank(clan, player_object):
            continue
        player_object_array.append(player_object)
    return player_object_array


async def get_players_elo_2v2(clan, players):

    team_object_array = []
    for player in players:
        player_ranked_stats = await fetch_player_ranked_stats(
            player['brawlhalla_id'])
        team_object = __extract_player_stats_into_team_object_2v2(
            clan, player_ranked_stats)
        if __check_if_name_is_blank(clan, team_object):
            continue
        team_object_array.append(team_object)
        print(team_object.name, team_object.current, team_object.peak)
    return team_object_array

# maybe use this function always and leave out 1s or 2s if not wanted, configure if wanted or not in clan_data.py. so you don't have to change everything here and in 1v1 and in 2v2


async def get_players_elo_1v1_and_2v2(clan, players):
    player_object_array = []
    team_object_array = []
    for player in players:
        player_ranked_stats = await fetch_player_ranked_stats(
            player['brawlhalla_id'])
        player_object = __extract_player_stats_into_player_object_1v1(
            player_ranked_stats)
        team_object = __extract_player_stats_into_team_object_2v2(
            clan, player_ranked_stats)
        if __check_if_name_is_blank(clan, player_object) and __check_if_name_is_blank(clan, team_object):
            continue
        player_object_array.append(player_object)
        team_object_array.append(team_object)
        print('1s: ' + player_object.name)
        print('2s: ' + team_object.name)
    return player_object_array, team_object_array


def __extract_player_stats_into_player_object_1v1(player):
    player_object = Player(
        player['name'], player['rating'], player['peak_rating'])
    player_object.name = __give_empty_name_a_placeholder_name(
        player_object.name)
    return player_object


def __extract_player_stats_into_team_object_2v2(clan, player):
    team_object = __find_best_team(clan, player)
    team_object.name = __format_teamname(team_object.name)
    team_object.name = __give_empty_name_a_placeholder_name(team_object.name)
    return team_object


def __format_teamname(best_team):
    if '+' in best_team:
        name_plus = best_team.find('+')
        name_length = len(best_team)
        name_1 = best_team[0:name_plus]
        name_2 = best_team[name_plus+1:name_length]
        new_name = name_1 + '** + **' + name_2
        return new_name
    else:
        return best_team


def __find_best_team(clan, player):
    all_my_2v2_teams = player['2v2']
    best_team = player["name"].encode("charmap").decode()
    best_current = 0
    best_peak = 0
    # Find best team
    if clan.sorting_method == "current":
        # FIND BEST TEAM CURRENT ELO
        for team in all_my_2v2_teams:
            rating = team["rating"]
            peak = team["peak_rating"]
            if rating > best_current:
                best_current = rating
                best_peak = peak
                best_team = team["teamname"].encode("charmap").decode()

    elif clan.sorting_method == "peak":
        # FIND BEST TEAM PEAK ELO
        for team in all_my_2v2_teams:
            rating = team["rating"]
            peak = team["peak_rating"]
            if peak > best_peak:
                best_current = rating
                best_peak = peak
                best_team = team["teamname"].encode("charmap").decode()
    return Team(best_team, best_current, best_peak)


def __give_empty_name_a_placeholder_name(player_name):
    if (player_name) == "":
        return 'N/A'
    else:
        return player_name


def __check_if_elo_is_zero(clan, player_object):
    if clan.no_elo_players == 'hide':
        if player_object.current == 0 and player_object.peak == 0:
            return True
    else:
        return False


def __check_if_name_is_blank(clan, player_object):
    if clan.no_elo_players == 'hide':
        if player_object.name == 'N/A' or player_object.name == "":
            return True
    else:
        return False
