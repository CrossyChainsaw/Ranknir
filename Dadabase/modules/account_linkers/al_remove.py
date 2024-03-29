import json
from Dadabase.modules.ps4.ps4_data import load_data, DATA_LOCATION
from Dadabase.modules.account_linkers.al_data import NAME_FOR_REMOVE_PLAYERS

async def rmp_remove(ctx, bh_id):
    data = load_data(ctx.guild.id)
    bh_name = __remove_rm_player(ctx, bh_id, data)
    await ctx.channel.send(bh_name + " was removed")


def __remove_rm_player(ctx, bh_id, data):
    bh_name = ""
    index = 0
    for player in data[NAME_FOR_REMOVE_PLAYERS]:
        if player['brawlhalla_id'] == str(bh_id):
            bh_name = data[NAME_FOR_REMOVE_PLAYERS].pop(index)['brawlhalla_name']
            with open(DATA_LOCATION + str(ctx.guild.id) + '.json', 'w') as file:
                json.dump(data, file)
        index += 1
    return bh_name
