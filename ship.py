import pygame

class Ship():
    """player ship class"""
    def __init__(self, ai_settings, screen):
        self.screen = screen
        self.ai_settings = ai_settings

        #load image, get rectangle
        self.image = pygame.image.load('images/player.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #start new ship bottom center
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        #decimal value for ship center
        self.center = float(self.rect.centerx)

        #movement flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        #moves ship center if movement flag true
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
        #update rect from self.center
        self.rect.centerx = self.center

    def blitme(self):
        #draw ship current loc
        self.screen.blit(self.image, self.rect)