#cd DataDuco\Documenten\Developer\Python\projects\evolution

#Importing modules
import random
import pygame

pygame.init()

#Game variables
WIDTH = 20 #10 perfect with x = 90
HEIGHT = WIDTH
tilesx = 3 #Most perfect is 90
tilesy = tilesx

starting = 5
fsr = 60 #FoodSpawnRate per fsr iterations 
fc = 0 #FoodCounter to track when to spawn
wc = 0 #WalkingCounter to track when to move player
current = []
currentFood = []

gameMap = [[0 for b in range(tilesx)] for u in range(tilesy)]

#Pygame
screen_height = tilesy*HEIGHT
screen_width = tilesx*WIDTH
win = pygame.display.set_mode((screen_height, screen_width))
pygame.display.set_caption("Evolution")
run = True
clock = pygame.time.Clock()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)


class Players(object):
	def __init__(self, speed, size, fdr, edr, mos, food, x, y):
		#Generation variables
		self.speed = speed
		self.size = size
		self.fdr = fdr #FoodDetectionRange
		self.edr = edr #EnemyDetectionRange
		self.mos = mos #MatingOffSet
		self.food = food
		self.x = x
		self.y = y

		#Player variables
		self.ttnm = 0
		self.color = [(self.speed + self.size)*255/200, (self.fdr + self.edr)*255/200, self.mos*255/100]

	def move(self, fx, fy):
		self.food += -1
		if food <= 0:
			self.die()

		if fx < 0:
			fx = 0
		if fy < 0:
			fy = 0
		if fx > tilesx-1:
			fx = tilesx-1
		if fy > tilesy-1:
			fy = tilesy-1

		if gameMap[fy][fx] == "Apple":
			self.food += 10


		gameMap[fy][fx] = [self.speed, self.size, self.fdr, self.edr, self.mos]
		gameMap[self.y][self.x] = 0
		self.x = fx
		self.y = fy

	def draw(self, win):
		pygame.draw.rect(win, self.color, (WIDTH*self.x, HEIGHT*self.y, WIDTH, HEIGHT))

	def die(self):
		current.remove(self)
		gameMap[y][x] = 0

class Food(object):
	def __init__(self, x, y, sort):
		self.x = x
		self.y = y
		self.sort = sort

	def eat(self):
		currentFood.remove(self)

	def draw(self, win):
		pygame.draw.rect(win, RED, (WIDTH*self.x, HEIGHT*self.y, WIDTH, HEIGHT))
	

#Functions
def function():
	x=1

def spawnFood():
	x = random.randint(0, tilesx-1)
	y = random.randint(0, tilesy-1)
	sort = random.choice(["Apple"]) #Add more later
	if gameMap[y][x] is 0:
		currentFood.append(Food(x, y, sort))
		gameMap[y][x] = sort

def spawnPlayer():
	speed = random.randint(1,100)
	size = random.randint(1,100)
	fdr = random.randint(1,100)
	edr = random.randint(1,100)
	mos = random.randint(1,100)
	food = random.randint(40,120)
	x = random.randint(0, tilesx-1)
	y = random.randint(0, tilesy-1)

	if gameMap[y][x] is 0:
		gameMap[y][x] = [speed, size, fdr, edr, mos]
		current.append(Players(speed, size, fdr, edr, mos, food, x, y))
	else:
		spawnPlayer()

#Place x players on random locations
for i in range(starting):
	spawnPlayer()

while run:
	fc += 1
	wc += 1

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
	win.fill(WHITE)

	for player in current: #Draw all objects in class Players
		player.draw(win)
	for snacks in currentFood: #Draw all objects in class Players
		snacks.draw(win)

	clock.tick(60)
	pygame.display.flip()

pygame.quit()