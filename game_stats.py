class GameStats():
    """documents the stats in the game"""

    def __init__(self, ai_settings):
        """initialize the stats"""
        self.ai_settings = ai_settings
        self.reset_stats()

        # inactive if the game just started
        self.game_active = False

        # never reset high_score
        self.high_score =  0

    def reset_stats(self):
        """initialize the stats which could be change during a game"""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1