import json
from discord import app_commands

DATA_LOCATION = 'Dadabase/data/'
SERVERS_DATA_LOCATION = DATA_LOCATION + 'servers/'
CLANS_DATA_LOCATION = DATA_LOCATION + 'clans/'
DATA_KEY_FOR_ACCOUNT_LINKERS = 'al_players' # account linkers / remove players / crossplayers
DATA_KEY_FOR_CONSOLE_PLAYERS = 'ps4_players' # console players

BENELUX_COUNTRIES = [    
    app_commands.Choice(name="Netherlands", value="NL"),
    app_commands.Choice(name="Belgium", value="BE"),
    app_commands.Choice(name="Luxembourg", value="LU")]

def read_data(path, id):
  """Read clan or server data"""
  with open(path + str(id) + '.json') as file:
    data = json.load(file)
    return data
  

def read_link_data(path, id):
  with open(path + str(id) + '.json') as data:
    link_data = json.load(data)["links"]
    return link_data
  

def read_all_countries():
  with open(DATA_LOCATION + 'all_countries.json', 'r') as file:
      data = json.load(file)
  all_countries = data['all_countries']
  country_choices = [app_commands.Choice(name=country['name'], value=country['value']) for country in all_countries]
  return country_choices


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