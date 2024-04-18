import json

SERVERS_DATA_LOCATION = 'Dadabase/data/servers/'
CLANS_DATA_LOCATION = 'Dadabase/data/clans/'
NAME_FOR_REMOVE_PLAYERS = 'al_players' # account linkers / remove players / crossplayers
NAME_FOR_CONSOLE_PLAYERS = 'ps4_players' # console players

def read_link_data(path, id):
  with open(path + str(id) + '.json') as data:
    link_data = json.load(data)["links"]
    return link_data


def read_data(path, id):
  """Read clan or server data"""
  with open(path + str(id) + '.json') as file:
    data = json.load(file)
    return data

def write_data(path, data, id):
  print('Entered: write_data()')
  with open(path + str(id) + '.json', 'w') as write_file:
    json.dump(data, write_file, indent=4)