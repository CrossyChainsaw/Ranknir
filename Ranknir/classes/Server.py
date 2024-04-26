import json
import requests
import time


class Server:
    def __init__(self, id, name, leaderboard_title, sorting_method, member_count, no_elo_players, channel_1v1_id="", channel_2v2_id="", channel_rotating_id="", color="", image="", links=[]):
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
        self.links = links