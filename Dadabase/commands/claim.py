import json
from Dadabase.modules.api import fetch_player_ranked_stats
from Dadabase.classes.User import User
from Dadabase.modules.data_management import read_link_data, write_data, read_data, SERVERS_DATA_LOCATION
from Dadabase.classes.Server import Server


async def claim(interaction, brawlhalla_id, country_of_residence, nationality):
    print("Entered Claim")
    ranked_stats = __request(brawlhalla_id)
    if (ranked_stats):
        user = __create_user(interaction, ranked_stats, country_of_residence, nationality)
        condition = __already_claimed(interaction)
        if condition == True:
            print('updating link')
            await __update_link(interaction, user)
        else:
            await __add_link(interaction, user)
    else:
        await interaction.response.send_message("Account with `brawlhalla_id: "+brawlhalla_id+"` does not exist or hasn't played ranked yet")


def __already_claimed(interaction):
    print('Entered: already_claimed()')
    link_data = []
    link_data = read_link_data(SERVERS_DATA_LOCATION, interaction.guild.id)
    for user in link_data:
        if str(interaction.user.id) == str(user['discord_id']):
            return True
    return False

    # check if dc is linked


async def __add_link(interaction, user):
    print('Entered: __add_link()')
    brawlhalla_name = __save_link(interaction, user)
    await interaction.response.send_message("Claimed brawlhalla account: " + brawlhalla_name)


async def __update_link(interaction, user):
    print('Entered: __update_link()')
    link_data = read_link_data(SERVERS_DATA_LOCATION, interaction.guild.id)
    x = 0
    print('g')
    for link in link_data:
        if interaction.user.id == link['discord_id']:
            break
        x += 1
    print(link_data[x])
    link_data[x]['brawlhalla_id'] = user.brawlhalla_id
    link_data[x]['brawlhalla_name'] = user.brawlhalla_name
    link_data[x]['country'] = user.country
    link_data[x]['nationality'] = user.nationality
    server = Server(interaction.guild.name, interaction.guild.name + " Leaderboard", link_data)
    write_data(SERVERS_DATA_LOCATION, server.__dict__, interaction.guild.id)
    await interaction.response.send_message(f"Updated claimed brawlhalla account to ```brawlhalla_name: {user.brawlhalla_name}\nbrawlhalla_id: {user.brawlhalla_id}\ncountry: {user.country}\nnationality: {user.nationality}```"
)


def __request(brawlhalla_id):
    print('Entered: __request()')
    return fetch_player_ranked_stats(brawlhalla_id)


def __save_link(interaction, user):
    print('Entered: __save_link()')
    __save_data(user, interaction)
    return user.brawlhalla_name


def __create_user(interaction, ranked_stats, country_of_residence, nationality):
    print('Entered: __create_user()')
    brawlhalla_id = ranked_stats['brawlhalla_id']
    brawlhalla_name = ranked_stats['name']
    discord_id = interaction.user.id
    discord_name = interaction.user.name
    user = User(brawlhalla_id, brawlhalla_name, discord_id, discord_name, country_of_residence, nationality)
    return user


def __save_data(user, interaction):
    print('Entered: __save_data()')
    link_data = read_link_data(
        SERVERS_DATA_LOCATION, interaction.guild.id)
    link_data.append(user.__dict__)
    server = Server(interaction.guild.name, interaction.guild.name + " Leaderboard", link_data)
    write_data(SERVERS_DATA_LOCATION,
               server.__dict__, interaction.guild.id)
