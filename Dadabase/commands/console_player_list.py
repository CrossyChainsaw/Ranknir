from Dadabase.modules.data_management import read_data, DATA_KEY_FOR_CONSOLE_PLAYERS, CLANS_DATA_LOCATION
from Dadabase.modules.format_embeds import format_embed_list
import discord


async def console_player_list(interaction):
    clan_data = read_data(CLANS_DATA_LOCATION, interaction.guild.id)
    msg = format_embed_list(clan_data, DATA_KEY_FOR_CONSOLE_PLAYERS)
    embed = __create_embed(msg)
    await interaction.response.send_message(embed=embed)


def __create_embed(msg):
    return discord.Embed(title="Console Players", description="The following players will be added to the leaderboard manually. To add another run: `/add_console_player`. To remove one run: `/remove_console_player`\n" + msg, color=0x00ff00)
