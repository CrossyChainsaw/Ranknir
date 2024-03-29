import json
from Dadabase.classes.Account import Account
from Dadabase.modules.ps4.ps4_data import load_data, DATA_LOCATION
from Dadabase.modules.account_linkers.al_data import NAME_FOR_REMOVE_PLAYERS

async def rmp_add(ctx, bh_id, bh_name):
    account = __create_account(bh_id, bh_name)
    data = load_data(ctx.guild.id)
    __add_rmp_player(ctx, account, data)
    await ctx.channel.send(bh_name + ' was added')


def __add_rmp_player(ctx, account, data):
    data[NAME_FOR_REMOVE_PLAYERS].append(account.__dict__)
    with open(DATA_LOCATION + str(ctx.guild.id) + '.json', 'w') as file:
        json.dump(data, file)


def __create_account(brawlhalla_id, brawlhalla_name):
    account = Account(brawlhalla_id, brawlhalla_name)
    return account
