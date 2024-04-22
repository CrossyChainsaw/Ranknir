from Dadabase.modules.data_management import read_link_data, SERVERS_DATA_LOCATION
from Dadabase.classes.User import User


async def check(interaction):
    link_data = read_link_data(SERVERS_DATA_LOCATION, interaction.guild.id)
    user = __find_user(interaction, link_data)
    if user is not None:
        if user.country == "":
            user.country = "Not Claimed"
        if user.ethnicity == "":
            user.ethnicity = "Not Claimed"
        await interaction.response.send_message(f"Currently claimed Brawlhalla account:\n```brawlhalla_name: {user.brawlhalla_name}\nbrawlhalla_id: {user.brawlhalla_id}\ncountry_of_residence: {user.country}\nethnicity: {user.ethnicity}```")
    else:
        await interaction.response.send_message("You haven't claimed an account yet, use `/claim` to claim your Brawlhalla account.")

def __find_user(interaction, link_data):
    for link in link_data:
        if str(interaction.user.id) == str(link['discord_id']):
            user = User(link['brawlhalla_id'], link['brawlhalla_name'],link['discord_id'], link['discord_name'], link['country'], link['ethnicity'])
            return user
    else:
        return None