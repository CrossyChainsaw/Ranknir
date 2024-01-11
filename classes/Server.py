import json
import requests
import os


class Server:
    def __init__(self, name, channel_1v1_id, channel_2v2_id, id, color, image, sorting_method, data_location, no_elo_players='hide', channel_rotating_id="NO ACCESS"):
        self.name = name
        self.channel_1v1_id = channel_1v1_id
        self.channel_2v2_id = channel_2v2_id
        self.id = id
        self.color = color
        self.image = image
        self.sorting_method = sorting_method
        self.DATA_LOCATION = data_location

        # Optional
        self.no_elo_players = no_elo_players  # hide / show
        self.channel_rotating_id = channel_rotating_id # id

    def get_players_data(self):
        print("getting players from: " + self.DATA_LOCATION)
        with open(self.DATA_LOCATION) as file:
            return json.load(file)

    def update_data(self):
        print("Entered: update_data()")
        print("id: " + str(self.id))
        json_object = requests.get(
            f"http://game-node01.jetstax.com:27046/get_links?api_key={str(os.environ['DADABASE_API_KEY'])}&id={str(self.id)}")
        data = json.loads(json_object.content)
        with open(self.DATA_LOCATION, 'w') as file:
            json.dump(data, file)
            print(self.name + ' data updated')
