from get_members_elo import get_members_2v2_elo, get_members_1v1_elo

# todo (should)
# turn sorting elo into method and use single one in both 1v1 and 2v2

def sort_teams_elo(clan_id, sorting_method):
    # get 2v2 teams, current and peak elo's
    clan_2v2_teamnames_old, clan_current_2v2_ratings_old,  clan_peak_2v2_ratings_old, clan = get_members_2v2_elo(clan_id, sorting_method)

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
    return clan_2v2_teamnames_sorted, clan_current_2v2_ratings_sorted, clan_peak_2v2_ratings_sorted, clan


def sort_2v2_elo(clan_id_array, sorting_method):

  # get all values from all clans in the array
  teamnames_all = []
  current_ratings_all = []
  peak_ratings_all = []
  
  for clan_id in clan_id_array:
    # get 2v2 teams, current and peak elo's
    teamnames, current_ratings, peak_ratings, _ = get_members_2v2_elo(clan_id, sorting_method)
      
    while len(teamnames) > 0:
      teamnames_all.append(teamnames.pop(0))
      current_ratings_all.append(current_ratings.pop(0))
      peak_ratings_all.append(peak_ratings.pop(0))
  
  # remove duplicates
  print('removing duplicate values...')

  teamnames_new = []
  current_ratings_new = []
  peak_ratings_new = []

  for (team_name, current, peak) in zip(teamnames_all, current_ratings_all, peak_ratings_all):
    if team_name not in teamnames_new:
      teamnames_new.append(team_name)
      current_ratings_new.append(current)
      peak_ratings_new.append(peak)

  # sort players elo
  current_ratings_sorted = []
  peak_ratings_sorted = []
  teamnames_sorted = []

  print('start sorting players elo...')
  if sorting_method == "current":
        while len(current_ratings_sorted) > 0:
            index = -1
            bestIndex = 0
            highestCurrentRating = -2
            for (current, peak, teamCurrent) in zip(current_ratings_new, peak_ratings_new, teamnames_new):
                index += 1
                if current > highestCurrentRating:
                    highestCurrentRating = current
                    bestIndex = index
            current_ratings_sorted.append(current_ratings_new.pop(bestIndex))
            peak_ratings_sorted.append(peak_ratings_new.pop(bestIndex))
            teamnames_sorted.append(teamnames_new.pop(bestIndex))

  if sorting_method == "peak":
        while len(current_ratings_new) > 0:
            index = -1
            bestIndex = 0
            highestCurrentRating = -2
            for (current, peak,
                 teamCurrent) in zip(current_ratings_new, peak_ratings_new, teamnames_new):
                index += 1
                if peak > highestCurrentRating:
                    highestCurrentRating = peak
                    bestIndex = index
            current_ratings_sorted.append(current_ratings_new.pop(bestIndex))
            peak_ratings_sorted.append(peak_ratings_new.pop(bestIndex))
            teamnames_sorted.append(teamnames_new.pop(bestIndex))
  print('done sorting')
  
  # Return all values
  return teamnames_sorted, current_ratings_sorted, peak_ratings_sorted


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





def sort_players_elo_multi(clan_id_1, clan_id_2, sorting_method):
  
  # get all players
  print("getting clan 1")
  clan_members_name_1, clan_members_current_1, clan_members_peak_1, clan = get_members_1v1_elo(clan_id_1)
  print("getting clan 2")
  clan_members_name_2, clan_members_current_2, clan_members_peak_2, clan_dont_care = get_members_1v1_elo(clan_id_2)

  clan_members_name = []
  clan_members_current = []
  clan_members_peak = []
  
  while len(clan_members_name_1) > 0:
    clan_members_name.append(clan_members_name_1.pop(0))
    clan_members_current.append(clan_members_current_1.pop(0))
    clan_members_peak.append(clan_members_peak_1.pop(0))

  while len(clan_members_name_2) > 0:
    clan_members_name.append(clan_members_name_2.pop(0))
    clan_members_current.append(clan_members_current_2.pop(0))
    clan_members_peak.append(clan_members_peak_2.pop(0))
  
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
  return clan_members_name_sorted, clan_members_current_sorted, clan_members_peak_sorted, clan, clan_dont_care

def sort_elo_1v1(clan_id_array, sorting_method):

  # get all values from all clans in the array
  player_names_all = []
  current_ratings_all = []
  peak_ratings_all = []
  
  count=0
  for clan_id in clan_id_array:
    player_names, current_ratings, peak_ratings, clan = get_members_1v1_elo(clan_id_array[count])
    
    while len(player_names) > 0:
      player_names_all.append(player_names.pop(0))
      current_ratings_all.append(current_ratings.pop(0))
      peak_ratings_all.append(peak_ratings.pop(0))
    count+=1

  # sort players elo
  player_names_sorted = []
  current_ratings_sorted = []
  peak_ratings_sorted = []

  print('start sorting players elo...')   
  while len(player_names_all) > 0:
    index = -1
    best_index = 0
    best_rating = -1
    for (name, current, peak) in zip(player_names_all, current_ratings_all, peak_ratings_all):
      index += 1
      if sorting_method == "current":
        if current > best_rating:
          best_rating = current
          best_index = index
      elif sorting_method == "peak":
        if peak > best_rating:
          best_rating = peak
          best_index = index
    player_names_sorted.append(player_names_all.pop(best_index))
    current_ratings_sorted.append(current_ratings_all.pop(best_index))
    peak_ratings_sorted.append(peak_ratings_all.pop(best_index))

    print("6")
    print(player_names_sorted)
    
  # return values
  return player_names_sorted, current_ratings_sorted, peak_ratings_sorted
def sort_teams_elo_multi(clan_id_array, sorting_method):
  print("clan_id_1: " + str(clan_id_1))
  print("clan_id_2: " + str(clan_id_2))
  
  # get 2v2 teams, current and peak elo's
  clan_2v2_teamnames_1, clan_current_2v2_ratings_1, clan_peak_2v2_ratings_1, clan = get_members_2v2_elo(clan_id_1, sorting_method)

  print('all teamnames for clan 1')
  for player in clan_2v2_teamnames_1:
    print(player)
  
  clan_2v2_teamnames_2, clan_current_2v2_ratings_2, clan_peak_2v2_ratings_2, clan_dont_care = get_members_2v2_elo(clan_id_2, sorting_method)

  print('all teamnames for clan 2')
  for player in clan_2v2_teamnames_2:
    print(player)

  print("clan_teamnames_1: " + str(len(clan_2v2_teamnames_1)))
  print("clan_teamnames_2: " + str(len(clan_2v2_teamnames_2)))

  # Add both clan arrays together
  clan_2v2_teamnames_old = []
  clan_current_2v2_ratings_old = []
  clan_peak_2v2_ratings_old =[]
  
  while len(clan_2v2_teamnames_1) > 0:
    clan_2v2_teamnames_old.append(clan_2v2_teamnames_1.pop(0))
    clan_current_2v2_ratings_old.append(clan_current_2v2_ratings_1.pop(0))
    clan_peak_2v2_ratings_old.append(clan_peak_2v2_ratings_1.pop(0))

  print('start popping clan 2 names')
  print('currently: ' + str(len(clan_2v2_teamnames_2)))
  while len(clan_2v2_teamnames_2) > 0:
    clan_2v2_teamnames_old.append(clan_2v2_teamnames_2.pop(0))
    clan_current_2v2_ratings_old.append(clan_current_2v2_ratings_2.pop(0))
    clan_peak_2v2_ratings_old.append(clan_peak_2v2_ratings_2.pop(0))

  print(clan_2v2_teamnames_old)
  print(clan_current_2v2_ratings_old)
  print(clan_peak_2v2_ratings_old)
  
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
  return clan_2v2_teamnames_sorted, clan_current_2v2_ratings_sorted, clan_peak_2v2_ratings_sorted, clan, clan_dont_care
  