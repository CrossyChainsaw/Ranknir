import json
import requests
import time


class Server:
    def __init__(self, name, channel_1v1_id, channel_2v2_id, id, color, sorting_method, data_location, image="", member_count='hide', no_elo_players='hide', channel_rotating_id="NO ACCESS"):
        self.name = name
        self.channel_1v1_id = channel_1v1_id
        self.channel_2v2_id = channel_2v2_id
        self.id = id
        self.color = color
        self.sorting_method = sorting_method
        self.DATA_LOCATION = data_location

        # Optional
        self.image = image
        self.no_elo_players = no_elo_players  # hide / show
        self.channel_rotating_id = channel_rotating_id  # id
        self.member_count = member_count

    def get_data(self):
        try:
            with open(self.DATA_LOCATION) as file:
                data = json.load(file)
                return data
        except:
            print('error in trying to load data')
            time.sleep(5)

    def get_server_name(self):
        server_data = self.get_data()
        return server_data['name']

    def get_server_title(self):
        server_data = self.get_data()
        return server_data['title']

    # Deprecated
    def update_data(self):
        print('update_data() is deprecated')
        # print("Entered: update_data()")
        # print("id: " + str(self.id))
        # json_object = requests.get(
        #     f"http://game-node01.jetstax.com:27046/get_links?api_key={str(os.environ[4])}&id={str(self.id)}")
        # data = json.loads(json_object.content)
        # with open(self.DATA_LOCATION, 'w') as file:
        #     json.dump(data, file)
        #     print(self.name + ' data updated')
