from Ranknir.modules.api import fetch_clan


async def get_clan_data(clan_id):
    clan = await fetch_clan(clan_id)
    print('%s - %s' % (clan['clan_name'], clan_id))
    return clan
