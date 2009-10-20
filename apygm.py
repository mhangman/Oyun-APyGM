#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
import sys


def run_game():
	screen = pygame.display.set_mode((640, 480))
	running = 1
	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit_game()
		
		screen.fill((0,0,0)) #filling background with black color
		pygame.display.flip()

def exit_game():
	sys.exit()

run_game()