from Ranknir.modules.api import fetch_player_ranked_stats
from Ranknir.modules.sort_elo import sort_elo
from Ranknir.modules.embed import send_embeds
from Ranknir.classes.Clan import Clan
from Ranknir.classes.Player import Player
import discord
import asyncio


async def send_all_legends_elo(brawlhalla_id, channel_id, bot):
    ranked_stats = await fetch_player_ranked_stats(brawlhalla_id)
    legends = ranked_stats['legends']
    legends_ranked_stats = []
    for legend in legends:
        player = Player(legend['legend_name_key'],legend['rating'], legend['peak_rating'])
        legends_ranked_stats.append(player)
    sorted_legends_ranked_stats = sort_elo('current', legends_ranked_stats)
    embed_title, embed_array = prep_embeds(
        ranked_stats, sorted_legends_ranked_stats)
    await send_embeds(embed_title, embed_array, bot, Clan('', 0, 0, [], 0x000000, '', 1165233663923994666), channel_id)


def prep_embeds(ranked_stats, sorted_legends_ranked_stats):
    name = ranked_stats['name']
    embed_title = discord.Embed(title=f'{name} Legends ELO', description='')
    # Variables
    embed_array = []
    global rank
    rank = 1
    count = 0
    embed = discord.Embed(description="")

    # Format Embeds
    for legend in sorted_legends_ranked_stats:
        if count == 15:
            embed_array.append(embed)
            count = 0
        if count == 0:
            embed = discord.Embed(description="")
        if count <= 20:
            rank_img = get_rank_img(legend.current)
            embed.description += f"{rank_img} **{(legend.name).capitalize()}**: current: **{legend.current}** peak: **{legend.peak}**\n"
        rank += 1
        count += 1
    embed_array.append(embed)

    return embed_title, embed_array


def get_rank_img(current):
    if current >= 2000:
        return "<:Diamond:1165251154247172158>"
    elif current >= 1680:
        return "<:Platinum:1165251156403040278>"
    elif current >= 1390:
        return "<:Gold:1165251155304132708>"
    elif current >= 1130:
        return "<:Silver:1165251157409677392>"
    elif current >= 910:
        return "<:Bronze:1165251152133242941>"
    elif current >= 200:
        return "<:Tin:1165251159800422421>"
