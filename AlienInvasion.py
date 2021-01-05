import pygame

from settings import Settings
from ship import Ship
from alien import Alien
from pygame.sprite import Group
import game_functions as gf

def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    #creates ship
    ship = Ship(ai_settings, screen)
    #active bullet group
    bullets = Group()
    #make alien
    alien = Alien(ai_settings, screen)

    #Main loop
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, ship, alien, bullets)


run_game()
