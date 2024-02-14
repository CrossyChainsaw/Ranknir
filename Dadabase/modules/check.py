from Dadabase.modules.data import read_link_data
from Dadabase.classes.User import User

DATA_LINKS_LOCATION_SERVER_SINGLE_ID = 'data/servers/'


async def check(ctx):
    link_data = read_link_data(
        DATA_LINKS_LOCATION_SERVER_SINGLE_ID, ctx.guild.id)
    user = ''
    for link in link_data:
        if str(ctx.author.id) == str(link['discord_id']):
            user = User(link['brawlhalla_id'], link['brawlhalla_name'],
                        link['discord_id'], link['discord_name'])
            break
    await ctx.channel.send('Currently claimed brawlhalla account \n```brawlhalla_name: ' + user.brawlhalla_name+'\nbrawlhalla_id: '+str(user.brawlhalla_id)+'```')
