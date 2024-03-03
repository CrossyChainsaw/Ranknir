class Clan:
    def __init__(self, name, channel_1v1_id, channel_2v2_id, id_array, color, image, server_id, sorting_method='current', member_count='show', xp='hide', format='A', elo_type='general', no_elo_players='hide', channel_rotating_id = "NO ACCESS", has_rm_players=False):
        self.name = name
        self.channel_1v1_id = channel_1v1_id
        self.channel_2v2_id = channel_2v2_id
        self.id_array = id_array
        self.color = color
        self.image = image
        self.server_id = server_id

        # Optional
        self.sorting_method = sorting_method  # current / peak
        self.member_count = member_count      # show / hide
        self.xp = xp                          # hide / show
        self.format = format                  # A / B
        self.elo_type = elo_type              # general / legend
        self.no_elo_players = no_elo_players  # show / hide
        self.channel_rotating_id = channel_rotating_id # id
        self.has_rm_players = has_rm_players  # True / False
