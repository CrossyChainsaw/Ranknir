import json

async def configure_clan(interaction):
    try:
        __create_data_file(interaction)
        __edit_data_file(interaction)
        await interaction.response.send_message('Succes!')
    except:
        await interaction.response.send_message('Something went wrong...')


def __create_data_file(interaction):
    open('Dadabase/data/clans/' + str(interaction.guild.id) + '.json', 'x')
    
    
def __edit_data_file(ctx):
    file = open('Dadabase/data/clans/' + str(ctx.guild.id) + '.json', 'a')
    file.write(json.dumps({
            "name": ctx.guild.name,
            "id": str(ctx.guild.id),
            "ps4_players": [],
            "al_players": []
        }))
