#Importing modules
import random
import pygame

pygame.init()

#Game variables
margin = 0
WIDTH = 15 #10 perfect with x = 90
HEIGHT = WIDTH
tilesx = 40 #Most perfect is 90
tilesy = tilesx

starting = 100
fsr = 200 #FoodSpawnRate per fsr iterations 
fc = 0 #FoodCounter to track when to spawn
wc = 0 #WalkingCounter to track when to move player
current = []

gameMap = [[0 for b in range(tilesx)] for u in range(tilesy)]

#Pygame
screen_height = tilesy*HEIGHT+tilesy*margin+1
screen_width = tilesx*WIDTH+tilesx*margin+1
win = pygame.display.set_mode((screen_height, screen_width))
pygame.display.set_caption("Evolution")
run = True
clock = pygame.time.Clock()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)


class Players(object):
	def __init__(self, speed, size, fdr, edr, mos, x, y):
		#Generation variables
		self.speed = speed
		self.size = size
		self.fdr = fdr #FoodDetectionRange
		self.edr = edr #EnemyDetectionRange
		self.mos = mos #MatingOffSet
		self.x = x
		self.y = y

		#Player variables
		self.ttnm = 0
		self.food = 0
		self.color = [(self.speed + self.size)*255/200, (self.fdr + self.edr)*255/200, self.mos*255/100]

	def move(self, fx, fy):
		if fx < 0:
			fx = 0
		if fy < 0:
			fy = 0
		if fx > tilesx-1:
			fx = tilesx-1
		if fy > tilesy-1:
			fy = tilesy-1

		gameMap[fy][fx] = [self.speed, self.size, self.fdr, self.edr, self.mos]
		gameMap[self.y][self.x] = 0
		self.x = fx
		self.y = fy

	def draw(self, win):
		pygame.draw.rect(win, self.color, ((margin+WIDTH)*(self.x)+margin, (margin+HEIGHT)*(self.y)+margin, WIDTH, HEIGHT))

#Place x players on random locations
for i in range(starting):
	speed = random.randint(1,100)
	size = random.randint(1,100)
	fdr = random.randint(1,100)
	edr = random.randint(1,100)
	mos = random.randint(1,100)
	x = random.randint(1, tilesx-1)
	y = random.randint(1, tilesy-1)

	current.append(Players(speed, size, fdr, edr, mos, x, y))

#Functions
def function():
	pass

while run:
	wc += 1
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
	win.fill(WHITE)

	for player in current:
		player.draw(win)


	if wc > 5:
		wc = 0
		for player in current:
			player.move(player.x, player.y+1)


	clock.tick(60)
	pygame.display.flip()

pygame.quit()