#Importing modules
import random
import numpy as np
from pprint import pprint

#Game variables
x = 10
y = 5
a = 5
players = 10
gen = []

gameMap = [[[0 for i in range(a)] for b in range(x)] for u in range(y)]
pprint(gameMap)

#Generation variables
speed = 0
size = 0
fdr = 0 #FoodDetectionRange
edr = 0 #EnemyDetectionRange
mos = 0 #MatingOffSet

#Functions
def checkSurrounding(i, j, x, y):
	pass


#Place players on random locations
for i in range(players):
	gen = []
	for i in range(a): #Create random generation
		gen.append(random.randint(1, 1000))
	gameMap[random.randint(0, y-1)][random.randint(0, x-1)] = gen

pprint(gameMap)


