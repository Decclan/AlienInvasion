import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """represents single alien ship"""

    def __init__(self, ai_settings, screen):
        """init alien with start pos"""
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        self.image = pygame.image.load('images/enemy_1.bmp')
        self.rect = self.image.get_rect()

        #start top left of screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #store alien pos
        self.x = float(self.rect.x)

    def blitme(self):
        self.screen.blit(self.image, self.rect)
