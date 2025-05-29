class Player:
    def __init__(self, brawlhalla_id, name, current, peak, total_wins=0, total_losses=0, legend="random", region="", country="", ethnicity=""):
        self.brawlhalla_id = brawlhalla_id
        self.name = name
        self.current = current
        self.peak = peak
        self.total_wins = total_wins
        self.total_losses = total_losses
        self.legend = legend
        self.region = region
        self.country = country
        self.ethnicity = ethnicity

    def to_dict(self):
        return {
            "brawlhalla_id": self.brawlhalla_id,
            "name": self.name,
            "current": self.current,
            "peak": self.peak,
            "total_wins": self.total_wins,
            "total_losses": self.total_losses,
            "legend": self.legend,
            "region": self.region,
            "country": self.country,
            "ethnicity": self.ethnicity,
        }
