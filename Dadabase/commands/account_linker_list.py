from Dadabase.modules.data_management import read_data, CLANS_DATA_LOCATION, NAME_FOR_REMOVE_PLAYERS
import discord

async def account_linker_list(interaction):
    data = read_data(CLANS_DATA_LOCATION, interaction.guild.id)
    msg = __format_msg(data)
    embed = __create_embed(msg)
    await interaction.response.send_message(embed=embed)


def __format_msg(data):
    msg = ''
    count = 1
    for entry in data[NAME_FOR_REMOVE_PLAYERS]:
        msg += str(count) + '. ' + '**id:** ' + \
            entry['brawlhalla_id'] + ', **name**: ' + \
            entry['brawlhalla_name'] + '\n'
        count += 1
    return msg


def __create_embed(msg):
    return discord.Embed(title="Account Linkers", description="The following players will be removed from the leaderboard, if you wish to make them appear in the leaderboard again, run `d!alrm id`\n" + msg, color=0x00ff00)
