class Team:
    def __init__(self, name, current, peak, brawlhalla_id_one, brawlhalla_id_two, total_wins=0, total_losses=0, legend="random", mate_legend="random", region="", country="", ethnicity=""):
        # Required
        self.name = name
        self.current = current
        self.peak = peak
        self.brawlhalla_id_one = brawlhalla_id_one
        self.brawlhalla_id_two = brawlhalla_id_two
        # Optional
        self.total_wins = total_wins
        self.total_losses = total_losses
        self.legend = legend
        self.mate_legend = mate_legend
        self.region = region
        self.country = country
        self.ethnicity = ethnicity