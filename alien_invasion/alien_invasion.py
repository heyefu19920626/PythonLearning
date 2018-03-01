""" main """

import pygame

from setting import Setting
from ship import Ship
import game_function as gf


def run_game():
    # init and create screen object
    pygame.init()
    ai_setting = Setting()
    screen = pygame.display.set_mode((
        ai_setting.screen_width, ai_setting.screen_height))
    pygame.display.set_caption('Alien Invasion')
    ship = Ship(screen)
    bullets = []

    # start game main loop
    while True:
        gf.check_events(ship,screen,ai_setting,bullets)
        ship.update()
        gf.update_screen(ai_setting, screen, ship,bullets)


run_game()
