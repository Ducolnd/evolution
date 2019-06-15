#Importing modules
import random
import numpy as np
from pprint import pprint
import pygame



pygame.init()

#Game variables
margin = 1
WIDTH = 10
HEIGHT = 10
x = 75
y = 100
a = 5
players = 100
gen = []
fsr = 5 #FoodSpawnRate  

gameMap = [[0 for b in range(x)] for u in range(y)]

#Generation variables
speed = 0
size = 0
fdr = 0 #FoodDetectionRange
edr = 0 #EnemyDetectionRange
mos = 0 #MatingOffSet

#Pygame
screen_height = y*HEIGHT+y*margin+1
screen_width = x*WIDTH+x*margin+1
print(str(screen_width) + "   " + str(screen_height))

win = pygame.display.set_mode((screen_height, screen_width))
pygame.display.set_caption("Evolution")
done = False
clock = pygame.time.Clock()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)


#Functions

#Place x players on random locations
for i in range(players):
	rx = random.randint(0, x-1)
	ry = random.randint(0, y-1)
	gen = []
	for i in range(a):
		gen.append(random.randint(1, 1000))

	while gameMap[ry][rx] is not 0:
		rx = random.randint(0, x-1)
		ry = random.randint(0, y-1)

	gameMap[ry][rx] = gen

while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True

	win.fill(BLACK)

	for row in range(y):
		for column in range(x):
			if gameMap[row][column] == 0:
				color = WHITE
			else:
				gen = gameMap[row][column]
				color = ((gen[2]*255/1000), (gen[2]*255/1000), (((gen[2]+gen[3]+gen[4] )/3)*255/1000) )
			pygame.draw.rect(win, color, ((margin+WIDTH)*column+margin, (margin+HEIGHT)*row+margin, WIDTH, HEIGHT))

	clock.tick(60)
	pygame.display.flip()

pygame.quit()