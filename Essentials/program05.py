from dUtilities import *

# -------------------------------------------------------------
title("Basic Dictionary Functions")
# -------------------------------------------------------------

print("An empty dictionary: dic1 = {}")
dic1 = {}
typeInfo("dic1", dic1)

print("\nhero = {'name': 'Darren', 'title': 'the Clumsy', 'hp': 40, 'power': 5, 'defense': 1}")
hero = {'name': 'Darren', 'title': 'the Clumsy', 'hp': 40, 'power': 5, 'defense': 1}
typeInfo("hero", hero)
typeInfo("hero.name", hero['name'])
typeInfo("hero.hp", hero['hp'])

# -------------------------------------------------------------
title("More Basic Dictionary Functions")
# -------------------------------------------------------------

print ("\n 'in' :")
typeInfo("'power' in hero", 'power' in hero)
typeInfo("'maxHp' in hero", 'maxHp' in hero)

print("\nshallowHero = hero.copy()")
shallowHero = hero.copy()
typeInfo("shallowHero", shallowHero)

# -------------------------------------------------------------
title("Adding or Removing Keys")
# -------------------------------------------------------------

print('\nAdding')
print("hero['maxHp'] = 40")
hero['maxHp'] = 40
typeInfo("hero", hero)

print('\nRemoving')
print("del hero['maxHp']")
del hero['maxHp']
typeInfo("hero", hero)

# -------------------------------------------------------------
title("Clearing and Handling Exceptions")
# -------------------------------------------------------------

print('\nClearing and Deleting the dictionary (works with other data types)')
print("hero.clear()")
hero.clear()
typeInfo("hero", hero)
print("del hero")
del hero
try:
	typeInfo("hero", hero)
except NameError:
	printError("name 'hero' is not defined")

apples = 12
print("apples = 12")
typeInfo("apples", apples)
del apples
print("del apples")
try:
	typeInfo("apples", apples)
except NameError:
	printError("name 'apples' is not defined")

programEnd()
