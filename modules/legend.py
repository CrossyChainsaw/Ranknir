from modules.api import fetch_player_ranked_stats

def get_best_legend_elo(ps4_players, sorting_method):
  players_name = []
  players_current = []
  players_peak = []  
  players_legend = []

  for ps4_player in ps4_players:
    player = fetch_player_ranked_stats(ps4_player["brawlhalla_id"])
    legends = player['legends']
    best_legend_rating = -1
    best_legend_peak = -1
    for legend in legends: 
      if sorting_method == 'current':
        if legend['rating'] > best_legend_rating:
          player_name = player['name'].encode("charmap").decode()
          best_legend_rating = legend['rating']
          best_legend_peak = legend['peak_rating']
          best_legend_name = legend['legend_name_key'].encode("charmap").decode()
      elif sorting_method == 'peak':
        if legend['peak_rating'] > best_legend_peak:
          player_name = player['name'].encode("charmap").decode()
          best_legend_rating = legend['rating']
          best_legend_peak = legend['peak_rating']
          best_legend_name = legend['legend_name_key'].encode("charmap").decode()

    players_name.append(player_name)
    players_current.append(best_legend_rating)
    players_peak.append(best_legend_peak)
    players_legend.append(best_legend_name)

    print('name: ' + player_name)
    print('current: ' + str(best_legend_rating))
    print('peak: ' + str(best_legend_peak))
    print('legend: ' + best_legend_name)

  #return players_name, players_current, players_peak, players_legend
  return players_name, players_current, players_peak
    
      