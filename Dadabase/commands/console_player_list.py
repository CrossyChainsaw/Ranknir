from Dadabase.modules.data_management import read_data, CLANS_DATA_LOCATION
import discord


async def console_player_list(interaction):
    data = read_data(CLANS_DATA_LOCATION, interaction.guild.id)
    msg = __format_msg(data)
    embed = __create_embed(msg)
    await interaction.response.send_message(embed=embed)


def __format_msg(data):
    msg = ''
    count = 1
    for entry in data['ps4_players']:
        msg += f"{count}. **id:** {entry['brawlhalla_id']}, **name**: {entry['brawlhalla_name']}\n"
        count += 1
    return msg


def __create_embed(msg):
    return discord.Embed(title="Console Players", description="The following players will be added to the leaderboard manually. To add another run: `/add_console_player`. To remove one run: `/remove_console_player`\n" + msg, color=0x00ff00)
