class Server2:
    def __init__(self, discord_server_name, brawlhalla_clan_names, discord_server_id,
                 brawlhalla_id_array, embed_color, leaderboard_title, discord_channel_1v1_id, 
                 discord_channel_2v2_id, discord_channel_rotating_id, leaderboard_image="",
                 players_sorting_method='current', show_member_count=True, show_clan_xp=False,
                 show_no_elo_players=False, show_player_win_loss=True, show_player_legends=True,
                 flag_type=None, account_linkers=[], console_players=[], legends_for_2v2=[]):
        
        # Required
        self.discord_server_id = discord_server_id
        self.discord_server_name = discord_server_name
        self.brawlhalla_id_array = brawlhalla_id_array
        self.brawlhalla_clan_names = brawlhalla_clan_names
        self.embed_color = embed_color
        self.leaderboard_title = leaderboard_title
        self.discord_channel_1v1_id = discord_channel_1v1_id
        self.discord_channel_2v2_id = discord_channel_2v2_id
        self.discord_channel_rotating_id = discord_channel_rotating_id
        # Optional
        self.leaderboard_image = leaderboard_image
        self.players_sorting_method = players_sorting_method
        self.show_member_count = show_member_count
        self.show_clan_xp = show_clan_xp
        self.show_no_elo_players = show_no_elo_players
        self.show_player_win_loss = show_player_win_loss
        self.show_player_legends = show_player_legends
        self.flag_type = flag_type
        self.account_linkers = account_linkers
        self.console_players = console_players
        self.legends_for_2v2 = legends_for_2v2