import os
import discord
from discord.ext import commands, tasks
from modules.keep_alive import keep_alive
from modules.embed import send_embeds2, prepare_embeds_new, prepare_embeds_new_server
from modules.sort_elo import sort_elo_1v1, sort_2v2_elo, sort_elo_1v1_server
from modules.wait import wait
from modules.turn import get_turn, next_turn
from modules.turn import reset_turn
from modules.clan import get_clans_data
from classes.clan import Clan
from classes.server import Server
from modules.get_members_elo import get_members_1v1_elo_server, get_members_1v1_elo, get_members_2v2_elo
from data.clan_data import Skyward, Pandation, lnsomnia, test_clan, Cybers, Cherimoya, Excalibur, Fanfare, Tews, Fawaka, Dair
from data.server_data import Brawlhalla_NL

# CHANGE BACK TO 12
# CHANGE BACK TO 12
# CHANGE BACK TO 12
# CHANGE BACK TO 12

# CHANGE BACK TO 12
# CHANGE BACK TO 12
# CHANGE BACK TO 12
# CHANGE BACK TO 12

intents = discord.Intents().all()
bot = commands.Bot(command_prefix=['r', 'R'], intents=intents)
#turn = 10


@bot.event
async def on_ready():
    # I'm back online!
    print(f'We have logged in as {bot.user}')

    # main, send 1v1 / 2v2 elo list
    while True:
        turn = get_turn()
        print("current turn: " + str(turn))

        if turn == 0:
            await main_2v2_crazy(Dair, sorting_method="current")
        elif turn == 1:
            await main_1v1_crazy(Pandation, sorting_method="peak")
        elif turn == 2:
            await main_2v2_crazy(Pandation, sorting_method="peak")
        elif turn == 3:
            await main_1v1_crazy(lnsomnia, sorting_method="peak")
        elif turn == 4:
            await main_2v2_crazy(lnsomnia, sorting_method="peak")
        elif turn > 20:
            await main_1v1_crazy(test_clan, sorting_method="peak")
        elif turn == 5:
            await main_1v1_crazy(Cybers, sorting_method="peak")
        elif turn == 6:
            await main_2v2_crazy(Cybers, sorting_method="current")
        elif turn == 7:
            await main_2v2_crazy(Skyward, sorting_method="current")
        elif turn == 8:
            await main_1v1_crazy(Cherimoya, sorting_method="peak")
        elif turn == 9:
            await main_1v1_crazy(Excalibur, sorting_method="peak")
        elif turn == 10:
            await main_2v2_crazy(Excalibur, sorting_method="peak")
        elif turn == 11:
            await main_2v2_crazy(Fanfare, sorting_method="peak")
        elif turn == 12:
            await main_1v1_crazy(Tews, sorting_method="current")
        elif turn == 13:
            await main_2v2_crazy(Tews, sorting_method="current")
        elif turn == 14:
            await main_1v1_crazy(Fawaka, sorting_method="current")
        elif turn == 15:
            await main_2v2_crazy(Fawaka, sorting_method="current")
        elif turn > 15:
            await main_1v1_server(Brawlhalla_NL, sorting_method="current")
            reset_turn()
        next_turn()
        wait(5)


async def main_1v1_crazy(clan, sorting_method):
    clan_data_array = get_clans_data(clan.id_array)
    players, console_player_amount = get_members_1v1_elo(clan, clan_data_array[0]['clan_name'])
    players_sorted = sort_elo_1v1(clan, players, sorting_method)
    embed2, embed_array = prepare_embeds_new(clan, clan_data_array, players_sorted, console_player_amount)
    await send_embeds2(embed2,
                       embed_array,
                       bot=bot,
                       channel_id=clan.channel_1v1_id,
                       clan_image=clan.image)

async def main_2v2_crazy(clan, sorting_method):
    clan_data_array = get_clans_data(clan.id_array)
    players, console_player_amount = get_members_2v2_elo(clan, sorting_method, clan_data_array[0]['clan_name'])
    players_sorted = sort_2v2_elo(clan, players, sorting_method)
    print(players_sorted[0])
    embed2, embed_array = prepare_embeds_new(clan, clan_data_array, players_sorted, console_player_amount)
    await send_embeds2(embed2,
                       embed_array,
                       bot=bot,
                       channel_id=clan.channel_2v2_id,
                       clan_image=clan.image)


async def main_1v1_server(server, sorting_method):
    # update data
    try:
        server.update_data()
    except:
        print("couldn't update data, make sure Dadabase is running")

    # get players elo
    names, current_ratings, peak_ratings = get_members_1v1_elo_server(server)

    # sort players elo
    names_sorted, current_ratings_sorted, peak_ratings_sorted = sort_elo_1v1_server(
        server, sorting_method, names, current_ratings, peak_ratings)
    print(names_sorted)

    embed2, embed_array = prepare_embeds_new_server(server, names_sorted,
                                                    current_ratings_sorted,
                                                    peak_ratings_sorted,
                                                    server.color)

    await send_embeds2(embed2,
                       embed_array,
                       bot=bot,
                       channel_id=server.channel_1v1_id,
                       clan_image=server.image)

    # clear arrays
    names_sorted.clear()
    current_ratings_sorted.clear()
    peak_ratings_sorted.clear()



keep_alive()
bot.run(os.environ["BOT_KEY"])
