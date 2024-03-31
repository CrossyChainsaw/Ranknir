import json
from Dadabase.classes.Account import Account
from Dadabase.modules.ps4.ps4_data import load_data, DATA_LOCATION


async def ps4_add(ctx, bh_id, bh_name):
    if __validate_id(bh_id):
        account = __create_account(bh_id, bh_name)
        data = load_data(ctx.guild.id)
        __add_ps4_player(ctx, account, data)
        await ctx.channel.send(bh_name + ' was added')
    else:
        await ctx.channel.send(str(bh_id) + " is not a valid brawlhalla_id")


def __add_ps4_player(ctx, account, data):
    data['ps4_players'].append(account.__dict__)
    with open(DATA_LOCATION + str(ctx.guild.id) + '.json', 'w') as file:
        json.dump(data, file)


def __create_account(brawlhalla_id, brawlhalla_name):
    account = Account(brawlhalla_id, brawlhalla_name)
    return account

def __validate_id(id):
    if isinstance(id, int):
        return True
    else:
        return False
