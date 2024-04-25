import json
from discord import app_commands
from Dadabase.classes.User import User

DATA_LOCATION = 'Dadabase/data/'
SERVERS_DATA_LOCATION = DATA_LOCATION + 'servers/'
CLANS_DATA_LOCATION = DATA_LOCATION + 'clans/'
DATA_KEY_FOR_ACCOUNT_LINKERS = 'al_players' # account linkers / remove players / crossplayers
DATA_KEY_FOR_CONSOLE_PLAYERS = 'ps4_players' # console players

BENELUX_COUNTRIES = [    
    app_commands.Choice(name="Netherlands", value="NL"),
    app_commands.Choice(name="Belgium", value="BE"),
    app_commands.Choice(name="Luxembourg", value="LU")]

ALL_COUNTRIES = [
    app_commands.Choice(name="Don't Specify", value=""),
    app_commands.Choice(name="Algeria", value="DZ"),
    app_commands.Choice(name="Argentina", value="AR"),
    app_commands.Choice(name="Belgium", value="BE"),
    app_commands.Choice(name="Brazil", value="BR"),
    app_commands.Choice(name="Canada", value="CA"),
    app_commands.Choice(name="Chile", value="CL"),
    app_commands.Choice(name="Curacao", value="CW"),
    app_commands.Choice(name="Dominican Republic", value="DO"),
    app_commands.Choice(name="Germany", value="DE"),
    app_commands.Choice(name="Indonesia", value="ID"),
    app_commands.Choice(name="Iraq", value="IQ"),
    app_commands.Choice(name="Italy", value="IT"),
    app_commands.Choice(name="Japan", value="JP"),
    app_commands.Choice(name="Luxembourg", value="LU"),
    app_commands.Choice(name="Morocco", value="MA"),
    app_commands.Choice(name="Netherlands", value="NL"),
    app_commands.Choice(name="Spain", value="ES"),
    app_commands.Choice(name="Suriname", value="SR"),
    app_commands.Choice(name="Turkey", value="TR"),
    app_commands.Choice(name="United States of America", value="US"),
    app_commands.Choice(name="Vietnam", value="VN")
]

SERVERS = [
    app_commands.Choice(name="US-E", value="USE"),
    app_commands.Choice(name="US-W", value="USW"),
    app_commands.Choice(name="Europe", value="EU"),
    app_commands.Choice(name="South East Asia", value="SEA"),
    app_commands.Choice(name="Australia", value="AUS"),
    app_commands.Choice(name="Brazil", value="BRS"),
    app_commands.Choice(name="Japan", value="JPN"),
    app_commands.Choice(name="Middle East", value="MDE"),
    app_commands.Choice(name="Southern Africa", value="SAF"),
]

SORTING_METHOD_OPTIONS = [
    app_commands.Choice(name="Current Elo", value="current"),
    app_commands.Choice(name="Peak Elo", value="peak")]

MEMBER_COUNT_OPTIONS = [
    app_commands.Choice(name="Hide", value="hide"),
    app_commands.Choice(name="Show", value="show")]

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
            with open(CLANS_DATA_LOCATION + str(interaction.guild.id) + '.json', 'w') as file:
                json.dump(data, file)
            break
    return bh_name

def find_link(discord_id, link_data):
    for link in link_data:
        if str(discord_id) == str(link['discord_id']):
            user = User(link['brawlhalla_id'], 
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