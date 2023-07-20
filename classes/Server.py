import json
import os
import requests
from classes.Xos import Xos


class Server:
    def __init__(self, name, channel_1v1_id, channel_2v2_id, id, color, image, sorting_method, data_location):
        self.name = name
        self.channel_1v1_id = channel_1v1_id
        self.channel_2v2_id = channel_2v2_id
        self.id = id
        self.color = color
        self.image = image
        self.sorting_method = sorting_method
        self.DATA_LOCATION = data_location

    def get_players_data(self):
        print("getting players from: " + self.DATA_LOCATION)
        with open(self.DATA_LOCATION) as file:
            return json.load(file)

    def update_data(self):
        json_object = requests.get(
            "http://game-node01.jetstax.com:27046//get_links/api_key="+Xos().environ[3])
        data = json.loads(json_object.content)
        with open(self.DATA_LOCATION, 'w') as file:
            json.dump(data, file)
            print(self.name + ' data updated')
