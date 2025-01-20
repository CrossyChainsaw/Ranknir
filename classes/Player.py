class Player:
    def __init__(self, brawlhalla_id, name, current, peak, region="", country="", ethnicity=""):
        self.brawlhalla_id = brawlhalla_id
        self.name = name
        self.current = current
        self.peak = peak
        self.total_wins = 0
        self.total_losses = 0
        self.legend = "random"
        self.region = region
        self.country = country
        self.ethnicity = ethnicity
