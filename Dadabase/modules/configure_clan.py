import json

async def configure_clan(ctx):
    try:
        __create_data_file(ctx)
        __edit_data_file(ctx)
        await ctx.channel.send('Succes!')
    except:
        await ctx.channel.send('Something went wrong...')


def __create_data_file(ctx):
    open('Dadabase/data/clans/' + str(ctx.guild.id) + '.json', 'x')
    
    
def __edit_data_file(ctx):
    file = open('Dadabase/data/clans/' + str(ctx.guild.id) + '.json', 'a')
    file.write(json.dumps({
            "name": ctx.guild.name,
            "id": str(ctx.guild.id),
            "ps4_players": [],
            "al_players": []
        }))
