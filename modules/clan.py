from modules.api import fetch_clan

def get_clan(clan_id):
    try:
        clan = fetch_clan(clan_id)  # request
    except:
        clan = []
        print("couldn't fetch clan data of clan " + str(clan_id))
    return clan

def get_clans(clan_id_array):
  clans = []
  for clan_id in clan_id_array:
    clans.append(get_clan(clan_id))
  return clans

def get_clan_members(clan_id):
    clan = get_clan(clan_id)
    try:
        clan_members = clan['clan']
    except:
        print("ERROR: couldn't get clan members, returned empty array")
        clan_members = []
    return clan_members, clan

