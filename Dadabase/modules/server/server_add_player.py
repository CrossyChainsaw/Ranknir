import json
from Dadabase.modules.api import fetch_player_ranked_stats
from Dadabase.classes.User import User
from Dadabase.modules.data import read_link_data, write_data, read_data, SERVERS_DATA_LOCATION
from Dadabase.classes.Server import Server

def __structure_option_if_empty(option):
    try:
        print(option.value)
        return option.value
    except:
        return "NL"

async def server_add_player(interaction, brawlhalla_id, discord_id, discord_name, country_of_residence, nationality):
    country_of_residence = __structure_option_if_empty(country_of_residence)
    nationality = __structure_option_if_empty(nationality)
    ranked_stats = __request(brawlhalla_id)
    if (ranked_stats):
        user = __create_user(interaction, ranked_stats, discord_id, discord_name, country_of_residence, nationality)
        condition = __already_claimed(interaction, user.discord_id)
        if condition == True:
            await __update_link(interaction, user)
        else:
            await __add_link(interaction, user)
    else:
        await interaction.response.send_message("Account with `brawlhalla_id: "+brawlhalla_id+"` does not exist or hasn't played ranked yet")


def __already_claimed(interaction, discord_id):
    print('Entered: already_claimed()')
    link_data = []
    link_data = read_link_data(SERVERS_DATA_LOCATION, interaction.guild.id)
    for user in link_data:
        if discord_id == str(user['discord_id']):
            return True
    return False


async def __add_link(interaction, user):
    print('Entered: __add_link()')
    __save_link(interaction, user)
    await interaction.response.send_message(f"Added brawlhalla account: {user.brawlhalla_name} (ID: {user.brawlhalla_id})")
    


async def __update_link(interaction, user):
    print('Entered: __update_link()')
    link_data = read_link_data(SERVERS_DATA_LOCATION, interaction.guild.id)
    x = 0
    print('g')
    for link in link_data:
        if user.discord_id == link['discord_id']:
            break
        x += 1
    print(link_data[x])
    link_data[x]['brawlhalla_id'] = user.brawlhalla_id
    link_data[x]['brawlhalla_name'] = user.brawlhalla_name
    server = Server(interaction.guild.name, interaction.guild.name + " Leaderboard", link_data)
    write_data(SERVERS_DATA_LOCATION,server.__dict__, interaction.guild.id)
    await interaction.response.send_message("Updated brawlhalla account to ```brawlhalla_name: "+user.brawlhalla_name+'\nbrawlhalla_id: '+str(user.brawlhalla_id)+'```')


def __request(brawlhalla_id):
    print('Entered: __request()')
    return fetch_player_ranked_stats(brawlhalla_id)


def __save_link(interaction, user):
    print('Entered: __save_link()')
    __save_data(user, interaction)
    return user.brawlhalla_name


def __create_user(interaction, ranked_stats, discord_id, discord_name, country_of_residence, nationality):
    print('Entered: __create_user()')
    brawlhalla_id = ranked_stats['brawlhalla_id']
    brawlhalla_name = ranked_stats['name']
    user = User(brawlhalla_id, brawlhalla_name, discord_id, discord_name, country_of_residence, nationality)
    return user


def __save_data(user, interaction):
    print('Entered: __save_data()')
    link_data = read_link_data(SERVERS_DATA_LOCATION, interaction.guild.id)
    link_data.append(user.__dict__)
    server = Server(interaction.guild.name, interaction.guild.name + " Leaderboard", link_data)
    print(user)
    print(server)
    write_data(SERVERS_DATA_LOCATION, server.__dict__, interaction.guild.id)
