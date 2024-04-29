from enum import Enum
import json
from discord import app_commands
from Dadabase.classes.Link import Link

# Paths
DADABASE_DATA_PATH = 'Dadabase/data/'
SERVERS_DATA_PATH = DADABASE_DATA_PATH + 'servers/'
CLANS_DATA_PATH = DADABASE_DATA_PATH + 'clans/'


# Data Keys
# Clans
DATA_KEY_FOR_ACCOUNT_LINKERS = 'account_linkers' # account linkers / remove players / crossplayers
DATA_KEY_FOR_CONSOLE_PLAYERS = 'console_players' # console players
DATA_KEY_FOR_SHOW_XP = 'show_xp'
# Server
DATA_KEY_FOR_SERVER_ID = 'id'
DATA_KEY_FOR_SERVER_NAME = "name"
DATA_KEY_FOR_LEADERBOARD_TITLE = "leaderboard_title"
DATA_KEY_FOR_FLAG_TYPE = 'flag_type'
DATA_KEY_FOR_SERVER_LINKS = 'links'
class FlagType(Enum):
    NONE = 'no_flags'
    REGION = 'region'
    COUNTRY = 'country'
    ETHNICITY = 'ethnicity'
# Both
DATA_KEY_FOR_SHOW_MEMBER_COUNT = 'show_member_count'
DATA_KEY_FOR_SHOW_NO_ELO_PLAYERS = 'show_no_elo_players'
DATA_KEY_FOR_SORTING_METHOD = "sorting_method"
DATA_KEY_FOR_CHANNEL_1V1_ID = "channel_1v1_id"
DATA_KEY_FOR_CHANNEL_2V2_ID = "channel_2v2_id"
DATA_KEY_FOR_CHANNEL_ROTATING_ID = "channel_rotating_id"
DATA_KEY_FOR_IMAGE = 'image'
DATA_KEY_FOR_COLOR = 'color'


# Functions
def read_data(path, id):
  """Read clan or server data"""
  with open(path + str(id) + '.json') as file:
    data = json.load(file)
    return data
  

def read_link_data(path, id):
  with open(path + str(id) + '.json') as data:
    link_data = json.load(data)["links"]
    return link_data


def write_data(path, data, id):
  print('Entered: write_data()')
  with open(path + str(id) + '.json', 'w') as write_file:
    json.dump(data, write_file, indent=4)


def add_player_to_clan_data(interaction, data, brawlhalla_account, data_location, key):
    """Adds a player to clan data. Used for Console Players and Account Linkers"""
    data[key].append(brawlhalla_account.__dict__)
    with open(data_location + str(interaction.guild.id) + '.json', 'w') as file:
        json.dump(data, file, indent=4)


def remove_player_from_clan_data(interaction, brawlhalla_id, data, key):
    """Removes a player from clan data. Used for Console Players and Account Linkers"""
    bh_name = ""
    for index, player in enumerate(data[key]):
        if player['brawlhalla_id'] == str(brawlhalla_id):
            bh_name = data[key].pop(index)['brawlhalla_name']
            with open(CLANS_DATA_PATH + str(interaction.guild.id) + '.json', 'w') as file:
                json.dump(data, file)
            break
    return bh_name

def find_link(discord_id, link_data):
    for link in link_data:
        if str(discord_id) == str(link['discord_id']):
            user = Link(link['brawlhalla_id'], 
                        link['brawlhalla_name'],
                        link['discord_id'], 
                        link['discord_name'], 
                        __check_empty(link.get('region')), 
                        __check_empty(link.get('country')), 
                        __check_empty(link.get('ethnicity')))
            return user
    else:
        return None
    
def find_link_index(discord_id, link_data):
    for index, link in enumerate(link_data):
        if discord_id == link['discord_id']:
            return index
    
def __check_empty(value):
   if value:
      return value
   else: 
      return "Not Specified"
   


def codeblock_with_link_data(user):
    return f"```ts\nbrawlhalla_name: {__empty_name(user.brawlhalla_name)}\nbrawlhalla_id: {user.brawlhalla_id}\nregion: {__check_empty(user.region)}\ncountry: {__check_empty(user.country)}\nethnicity: {__check_empty(user.ethnicity)}```"


def __empty_name(name):
    if name == "":
        return "N/A (finish 1s placement matches)"
    else:
        return name