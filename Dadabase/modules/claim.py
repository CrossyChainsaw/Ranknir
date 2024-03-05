import json
from Dadabase.modules.api import fetch_player_ranked_stats
from Dadabase.classes.User import User
from Dadabase.modules.data import read_link_data, write_data, read_data, DATA_LINKS_LOCATION_SERVER_SINGLE_ID
from Dadabase.classes.Server import Server


async def claim(ctx, brawlhalla_id):
    ranked_stats = __request(brawlhalla_id)
    if (ranked_stats):
        condition = __already_claimed(ctx)
        if condition == True:
            print('updating link')
            await __update_link(ctx, ranked_stats)
        else:
            await __add_link(ctx, ranked_stats)
    else:
        await ctx.channel.send("Account with `brawlhalla_id: "+brawlhalla_id+"` does not exist or hasn't played ranked yet")


def __already_claimed(ctx):
    print('Entered: already_claimed()')
    link_data = []
    link_data = read_link_data(
        DATA_LINKS_LOCATION_SERVER_SINGLE_ID, ctx.guild.id)
    for user in link_data:
        if str(ctx.author.id) == str(user['discord_id']):
            return True
    return False

    # check if dc is linked


async def __add_link(ctx, ranked_stats):
    print('Entered: __add_link()')
    brawlhalla_name = __save_link(ctx, ranked_stats)
    await ctx.channel.send("Claimed brawlhalla account: " + brawlhalla_name)


async def __update_link(ctx, ranked_stats):
    print('Entered: __update_link()')
    user = __create_user(ctx, ranked_stats)
    link_data = read_link_data(
        DATA_LINKS_LOCATION_SERVER_SINGLE_ID, ctx.guild.id)
    x = 0
    print('g')
    for link in link_data:
        if ctx.author.id == link['discord_id']:
            break
        x += 1
    print(link_data[x])
    link_data[x]['brawlhalla_id'] = user.brawlhalla_id
    link_data[x]['brawlhalla_name'] = user.brawlhalla_name
    server = Server(ctx.guild.name, ctx.guild.name + " Leaderboard", link_data)
    write_data(DATA_LINKS_LOCATION_SERVER_SINGLE_ID,
               server.__dict__, ctx.guild.id)
    await ctx.channel.send("Updated claimed brawlhalla account to ```brawlhalla_name: "+user.brawlhalla_name+'\nbrawlhalla_id: '+str(user.brawlhalla_id)+'```')


def __request(brawlhalla_id):
    print('Entered: __request()')
    return fetch_player_ranked_stats(brawlhalla_id)


def __save_link(ctx, ranked_stats):
    print('Entered: __save_link()')
    user = __create_user(ctx, ranked_stats)
    __save_data(user, ctx)
    return user.brawlhalla_name


def __create_user(ctx, ranked_stats):
    print('Entered: __create_user()')
    brawlhalla_id = ranked_stats['brawlhalla_id']
    brawlhalla_name = ranked_stats['name']
    discord_id = ctx.author.id
    discord_name = ctx.author.name
    user = User(brawlhalla_id, brawlhalla_name, discord_id, discord_name)
    return user


def __save_data(user, ctx):
    print('Entered: __save_data()')
    link_data = read_link_data(
        DATA_LINKS_LOCATION_SERVER_SINGLE_ID, ctx.guild.id)
    link_data.append(user.__dict__)
    server = Server(ctx.guild.name, ctx.guild.name + " Leaderboard", link_data)
    write_data(DATA_LINKS_LOCATION_SERVER_SINGLE_ID,
               server.__dict__, ctx.guild.id)
