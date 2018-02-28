""" main """

import sys

import pygame

from setting import Setting
from ship import Ship

def run_game():
	# init and create screen object
	pygame.init()
	ai_setting = Setting()
	screen = pygame.display.set_mode((
		ai_setting.screen_width,ai_setting.screen_height))
	pygame.display.set_caption('Alien Invasion')
	ship = Ship(screen)


	# start game main loop
	while True:

		# monitor mouse and keyboard events
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

		# redraw the screen at each cycle
		screen.fill(ai_setting.bg_color)
		ship.blitme()

		# let's recent paint screen is visibe
		pygame.display.flip()

run_game()
