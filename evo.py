#cd DataDuco\Documenten\Developer\Python\projects\evolution

#Importing modules
import random
import pygame
from pprint import pprint as pp

pygame.init()

#Game variables
WIDTH = 25 #10 perfect with x = 90
HEIGHT = WIDTH
tilesx = 40 #Most perfect is 90
tilesy = tilesx

starting = 30
startingFood = 30
fsr = 20 #FoodSpawnRate per fsr iterations 
fc = 0 #FoodCounter to track when to spawn
wc = 0 #WalkingCounter to track when to move player
current = []
currentFood = []
l = []

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
DARKBLUE = (0,0,139)


class Players(object):
	def __init__(self, speed, fdr, edr, mos, fgt, food, grown, x, y):
		#Generation variables
		self.speed = speed
		self.size = 100-self.speed
		self.fdr = fdr #FoodDetectionRange
		self.edr = edr #EnemyDetectionRange
		self.mos = mos #MatingOffSet
		self.fgt = fgt #Food Give Through
		self.food = food
		self.grown = grown

		#Player variables
		self.ttnm = 0
		self.color = [(self.speed + self.size)*255/100, (self.fdr + self.edr)*255/12, self.fgt*255/120]
		self.x = x
		self.y = y
		self.wc = 0
		self.wanderBool = False
		self.mateBool = False
		self.objective = []
		self.steps = 10

	def move(self, fx, fy):
		self.food += random.randint(-2, -1)

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
				self.objective = []
				self.steps = 10
				self.food += 10
				gameMap[fy][fx][1].eat()

		gameMap[self.y][self.x] = 0
		gameMap[fy][fx] = [self.speed, self.size, self.fdr, self.edr, self.mos]
		self.x = fx
		self.y = fy

	def draw(self, win):
		pygame.draw.rect(win, self.color, (WIDTH*self.x, HEIGHT*self.y, WIDTH, HEIGHT))
		if self.wanderBool:
			pygame.draw.rect(win, BLACK, (WIDTH*self.x, HEIGHT*self.y, WIDTH, HEIGHT), 1)
		if self.mateBool:
			pygame.draw.rect(win, DARKBLUE, (WIDTH*self.x, HEIGHT*self.y, WIDTH, HEIGHT), 1)

		food_number = ffont.render(str(self.food), True, BLACK)
		win.blit(food_number, (self.x*WIDTH+(WIDTH/2-food_number.get_width()/2), self.y*HEIGHT+(HEIGHT/2-food_number.get_height()/2)))

	def die(self):
		current.remove(self)
		gameMap[self.y][self.x] = 0

	def find_objective(self):
		for y in range((self.fdr*2)+1):
			t = self.y-self.fdr+y
			if t < 0:
				continue
			if t >= tilesy:
				continue
			for x in range((self.fdr*2)+1):
				t2 = self.x - self.fdr + x
				if t2 < 0:
					continue
				if t2 >= tilesx:
					continue
				if gameMap[t][t2] is not 0:
					if self.wanderBool:
						if "Player" in gameMap[t][t2]:
							if gameMap[t][t2][1].mateBool:
								self.objective = [t, t2]
					else:
						if "Apple" in gameMap[t][t2]:
							if (abs(gameMap[t][t2][1].y - self.y) + abs(gameMap[t][t2][1].x - self.x)) < self.steps:
								self.objective = [gameMap[t][t2][1].y, gameMap[t][t2][1].x]
								self.steps = (abs(self.objective[0] - self.y) + abs(self.objective[1] - self.x))
								self.wanderBool = False

	def whereToMove(self):
		if self.objective:
			if self.y == self.objective[0] and self.x == self.objective[1]:
				self.objective = []

		if self.objective:
			a = self.objective[0] - self.y
			b = self.objective[1] - self.x

			if not b:
				if a < 0:
					self.move(self.x, self.y-1)
				if a > 0:
					self.move(self.x, self.y+1)
			elif not a:
				if b < 0:
					self.move(self.x-1, self.y)
				if b > 0:
					self.move(self.x+1, self.y)
			elif random.choice([0,1]):
				if b < 0:
					self.move(self.x-1, self.y)
				if b > 0:
					self.move(self.x+1, self.y)
			else:
				if a < 0:
					self.move(self.x, self.y-1)
				if a > 0:
					self.move(self.x, self.y+1)

	def wander(self):
		self.wanderBool = True
		if random.choice([0,1]):
			self.move(self.x+random.choice([-1,1]), self.y)
		else:
			self.move(self.x, self.y+random.choice([-1,1]))

	def mate(self):
		self.wanderBool = True
		print("Wanderbool True")
		self.find_objective()
		self.whereToMove()

	def main(self):
		if self.food <= 0:
			self.die()
		if self.food > self.mos:
			self.mate()
		else:
			self.wc += 1
			if self.wc > (100-self.speed):
				self.wc = 0
				self.find_objective()
				if not self.objective:
					self.wander()
				self.whereToMove()

		self.draw(win)
                        

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
	fdr = random.randint(1,6)
	edr = random.randint(1,6)
	food = random.randint(40,120)
	fgt = random.randint(20,120)
	mos = random.randint(fgt+50,fgt+150)
	x = random.randint(0, tilesx-1)
	y = random.randint(0, tilesy-1)

	if gameMap[y][x] is 0:
		gameMap[y][x] = ["Player", Players(speed, fdr, edr, mos, fgt, food, True, x, y), speed, 100-speed, fdr, edr, mos]
		current.append(Players(speed, fdr, edr, mos, fgt, food, True, x, y))
		print(fdr)
	else:
		spawnPlayer()

#Place x players on random locations
for i in range(starting):
	spawnPlayer()
for i in range(startingFood):
	spawnFood()

while run:
	fc += 1
        
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

	win.fill(WHITE)

	if fc > fsr:
		fc = 0
		spawnFood()

	for player in current:
		player.main()

	for snacks in currentFood: #Draw all objects in class Players
		snacks.draw(win)

	clock.tick(1000)

	pygame.display.flip()

pygame.quit()