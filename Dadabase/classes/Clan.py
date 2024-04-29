from Dadabase.modules.format import format_color, split_string
from Dadabase.modules.validate_type import cast_to_int


class Clan:
    def __init__(self, server_name:str, clan_names: str, channel_1v1_id:int, channel_2v2_id:int, clan_ids:str, color:str, image:str, server_id:str, sorting_method:str='current', show_member_count:bool=True, show_xp:bool=False, show_no_elo_players:bool=False, channel_rotating_id:str = None, account_linkers=[], console_players=[]):
        
        # Convert Fields
        channel_1v1_id = int(channel_1v1_id)
        channel_2v2_id = int(channel_2v2_id)
        channel_rotating_id = cast_to_int(channel_rotating_id)
        color = format_color(color)
        clan_names = split_string(clan_names)
        clan_id_list = split_string(clan_ids)
        
        # Required
        self.server_name = server_name
        self.clan_names = clan_names
        self.discord_server_id = server_id
        self.id_array = clan_id_list
        self.color = color
        self.image = image
        self.channel_1v1_id = channel_1v1_id
        self.channel_2v2_id = channel_2v2_id

        # Optional
        self.channel_rotating_id = channel_rotating_id 
        self.sorting_method = sorting_method  # current / peak
        self.show_member_count = show_member_count
        self.show_xp = show_xp
        self.show_no_elo_players = show_no_elo_players

        # Empty Arrays
        self.account_linkers = account_linkers
        self.console_players = console_players
