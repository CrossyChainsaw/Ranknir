from get_members_2v2_elo import get_members_2v2_elo


def sort_players_elo(clan_id, sorting_method):
    # get 2v2 teams, current and peak elo's
    returned_values = get_members_2v2_elo(clan_id)
    clan_2v2_teamnames_old = returned_values[0]
    clan_current_2v2_ratings_old = returned_values[1]
    clan_peak_2v2_ratings_old = returned_values[2]
    clan = returned_values[3]

    # remove duplicates
    print('removing duplicate values...')

    clan_2v2_teamnames_new = []
    clan_current_2v2_ratings_new = []
    clan_peak_2v2_ratings_new = []

    for (current, peak, team_name) in zip(clan_current_2v2_ratings_old,
                                          clan_peak_2v2_ratings_old,
                                          clan_2v2_teamnames_old):
        if team_name not in clan_2v2_teamnames_new:
            clan_2v2_teamnames_new.append(team_name)
            clan_current_2v2_ratings_new.append(current)
            clan_peak_2v2_ratings_new.append(peak)

    # sort players elo
    clan_current_2v2_ratings_sorted = []
    clan_peak_2v2_ratings_sorted = []
    clan_2v2_teamnames_sorted = []

    print('start sorting players elo...')
    if sorting_method == "current":
        while len(clan_current_2v2_ratings_new) > 0:
            index = -1
            bestIndex = 0
            highestCurrentRating = -2
            for (current, peak,
                 teamCurrent) in zip(clan_current_2v2_ratings_new,
                                     clan_peak_2v2_ratings_new,
                                     clan_2v2_teamnames_new):
                index += 1
                if current > highestCurrentRating:
                    highestCurrentRating = current
                    bestIndex = index
            clan_current_2v2_ratings_sorted.append(
                clan_current_2v2_ratings_new.pop(bestIndex))
            clan_peak_2v2_ratings_sorted.append(
                clan_peak_2v2_ratings_new.pop(bestIndex))
            clan_2v2_teamnames_sorted.append(
                clan_2v2_teamnames_new.pop(bestIndex))

    if sorting_method == "peak":
        while len(clan_current_2v2_ratings_new) > 0:
            index = -1
            bestIndex = 0
            highestCurrentRating = -2
            for (current, peak,
                 teamCurrent) in zip(clan_current_2v2_ratings_new,
                                     clan_peak_2v2_ratings_new,
                                     clan_2v2_teamnames_new):
                index += 1
                if peak > highestCurrentRating:
                    highestCurrentRating = peak
                    bestIndex = index
            clan_current_2v2_ratings_sorted.append(
                clan_current_2v2_ratings_new.pop(bestIndex))
            clan_peak_2v2_ratings_sorted.append(
                clan_peak_2v2_ratings_new.pop(bestIndex))
            clan_2v2_teamnames_sorted.append(
                clan_2v2_teamnames_new.pop(bestIndex))
    print('done sorting')
    # Return all values
    return_values = []
    return_values.append(clan_2v2_teamnames_sorted)
    return_values.append(clan_current_2v2_ratings_sorted)
    return_values.append(clan_peak_2v2_ratings_sorted)
    return_values.append(clan)
    return return_values
