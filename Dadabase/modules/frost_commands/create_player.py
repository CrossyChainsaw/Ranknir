from Dadabase.classes.Account import Account
from Dadabase.classes.Server import Server
from Dadabase.modules.data import read_link_data, write_data
from Dadabase.modules.api import fetch_player_stats
import json

DATA_LINKS_LOCATION_SERVER_FROST = 'Dadabase/data/Frost/'
DATA_SINGLE_PLAYER_LOCATION = 'Dadabase/data/Frost/player_stats/'


async def create_player(ctx, brawlhalla_id, nickname):
    print('Entered: create_player()')
    await __create_player(ctx, brawlhalla_id, nickname)
    await __get_player_stats(ctx, brawlhalla_id, nickname)


async def __create_player(ctx, brawlhalla_id, nickname):
    print('Entered: __create_player()')
    player = Account(brawlhalla_id, nickname)
    link_data = read_link_data(DATA_LINKS_LOCATION_SERVER_FROST, ctx.guild.id)
    link_data.append(player.__dict__)
    server = Server(ctx.guild.name, link_data)
    write_data(DATA_LINKS_LOCATION_SERVER_FROST, server.__dict__, ctx.guild.id)
    await ctx.channel.send('Created: ' + brawlhalla_id + ' ' + nickname)


async def __get_player_stats(ctx, brawlhalla_id, nickname):
    stats = fetch_player_stats(brawlhalla_id)
    open(DATA_SINGLE_PLAYER_LOCATION + str(brawlhalla_id) + '.json', 'x')
    with open(DATA_SINGLE_PLAYER_LOCATION + str(brawlhalla_id) + '.json', 'w') as write_file:
        json.dump(stats, write_file)
    await ctx.channel.send('Updated data of ' + nickname)
