
class Server:
    def __init__(self, id, name, leaderboard_title, sorting_method, show_member_count, show_no_elo_players, 
                 channel_1v1_id="", channel_2v2_id="", channel_rotating_id="", color="", image="", flag_type:str = None, links=[], legend_for_2v2=[]):
        # Required
        self.id = id
        self.name = name
        self.leaderboard_title = leaderboard_title
        self.sorting_method = sorting_method
        self.show_member_count = show_member_count
        self.show_no_elo_players = show_no_elo_players

        # Optional
        self.channel_1v1_id = channel_1v1_id
        self.channel_2v2_id = channel_2v2_id
        self.channel_rotating_id = channel_rotating_id
        self.image = image
        self.color = color
        self.flag_type = flag_type
        self.links = links
        self.legend_for_2v2 = legend_for_2v2