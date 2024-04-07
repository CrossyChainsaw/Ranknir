import json
from Dadabase.modules.api import fetch_player_ranked_stats
from Dadabase.classes.User import User
from Dadabase.modules.data import read_link_data, write_data, read_data, DATA_LINKS_LOCATION_SERVER_SINGLE_ID
from Dadabase.classes.Server import Server


async def claim(interaction, brawlhalla_id):
    print("Entered Claim")
    ranked_stats = __request(brawlhalla_id)
    if (ranked_stats):
        condition = __already_claimed(interaction)
        if condition == True:
            print('updating link')
            await __update_link(interaction, ranked_stats)
        else:
            await __add_link(interaction, ranked_stats)
    else:
        await interaction.response.send_message("Account with `brawlhalla_id: "+brawlhalla_id+"` does not exist or hasn't played ranked yet")


def __already_claimed(interaction):
    print('Entered: already_claimed()')
    link_data = []
    link_data = read_link_data(DATA_LINKS_LOCATION_SERVER_SINGLE_ID, interaction.guild.id)
    for user in link_data:
        if str(interaction.user.id) == str(user['discord_id']):
            return True
    return False

    # check if dc is linked


async def __add_link(interaction, ranked_stats):
    print('Entered: __add_link()')
    brawlhalla_name = __save_link(interaction, ranked_stats)
    await interaction.response.send_message("Claimed brawlhalla account: " + brawlhalla_name)


async def __update_link(interaction, ranked_stats):
    print('Entered: __update_link()')
    user = __create_user(interaction, ranked_stats)
    link_data = read_link_data(
        DATA_LINKS_LOCATION_SERVER_SINGLE_ID, interaction.guild.id)
    x = 0
    print('g')
    for link in link_data:
        if interaction.user.id == link['discord_id']:
            break
        x += 1
    print(link_data[x])
    link_data[x]['brawlhalla_id'] = user.brawlhalla_id
    link_data[x]['brawlhalla_name'] = user.brawlhalla_name
    server = Server(interaction.guild.name, interaction.guild.name + " Leaderboard", link_data)
    write_data(DATA_LINKS_LOCATION_SERVER_SINGLE_ID,
               server.__dict__, interaction.guild.id)
    await interaction.response.send_message("Updated claimed brawlhalla account to ```brawlhalla_name: "+user.brawlhalla_name+'\nbrawlhalla_id: '+str(user.brawlhalla_id)+'```')


def __request(brawlhalla_id):
    print('Entered: __request()')
    return fetch_player_ranked_stats(brawlhalla_id)


def __save_link(interaction, ranked_stats):
    print('Entered: __save_link()')
    user = __create_user(interaction, ranked_stats)
    __save_data(user, interaction)
    return user.brawlhalla_name


def __create_user(interaction, ranked_stats):
    print('Entered: __create_user()')
    brawlhalla_id = ranked_stats['brawlhalla_id']
    brawlhalla_name = ranked_stats['name']
    discord_id = interaction.user.id
    discord_name = interaction.user.name
    user = User(brawlhalla_id, brawlhalla_name, discord_id, discord_name)
    return user


def __save_data(user, interaction):
    print('Entered: __save_data()')
    link_data = read_link_data(
        DATA_LINKS_LOCATION_SERVER_SINGLE_ID, interaction.guild.id)
    link_data.append(user.__dict__)
    server = Server(interaction.guild.name, interaction.guild.name + " Leaderboard", link_data)
    write_data(DATA_LINKS_LOCATION_SERVER_SINGLE_ID,
               server.__dict__, interaction.guild.id)
