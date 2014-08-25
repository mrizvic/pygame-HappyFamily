#!/bin/env python

import sys,pygame
import random
import Vector

pygame.init()

size = width,height = 1440,900
speed = [0,0]
black = 0,0,0

screen = pygame.display.set_mode(size)

ball = pygame.image.load('ball.gif')
ballrect = ball.get_rect()

v = Vector.Vector()
v.maxspeed=10
v.maxfactor=0.25

running = True

ballrect = ballrect.move(770,450)

while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT or ( event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE ):
			running = False

	v.set()


	print '{} {}'.format(v.x,v.y)

        if ballrect.left < 0 or ballrect.right > width:
		print 'X axis overflow'
		v.x = v.x * -1
        if ballrect.top < 0 or ballrect.bottom > height:
		print 'Y axis overflow'
		v.y = v.y * -1

	speed[0] = v.x
	speed[1] = v.y


	ballrect = ballrect.move(speed)

	screen.fill(black)
	screen.blit(ball,ballrect)
	pygame.display.flip()


pygame.quit()
sys.exit(1)
