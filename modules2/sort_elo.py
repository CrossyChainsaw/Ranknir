from classes.Player import Player


def sort_elo(sorting_method, players):
    players_sorted = []

    while len(players) > 0:
        index = -1
        best_index = 0
        best_rating = -1
        for player in players:
            index += 1
            if sorting_method == "current":
                if player.current > best_rating:
                    best_rating = player.current
                    best_index = index
            elif sorting_method == "peak":
                if player.peak > best_rating:
                    best_rating = player.peak
                    best_index = index
        players_sorted.append(players.pop(best_index))

    return players_sorted
