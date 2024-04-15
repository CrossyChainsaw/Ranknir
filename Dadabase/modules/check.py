from Dadabase.modules.data import read_link_data, SERVERS_DATA_LOCATION
from Dadabase.classes.User import User


async def check(interaction):
    link_data = read_link_data(
        SERVERS_DATA_LOCATION, interaction.guild.id)
    user = ''
    for link in link_data:
        if str(interaction.user.id) == str(link['discord_id']):
            user = User(link['brawlhalla_id'], link['brawlhalla_name'],link['discord_id'], link['discord_name'], link['country'], link['nationality'])
            break
    await interaction.response.send_message('Currently claimed brawlhalla account \n```brawlhalla_name: ' + user.brawlhalla_name+'\nbrawlhalla_id: '+str(user.brawlhalla_id)+'```')
