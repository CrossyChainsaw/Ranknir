from modules.api import fetch_clan_from_open_api


async def get_clan_data(clan_id):
    clan = await fetch_clan_from_open_api(clan_id)
    print('%s - %s' % (clan['clan_name'], clan_id))
    return clan
