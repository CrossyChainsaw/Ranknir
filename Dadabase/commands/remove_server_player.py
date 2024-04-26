import json
from Dadabase.modules.data_management import read_data, write_data, SERVERS_DATA_PATH

async def remove_server_player(interaction, brawlhalla_id):
    server_id = interaction.guild.id
    brawlhalla_name = ""
    server_data = read_data(SERVERS_DATA_PATH, server_id)
    for index, item in enumerate(server_data['links']):
        if item['brawlhalla_id'] == brawlhalla_id:
            brawlhalla_name = server_data['links'][index]['brawlhalla_name']
            del server_data['links'][index]
            write_data(SERVERS_DATA_PATH, server_data, server_id)
            await interaction.response.send_message(f"Removed brawlhalla account: {brawlhalla_name} (ID: {brawlhalla_id})")
            return
    await interaction.respond.send_message(f"Couldn't find brawlhalla account with ID: {brawlhalla_id}")
    


