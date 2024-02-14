import json


def read_link_data(path, id):
  with open(path + str(id) + '.json') as data:
    link_data = json.load(data)["links"]
    return link_data


def read_data(path, id):
  with open(path + str(id) + '.json') as data:
    the_data = json.load(data)
    return the_data

def write_data(path, data, id):
  print('Entered: write_data()')
  with open(path + str(id) + '.json', 'w') as write_file:
    json.dump(data, write_file)

    
