class Clan:
    def __init__(self, server_name:str, clan_names: str, channel_1v1_id:int, channel_2v2_id:int, id_array:str, color:str, image:str, server_id:str, sorting_method='current', member_count='show', xp='hide', no_elo_players='hide', channel_rotating_id = "NO ACCESS", has_account_linkers=False, account_linkers=[], console_players=[]):
        self.server_name = server_name
        self.clan_names = clan_names
        self.discord_server_id = server_id
        self.id_array = id_array
        self.color = color
        self.image = image
        self.channel_1v1_id = channel_1v1_id
        self.channel_2v2_id = channel_2v2_id

        # Optional
        self.channel_rotating_id = channel_rotating_id # id
        self.sorting_method = sorting_method  # current / peak
        self.member_count = member_count      # show / hide
        self.xp = xp                          # show / hide
        self.no_elo_players = no_elo_players  # show / hide
        self.has_account_linkers = has_account_linkers  # True / False
        self.account_linkers = account_linkers
        self.console_players = console_players
