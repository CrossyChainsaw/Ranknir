async def configure_server(ctx):
    try:
        data_loc = 'servers/'
        __create_data_file(ctx, data_loc)
        __edit_data_file_server(ctx, data_loc)
        await ctx.channel.send('Succes! Created a single id data file for ' + ctx.guild.name)
    except Exception as ex:
        print(ex)
        await ctx.channel.send('Something went wrong...')


def __create_data_file(ctx, loc):
    open('Dadabase/data/' + loc + str(ctx.guild.id) + '.json', 'x')


def __edit_data_file_server(ctx, loc):
    file = open('Dadabase/data/' + loc + str(ctx.guild.id) + '.json', 'a')
    file.write("{\"name\": \"" + ctx.guild.name + "\", \"links\": []}")
