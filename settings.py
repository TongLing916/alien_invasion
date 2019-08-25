class Settings():
    """ a class to store all settings"""

    def __init__(self):
        """initialize settings for the game"""
        # settings for screen
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # settings for ship
        self.ship_speed_factor = 1.5
        self.ship_limit = 3

        # settings for bullet
        self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3

        # settings for aliens
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        # fleet_direction == 1: moving right
        # fleet_direction == -1: moving left
        self.fleet_direction = 1

        # speed up the rythme
        self.speedup_scale = 1.1
        # speed of increasing the score of an alien
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """initialize with the game"""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1

        # fleet_direction == 1: moving right
        # fleet_direction == -1: moving left
        self.fleet_direction = 1

        # score
        self.alien_points = 50

    def increase_speed(self):
        """increase speed in the settings"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
