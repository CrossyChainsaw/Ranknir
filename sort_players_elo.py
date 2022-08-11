from pickletools import read_unicodestring1
from get_members_2v2_elo import get_members_2v2_elo


def sort_players_elo(clan_id):
    # get 2v2 teams, current and peak elo's
    returned_values = get_members_2v2_elo(clan_id)
    clan_2v2_teamnames = returned_values[0]
    clan_current_2v2_ratings = returned_values[1]
    clan_peak_2v2_ratings = returned_values[2]
    clan = returned_values[3]

    clan_current_2v2_ratings_sorted = []
    clan_peak_2v2_ratings_sorted = []
    clan_2v2_teamnames_sorted = []

    # sort players elo
    print('start sorting players elo...')
    while len(clan_current_2v2_ratings) > 0:
        index = -1
        bestIndex = 0
        highestCurrentRating = -2
        for (current, peak, teamCurrent) in zip(clan_current_2v2_ratings,
                                                clan_peak_2v2_ratings,
                                                clan_2v2_teamnames):
            index += 1
            if current > highestCurrentRating:
                highestCurrentRating = current
                bestIndex = index
        clan_current_2v2_ratings_sorted.append(
            clan_current_2v2_ratings.pop(bestIndex))
        clan_peak_2v2_ratings_sorted.append(
            clan_peak_2v2_ratings.pop(bestIndex))
        clan_2v2_teamnames_sorted.append(clan_2v2_teamnames.pop(bestIndex))
    print('done sorting')

    # Return all values
    return_values = []
    return_values.append(clan_2v2_teamnames_sorted)
    return_values.append(clan_current_2v2_ratings_sorted)
    return_values.append(clan_peak_2v2_ratings_sorted)
    return_values.append(clan)
    return return_values
