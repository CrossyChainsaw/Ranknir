from Dadabase.classes.Clan import Clan
from Ranknir.classes.Player import Player
from Ranknir.classes.Team import Team
from Ranknir.modules.api import fetch_player_ranked_stats


# There are different functions for 1v1, 2v2 and 1v1&2v2. I made an extra one for 1v1&2v2 because it halves the api requests.

#################### GET ALL PLAYERS ELO ######################

# maybe use this function always and leave out 1s or 2s if not wanted, configure if wanted or not in clan_data.py. so you don't have to change everything here and in 1v1 and in 2v2
async def get_players_elo_1v1_and_2v2(clan, players, subclan_name, is_console_players=False):
    """Gets the personal elo and best-team for each player and `returns` an array of `Player` objects and `Team` objects"""
    player_object_array = []
    team_object_array = []
    for i, player in enumerate(players):
        player_ranked_stats = await fetch_player_ranked_stats(player['brawlhalla_id'])
        player_object = __extract_player_stats_into_player_object_1v1(player_ranked_stats, player)
        team_object = __extract_player_stats_into_team_object_2v2(clan, player_ranked_stats, player)
        if __check_if_name_is_blank(clan, player_object) or __check_if_name_is_blank(clan, team_object):
            if is_console_players: # fix console players' blank names
                if __check_if_name_is_blank(clan, player_object):
                    player_object.name = player['brawlhalla_name']
                if __check_if_name_is_blank(clan, team_object):
                    team_object.name = player['brawlhalla_name']
        player_object_array.append(player_object)
        team_object_array.append(team_object)
        print('%s %s/%s' % (subclan_name, str(i + 1), str(len(players))))
        print('1s: ' + player_object.name)
        print('2s: ' + team_object.name)
    return player_object_array, team_object_array


async def get_players_elo_1v1_and_2v2_and_rotating(clan, players, subclan_name):
    """Gets the personal elo, best-team and rotating ranked elo for each player and `returns` an array of `Player` objects, `Team` objects and `Player` (Rotating Ranked) objects"""
    player_object_array = []
    team_object_array = []
    rotating_object_array = []
    for i, player in enumerate(players):
        player_ranked_stats = await fetch_player_ranked_stats(player['brawlhalla_id'])
        player_object = __extract_player_stats_into_player_object_1v1(player_ranked_stats, player)
        team_object = __extract_player_stats_into_team_object_2v2(clan, player_ranked_stats, player)
        rotating_object = __extract_player_stats_into_player_object_rotating(player_ranked_stats, player)
        if __check_if_name_is_blank(clan, player_object) and __check_if_name_is_blank(clan, team_object) and __check_if_name_is_blank(clan, rotating_object):
            _ = None  # some bs code for no crash
            # continue # uncomment for hide elo players
        player_object_array.append(player_object)
        team_object_array.append(team_object)
        rotating_object_array.append(rotating_object)
        print(f'{subclan_name} {i+1}/{len(players)}')
        print('1s: ' + player_object.name)
        print('2s: ' + team_object.name)
        print('rr: ' + rotating_object.name)
    return player_object_array, team_object_array, rotating_object_array


###################### PUT PLAYER DATA IN PYTHON OBJECTS #######################


def __extract_player_stats_into_player_object_1v1(player_ranked_stats, player:Player):
    """Takes player data and turns it into a `Player` object"""
    # print('Entered: __extract_player_stats_into_player_object_1v1()')
    player_object = Player(name=player_ranked_stats['name'], 
                           current=player_ranked_stats['rating'],
                           peak=player_ranked_stats['peak_rating'],
                           region=player.get('region'),
                           country=player.get('country'),
                           ethnicity=player.get('ethnicity'))
    player_object.name = __fill_in_empty_name(player_object.name, player)
    player_object.name = __try_decode(player_object.name)
    return player_object


def __extract_player_stats_into_team_object_2v2(clan, player_ranked_stats, player):
    """Takes player data and turns it into a `Team` object"""
    # print('Entered: __extract_player_stats_into_team_object_2v2()')
    team_object = __find_best_team(clan, player_ranked_stats, player)
    team_object.name = __format_teamname(player_ranked_stats, team_object)
    team_object.name = __fill_in_empty_name(team_object.name, player_ranked_stats)
    team_object.name = __try_decode(team_object.name)
    return team_object


def __extract_player_stats_into_player_object_rotating(player_ranked_stats, player):
    """Takes player data and turns it into a `Player` object (Rotating Ranked)"""
    # print('Entered: __extract_player_stats_into_player_object_rotating()')
    rotating_stats = player_ranked_stats['rotating_ranked']
    if rotating_stats == []:
        name = ""
        rating = 0
        peak = 0
    else:
        name = rotating_stats['name']
        rating = rotating_stats['rating']
        peak = rotating_stats['peak_rating']
    rotating_object = Player(name, rating, peak, 
                             region=player.get('region'),
                             country=player.get('country'),
                             ethnicity=player.get('ethnicity'))
    rotating_object.name = __fill_in_empty_name(rotating_object.name, player_ranked_stats)
    rotating_object.name = __try_decode(rotating_object.name)
    return rotating_object


############################ USEFUL FUNCTIONS #########################


# testse
def __try_decode(name):
    """Tries to decode unicode symbols"""
    # print('Entered: __try_decode()')
    try:
        new_name = name.encode("charmap").decode()
        return new_name
    except:
        return name


def __change_order_team_name(team_object:Team):
    best_team_name = team_object.name
    if '+' in best_team_name:
        name_plus_index = best_team_name.find('+')
        team_name_length = len(best_team_name)
        name_1 = best_team_name[0:name_plus_index]
        name_2 = best_team_name[name_plus_index + 1:team_name_length]
        new_best_team_name = name_2 + '+' + name_1
        team_object.name = new_best_team_name
        return team_object
    else:
        return team_object


def __format_teamname(player:Player, team_object:Team):
    """Puts 2 asterisks after name 1, and 2 asterisks before name 2. Necessary for making the names bold when sending the embed (consider putting this in embed.py)"""
    best_team_name = team_object.name
    if '+' in best_team_name:
        name_plus_index = best_team_name.find('+')
        name_length = len(best_team_name)
        name_1 = best_team_name[0:name_plus_index]
        name_2 = best_team_name[name_plus_index + 1:name_length]
        new_name = name_1 + '** + **' + name_2
        return new_name
    else:
        return best_team_name


def __check_order_team_name(player, brawl_id_one, brawl_id_two, team_obj):
    if player["brawlhalla_id"] == brawl_id_one:
        return team_obj
    else:
        return __change_order_team_name(team_obj)


def __find_best_team(clan:Clan, player_ranked_stats, player):
    """Finds the best team of the player using `sorting_method` and returns a `Team` object"""
    all_my_2v2_teams = player_ranked_stats['2v2']
    best_team = None
    best_team_name = player_ranked_stats["name"]
    brawl_id_one = player_ranked_stats["brawlhalla_id"]
    brawl_id_two = 0
    best_current = 0
    best_peak = 0
    # Find best team
    if clan.sorting_method == "current":
        # FIND BEST TEAM CURRENT ELO
        for team in all_my_2v2_teams:
            rating = team["rating"]
            if rating > best_current:
                best_team = team
                best_current = rating
    elif clan.sorting_method == "peak":
        # FIND BEST TEAM PEAK ELO
        for team in all_my_2v2_teams:
            peak = team["peak_rating"]
            if peak > best_peak:
                best_team = team
                best_peak = peak

    # format name
    if best_team != None:
        best_team_name = best_team["teamname"]
        best_current = best_team["rating"]
        best_peak = best_team["peak_rating"]
        brawl_id_one = best_team["brawlhalla_id_one"]
        brawl_id_two = best_team["brawlhalla_id_two"]

    team_obj = Team(best_team_name, best_current, best_peak, 
                        region=player.get('region'),
                        country=player.get('country'),
                        ethnicity=player.get('ethnicity'))
    team_obj = __check_order_team_name(player_ranked_stats, brawl_id_one, brawl_id_two,
                                       team_obj)

    return team_obj


def __fill_in_empty_name(player_name, player):
    # print('Entered: __give_empty_name_a_placeholder_name()')
    if player_name == "":
        player_name = __try_get_discord_name(player, player_name)
    if player_name == "":
        return 'N/A'
    else:
        return player_name
    
def __try_get_discord_name(player, player_name):
    if "discord_name" in player:
        return player["discord_name"]
    else:
        return player_name



def __check_if_elo_is_zero(clan:Clan, player_object:Player):
    if clan.show_no_elo_players == True:
        if player_object.current == 0 and player_object.peak == 0:
            return True
    else:
        return False


def __check_if_name_is_blank(clan:Clan, player_object:Player):
    # if you wanna add the thing for, if clan configs "dont show no elo players" etc etc put another if checking that
    if player_object.name == 'N/A' or player_object.name == "":
        return True
    else:
        return False
