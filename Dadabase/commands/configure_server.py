import json

async def configure_server(interaction):
    try:
        data_loc = 'servers/'
        __create_data_file(interaction, data_loc)
        __edit_data_file(interaction, data_loc)
        await interaction.response.send_message('Succes! Created a single id data file for ' + interaction.guild.name)
    except Exception as ex:
        print(ex)
        await interaction.response.send_message('Something went wrong...')


def __create_data_file(interaction, loc):
    open('Dadabase/data/' + loc + str(interaction.guild.id) + '.json', 'x')


def __edit_data_file(interaction, loc):
    file_path = 'Dadabase/data/' + loc + str(interaction.guild.id) + '.json'
    with open(file_path, 'a') as file:
        guild_data = {
            "name": interaction.guild.name,
            "title": interaction.guild.name + " Leaderboard",
            "links": []
        }
        file.write(json.dumps(guild_data, indent=4))
