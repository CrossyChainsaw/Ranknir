from Dadabase.modules.data_management import read_data, SERVERS_DATA_PATH, DATA_KEY_FOR_SERVER_LINKS, ADD_SERVER_PLAYER_COMMAND, REMOVE_SERVER_PLAYER_COMMAND
from Dadabase.modules.format import format_embed_list
import discord


async def server_player_list(interaction):
    server_data = read_data(SERVERS_DATA_PATH, interaction.guild.id)
    msg = format_embed_list(server_data, DATA_KEY_FOR_SERVER_LINKS)
    embed = __create_embed(msg)
    await interaction.response.send_message(embed=embed)


def __create_embed(msg):
    return discord.Embed(title="Server Players", description=f"The following players will be added to the leaderboard. To add another run: `{ADD_SERVER_PLAYER_COMMAND}`. To remove one run: `{REMOVE_SERVER_PLAYER_COMMAND}`\n" + msg, color=0x00ff00)
