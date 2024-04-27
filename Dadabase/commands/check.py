from Dadabase.modules.data_management import codeblock_with_link_data, find_link, read_link_data, SERVERS_DATA_PATH
from Dadabase.classes.Link import Link


async def check(interaction):
    link_data = read_link_data(SERVERS_DATA_PATH, interaction.guild.id)
    user = find_link(interaction.user.id, link_data)
    if user:
        await interaction.response.send_message(f"Currently claimed Brawlhalla account {codeblock_with_link_data(user)}")
    else:
        await interaction.response.send_message("You haven't claimed an account yet, use `/claim` to claim your Brawlhalla account.")