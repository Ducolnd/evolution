#cd DataDuco\Documenten\Developer\Python\projects\evolution

#Importing modules
import random
import pygame

pygame.init()

#Game variables
WIDTH = 20 #10 perfect with x = 90
HEIGHT = WIDTH
tilesx = 40 #Most perfect is 90
tilesy = tilesx

starting = 10
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
ffont = pygame.font.SysFont("comicsansms", 20)
clock = pygame.time.Clock()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)


class Players(object):
	def __init__(self, speed, fdr, edr, mos, food, x, y):
		#Generation variables
		self.speed = speed
		self.size = 100-self.speed
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
		if self.food <= 0:
			self.die()

		if fx < 0:
			fx = 0
		if fy < 0:
			fy = 0
		if fx > tilesx-1:
			fx = tilesx-1
		if fy > tilesy-1:
			fy = tilesy-1

		if gameMap[fy][fx] is not 0:
			if "Apple" in gameMap[fy][fx]:
				self.food += 10
				gameMap[fy][fx][1].eat()

		gameMap[fy][fx] = [self.speed, self.size, self.fdr, self.edr, self.mos]
		gameMap[self.y][self.x] = 0
		self.x = fx
		self.y = fy

	def draw(self, win):
		pygame.draw.rect(win, self.color, (WIDTH*self.x, HEIGHT*self.y, WIDTH, HEIGHT))
		food_number = ffont.render(str(self.food), True, BLACK)
		win.blit(food_number, (self.x*WIDTH+(WIDTH/2-food_number.get_width()/2), self.y*HEIGHT+(HEIGHT/2-food_number.get_height()/2)))

	def die(self):
		current.remove(self)
		gameMap[y][x] = 0
		gameMap[self.y][self.x] = 0
		
	def find_objective(self, objective):
		pass

	def wander(self):
		ry = random.randint(-1, 1)
		
                        
class Food(object):
	def __init__(self, x, y, sort):
		self.x = x
		self.y = y
		self.sort = sort
                
	def eat(self):
		currentFood.remove(self)
		gameMap[self.y][self.x] = 0

	def draw(self, win):
		pygame.draw.rect(win, RED, (WIDTH*self.x, HEIGHT*self.y, WIDTH, HEIGHT))
	

#Functions
def spawnFood():
	x = random.randint(0, tilesx-1)
	y = random.randint(0, tilesy-1)
	sort = random.choice(["Apple"]) #Add more later
	if gameMap[y][x] is 0:
		foodClass = Food(x, y, sort)
		currentFood.append(foodClass)
		gameMap[y][x] = [sort, foodClass]

def spawnPlayer():
	speed = random.randint(1,100)
	fdr = random.randint(1,100)
	edr = random.randint(1,100)
	mos = random.randint(1,100)
	food = random.randint(40,120)
	x = random.randint(0, tilesx-1)
	y = random.randint(0, tilesy-1)

	if gameMap[y][x] is 0:
		gameMap[y][x] = [speed, size, fdr, edr, mos]
		current.append(Players(speed, fdr, edr, mos, food, x, y))
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

	if fc > 100:
		fc = 0
		spawnFood()
	if wc > 10:
		wc = 0
		for player in current:
			player.move(player.x+1, player.y)

	for player in current: #Draw all objects in class Players
		player.draw(win)
	for snacks in currentFood: #Draw all objects in class Players
		snacks.draw(win)

	clock.tick(60)
	pygame.display.flip()

pygame.quit()
