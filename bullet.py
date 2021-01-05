import pygame 
from pygame.sprite import Sprite

class Bullet(Sprite):
    """class for bullet management"""
    
    def __init__(self, ai_settings, screen, ship):
        #creates bullet at ships position
        super(Bullet, self).__init__()
        self.screen = screen

        #create bullet at (0,0) then correct position
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        #var for storing bullet pos
        self.y = float(self.rect.y)

        self.colour = ai_settings.bullet_colour
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        #move bullet up screen
        self.y -= self.speed_factor
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.colour, self.rect)