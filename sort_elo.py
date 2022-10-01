from get_members_elo import get_members_2v2_elo, get_members_1v1_elo

# todo (should)
# turn sorting elo into method and use single one in both 1v1 and 2v2

def sort_teams_elo(clan_id, sorting_method):
    # get 2v2 teams, current and peak elo's
    returned_values = get_members_2v2_elo(clan_id, sorting_method)
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


def sort_players_elo(clan_id, sorting_method):
  # get all players
  clan_members_name, clan_members_current, clan_members_peak, clan = get_members_1v1_elo(clan_id)
  # mock data for quick testing
  #clan_members_name = ["Crossy", "Sparky", "Glassy"]
  #clan_members_current = [1400, 1679, 1500]
  #clan_members_peak = [3000, 1679, 2800]
  #clan = {"clan_name": "testing", "clan_xp": "over 9000"}
  
  # sort players elo
  clan_members_name_sorted = []
  clan_members_current_sorted = []
  clan_members_peak_sorted = []

  print('start sorting players elo...')
  if sorting_method == "current":
    while len(clan_members_name) > 0:
      index = -1
      bestIndex = 0
      bestCurrent = -1
      for (name, current, peak) in zip(clan_members_name, clan_members_current, clan_members_peak):
        index += 1
        if current > bestCurrent:
          bestCurrent = current
          bestIndex = index
      clan_members_name_sorted.append(clan_members_name.pop(bestIndex))
      clan_members_current_sorted.append(clan_members_current.pop(bestIndex))
      clan_members_peak_sorted.append(clan_members_peak.pop(bestIndex))
      
  elif sorting_method == "peak":
    print("test")
    while len(clan_members_name) > 0:
      index = -1
      bestIndex = 0
      bestPeak = -1
      for (name, current, peak) in zip(clan_members_name, clan_members_current, clan_members_peak):
        index += 1
        print("index: " + str(index))
        print(str(peak) + " > " + str(bestPeak) + "?")
        if peak > bestPeak:
          bestPeak = peak
          print(str(bestPeak))
          bestIndex = index
          print(str(bestIndex))
      clan_members_name_sorted.append(clan_members_name.pop(bestIndex))
      clan_members_current_sorted.append(clan_members_current.pop(bestIndex))
      clan_members_peak_sorted.append(clan_members_peak.pop(bestIndex))
          
  # return values
  return clan_members_name_sorted, clan_members_current_sorted, clan_members_peak_sorted, clan
