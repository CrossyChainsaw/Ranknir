from Dadabase.modules.frost_commands.data import get_all_player_ids, DATA_SINGLE_PLAYER_LOCATION
from Dadabase.modules.data import read_data
from Dadabase.classes.Frost_Player import Frost_Player
import discord


async def legend_list(ctx, legend_id):
    all_ids = get_all_player_ids()
    embed = discord.Embed(title='', description='')
    all_players = []
    for id in all_ids:
        data = read_data(DATA_SINGLE_PLAYER_LOCATION, id)
        legends = data['legends']
        for legend in legends:
            if legend['legend_id'] == int(legend_id):
                embed.title = (legend['legend_name_key']).capitalize()
                player = Frost_Player(data['name'], str(
                    legend['level']), legend['xp'])
                all_players.append(player)
    sorted_list = sort_list(all_players)
    for player in sorted_list:
        embed.description += "%s - Lv. %s (%s xp)\n" % (
            player.name, player.level, str(player.xp))
    await ctx.channel.send(embed=embed)


def sort_list(all_player_list):
    sorted_list = []
    highest_xp = -1
    best_player = None
    while len(all_player_list) > 0:
        best_i = 0
        highest_xp = -1
        for i, player in enumerate(all_player_list):
            if player.xp > highest_xp:
                highest_xp = player.xp
                best_player = player
                best_i = i
        print(best_player.name)
        sorted_list.append(all_player_list.pop(best_i))
    return sorted_list
