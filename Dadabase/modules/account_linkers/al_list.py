from Dadabase.modules.ps4.ps4_data import load_data
from Dadabase.modules.account_linkers.al_data import NAME_FOR_REMOVE_PLAYERS
import discord

async def rmp_list(ctx):
    data = load_data(ctx.guild.id)
    msg = __format_msg(data)
    embed = __create_embed(msg)
    await ctx.channel.send(embed=embed)


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
    return discord.Embed(title="Account Linkers", description="The following players will be removed from the leaderboard, if you wish to make them appear in the leaderboard again, run `d!rmprm id`\n" + msg, color=0x00ff00)
