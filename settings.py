class Settings():
    """settings for alien invasion"""
    def __init__(self):
        self.screen_width = 1000
        self.screen_height = 600
        self.bg_colour = (87, 193, 255)

        #ship settings
        self.ship_speed_factor = 1.5

        #bullet settings
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_colour = 255, 210, 0
        self.bullets_allowed = 3
