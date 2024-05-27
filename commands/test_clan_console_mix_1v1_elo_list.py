from Ranknir.modules.data_management import TEST_SERVER_ID, load_clan
from Ranknir.modules.get_players import get_account_linker_players
from Ranknir.modules.test_data import CLAN_DATA, PLAYER_OBJECT_DATA
from Ranknir.modules.sort_elo import sort_elo
from Ranknir.modules.embed import prepare_embeds_clan_mix_console, send_embeds

# Try to document what functions this exactly tests
async def test_clan_console_mix_1v1_elo_list(bot):
    # Set Test Variables
    clan = load_clan(TEST_SERVER_ID)
    console_player_objects = PLAYER_OBJECT_DATA[-5:]
    clan_player_objects = PLAYER_OBJECT_DATA[:5]


    # structure -> all_players_array = [[console_players], [clan1_players], [clan2_players], [clan3_players]]
    all_player_objects_array = []
    # Get Console Players
    #console_players = get_console_players(clan)
    #console_player_objects, _ = await get_players_elo_1v1_and_2v2(clan, console_players, f"{clan.server_name} (Console)")
    all_player_objects_array.append(console_player_objects)
    # Get Clan
    clan_data_array = []
    for i in range(len(clan.id_array)):
        # Get Clan Data
        #clan_data = await get_clan_data(clan.id_array[i])
        clan_data = CLAN_DATA
        clan_data_array.append(clan_data)
        # Get Clan Players
        clan_players = clan_data['clan']
        # Remove rm Players
        rm_players = get_account_linker_players(clan.discord_server_id)
        clan_players = [p for p in clan_players if p['brawlhalla_id'] not in rm_players]
        # Get Elo
        #clan_player_objects, _ = await get_players_elo_1v1_and_2v2(clan, clan_players, clan.clan_names[i])
        all_player_objects_array.append(clan_player_objects)
    # Restructure the array with all players
    all_player_objects_array_restructured = __fix_structure(all_player_objects_array)
    all_player_objects_array_sorted = sort_elo(clan.sorting_method, all_player_objects_array_restructured)
    embed_title, embed_array = prepare_embeds_clan_mix_console(
        clan,
        all_player_objects_array_sorted,
        clan_data_array,
        #console_player_amount=len(console_players))
        console_player_amount=len(console_player_objects))
    await send_embeds(embed_title, embed_array, bot, clan, clan.channel_1v1_id)


# function could use a better name
def __fix_structure(all_players_array):
    # new structure -> restructured_player_array = [console players + clan1_players + clan2_players + clan3_players]
    restructured_player_array = []
    for player_array in all_players_array:
        for player in player_array:
            restructured_player_array.append(player)
    return restructured_player_array