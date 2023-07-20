from modules.api import fetch_clan


def get_clan_data(clan_id):
    clan = fetch_clan(clan_id)
    print(clan['clan_name'])
    return clan
