import pygame

class Ship():

	def __init__(self,screen):
		""" initialize ship and set it's initial position """
		self.screen = screen

		# loads the ship's image and get external rectangle
		self.image = pygame.image.load('images/ship.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()

		# place each new ship in the center of the screen
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom

	def blitme(self):
		""" draw the ship at the specified location """
		self.screen.blit(self.image,self.rect)