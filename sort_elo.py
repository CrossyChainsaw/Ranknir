from get_members_elo import get_members_2v2_elo, get_members_1v1_elo

# todo (should)
# turn sorting elo into method and use single one in both 1v1 and 2v2

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

  