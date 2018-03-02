import sys
import pygame
import bullet


def check_events(ship,screen,ai_setting,bullets):
    # monitor mouse and keyboard events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ship,screen,ai_setting,bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)

def update_screen(ai_setting, screen, ship,bullets):
    # redraw the screen at each cycle
    screen.fill(ai_setting.bg_color)
    ship.blitme()
    update_bullets(bullets)
    # let's recent paint screen is visibe
    pygame.display.flip()


def check_keydown_events(event, ship,screen,ai_setting,bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    if event.key == pygame.K_LEFT:
        ship.moving_left = True
    if event.key == pygame.K_SPACE:
        new_bullet = bullet.Bullet(screen,ship,ai_setting)
        bullets.append(new_bullet)

def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    if event.key == pygame.K_LEFT:
        ship.moving_left = False

def update_bullets(bullets):
    if bullets:
        for bulleted in bullets:
            # print(bulleted.rect.y)
            bulleted.update()
            if bulleted.rect.bottom <= 0:
                bullets.remove(bulleted)
            else:
                bulleted.draw_bullet()
