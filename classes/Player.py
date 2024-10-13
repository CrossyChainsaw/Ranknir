class Player:
    def __init__(self, name, current, peak, total_wins=0, total_losses=0, region="", country="", ethnicity=""):
        self.name = name
        self.current = current
        self.peak = peak
        self.total_wins = total_wins
        self.total_losses = total_losses
        self.region = region
        self.country = country
        self.ethnicity = ethnicity
