from Dadabase.modules.data_management import read_data, CLANS_DATA_PATH, DATA_KEY_FOR_ACCOUNT_LINKERS
from Dadabase.modules.command import REMOVE_SERVER_PLAYER_COMMAND
from Dadabase.modules.format import format_embed_list
import discord


async def account_linker_list(interaction):
    data = read_data(CLANS_DATA_PATH, interaction.guild.id)
    msg = format_embed_list(data, DATA_KEY_FOR_ACCOUNT_LINKERS)
    embed = __create_embed(msg)
    await interaction.response.send_message(embed=embed)


def __create_embed(msg):
    return discord.Embed(title="Account Linkers", description=f"The following players will be removed from the clan leaderboard, if you wish to make them appear in the leaderboard again, run `{REMOVE_SERVER_PLAYER_COMMAND}`\n" + msg, color=0x00ff00)
