#Importing modules
import random
import numpy as np
from pprint import pprint
import pygame
import string

pygame.init()

#Game variables
margin = 1
WIDTH = 15 #10 perfect with x = 90
HEIGHT = WIDTH
x = 40 #Most perfect is 90
y = x
a = 5
players = 10
gen = []
fsr = 200 #FoodSpawnRate per fsr iterations 
fc = 0 #FoodCounter to track when to spawn
wc = 0 #WalkingCounter to track when to move player
dirs = []
current = []

gameMap = [[0 for b in range(x)] for u in range(y)]

#Generation variables
speed = 0
size = 0
fdr = 0 #FoodDetectionRange
edr = 0 #EnemyDetectionRange
mos = 0 #MatingOffSet

#Player variables
ttns = 0
food = 0

#Pygame
screen_height = y*HEIGHT+y*margin+1
screen_width = x*WIDTH+x*margin+1

win = pygame.display.set_mode((screen_height, screen_width))
pygame.display.set_caption("Evolution")
done = False
clock = pygame.time.Clock()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)


#Functions

def spawnFood():
	rx = random.randint(0, x-1)
	ry = random.randint(0, y-1)
	while gameMap[ry][rx] is not 0:
		rx = random.randint(0, x-1)
		ry = random.randint(0, y-1)
	gameMap[ry][rx] = "food"

def checkSurroundings():
	pass

def move(where, place, who):
	gameMap[where[0]][where[1]] = who
	gameMap[place[0]][place[1]] = 0

def birth():
	pass


#Place x players on random locations
for i in range(players):
	rx = random.randint(0, x-1)
	ry = random.randint(0, y-1)
	location = [ry, rx]
	gen = []
	for i in range(a):
		gen.append(random.randint(1, 100))
	gen.extend([ttns, random.randint(0,20), location])

	current.append(gen)

	while gameMap[ry][rx] is not 0:
		rx = random.randint(0, x-1)
		ry = random.randint(0, y-1)

	gameMap[ry][rx] = gen


while not done:
	fc += 1
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True

	win.fill(BLACK)

	if fc > fsr:
		spawnFood()

	for i in current:
		if i[6] < 1:
			gameMap[i[7][0]][i[7][1]] = 0
			current.remove(i)
			continue
		i[5] += 1
		if i[5] > i[0]:
			i[6] += -1
			i[5] = 0
			rx = random.randint(-1,1)
			if rx == 0:
				ry = random.choice([-1,1])
			else:
				ry = random.randint(-1,1)
			ry = i[7][0]-ry
			rx = i[7][1]-rx

			if ry < 0:
				ry = 0
			if ry > x:
				ry = (x-1)
			if rx < 0:
				rx = 0
			if rx > x:
				rx = (x-1)
			if gameMap[ry][rx] == "food":
				i[6] += 10
			loc = [ry, rx]
			move(loc, i[7], i[0:5])
			i[7] = loc


	for row in range(y):
		for column in range(x):
			if gameMap[row][column] == 0:
				color = WHITE
			elif gameMap[row][column] == "food":
				color = RED
			else:
				gen = gameMap[row][column]
				color = ((gen[2]*255/100), (gen[2]*255/100), (((gen[2]+gen[3]+gen[4] )/3)*255/100) )
			pygame.draw.rect(win, color, ((margin+WIDTH)*column+margin, (margin+HEIGHT)*row+margin, WIDTH, HEIGHT))

	clock.tick(60)
	pygame.display.flip()

pygame.quit()