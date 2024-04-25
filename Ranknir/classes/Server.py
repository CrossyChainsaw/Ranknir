import json
import requests
import time


class Server:
    def __init__(self, id, name, leaderboard_title, sorting_method, member_count, no_elo_players, channel_1v1_id="", channel_2v2_id="", channel_rotating_id="", color="", image=""):
        # Required
        self.id = id
        self.name = name
        self.leaderboard_title = leaderboard_title
        self.sorting_method = sorting_method
        self.member_count = member_count
        self.no_elo_players = no_elo_players

        # Optional
        self.channel_1v1_id = channel_1v1_id
        self.channel_2v2_id = channel_2v2_id
        self.channel_rotating_id = channel_rotating_id
        self.image = image
        self.color = color

        # Other
        links = []

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
