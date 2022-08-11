import json
import re
import time
from api import fetch_clan, fetch_player_ranked_stats


def get_clan(clan_id):
    try:
        clan = json.loads(fetch_clan(clan_id).content)  # request
    except:
        clan = []
    return clan


def get_clan_members(clan_id):
    clan = get_clan(clan_id)
    try:
        clan_members = clan['clan']

        # test process with only 3 clan members
        # with open('./test_data.json') as f:
        #    clan_members = json.load(f)
    except:
        clan_members = []

    # return values
    return_values = []
    return_values.append(clan_members)
    return_values.append(clan)
    return return_values


def get_members_2v2_elo(clan_id):
    # get clan and clan members
    return_values = get_clan_members(clan_id)
    clan_members = return_values[0]
    clan = return_values[1]

    clan_2v2_teamnames = []
    clan_current_2v2_ratings = []
    clan_peak_2v2_ratings = []

    num = 0
    for player in clan_members:
        num += 1
        try:
            all_my_2v2_teams = json.loads(
                fetch_player_ranked_stats(
                    player["brawlhalla_id"]).content)["2v2"]  # request

            # FIND BEST TEAM CURRENT ELO
            bestCurrentTeam = "bestCurrentTeam is undefined"
            bestCurrent = -1
            bestPeak = -1

            for team in all_my_2v2_teams:
                rating = team["rating"]
                peak = team["peak_rating"]
                if rating > bestCurrent:
                    bestCurrent = rating
                    bestPeak = peak
                    bestCurrentTeam = team["teamname"]

            # ADD ALL VALUES TO ARRAYS
            if bestCurrentTeam.startswith("bestCurrentTeam is undefined"):
                bestCurrent = -1
                bestPeak = -1
                bestCurrentTeam = player["name"]
            print(str(num) + ': ' + bestCurrentTeam)
            print("current: " + str(bestCurrent))
            print("peak: " + str(bestPeak))
            print(' ')
            clan_2v2_teamnames.append(bestCurrentTeam)
            clan_current_2v2_ratings.append(bestCurrent)
            clan_peak_2v2_ratings.append(bestPeak)

        except:
            currentResult = "**" + \
                str(num) + ". " + player["name"] + \
                "**: **current:**" + " -1" + " **peak:**" + " -1"

            clan_2v2_teamnames.append(player["name"])
            clan_current_2v2_ratings.append(-1)
            clan_peak_2v2_ratings.append(-1)

            print(currentResult)
    return_values = []
    return_values.append(clan_2v2_teamnames)
    return_values.append(clan_current_2v2_ratings)
    return_values.append(clan_peak_2v2_ratings)
    return_values.append(clan)
    return return_values
