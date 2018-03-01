import sys
import pygame


def check_events(ship):
    # monitor mouse and keyboard events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ship)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)

def update_screen(ai_setting, screen, ship):
    # redraw the screen at each cycle
    screen.fill(ai_setting.bg_color)
    ship.blitme()
    # let's recent paint screen is visibe
    pygame.display.flip()


def check_keydown_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    if event.key == pygame.K_LEFT:
        ship.moving_left = True


def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    if event.key == pygame.K_LEFT:
        ship.moving_left = False
