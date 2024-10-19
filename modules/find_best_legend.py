def find_best_legend(player_ranked_stats):
    player_legends_data = player_ranked_stats['legends']
    best_legend_rating = -1 # placeholder elo
    best_legend = 'bodvar' # placeholder legend
    for legend_data in player_legends_data:
        if legend_data['rating'] > best_legend_rating:
            best_legend_rating = legend_data['rating']
            best_legend = legend_data['legend_name_key']
    best_legend = best_legend.replace(" ", "")
    return best_legend