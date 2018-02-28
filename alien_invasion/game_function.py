import sys
import pygame


def check_events(ship):
    # monitor mouse and keyboard events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = True
            if event.key == pygame.K_LEFT:
                ship.moving_left = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False
            if event.key == pygame.K_LEFT:
                ship.moving_left == False



def update_screen(ai_setting, screen, ship):
    # redraw the screen at each cycle
    screen.fill(ai_setting.bg_color)
    ship.blitme()
    # let's recent paint screen is visibe
    pygame.display.flip()
