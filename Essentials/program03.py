from dUtilities import *

# -------------------------------------------------------------
title("Lists (true arrays not natively supported) --------------------")
# -------------------------------------------------------------

print('\nSyntax: cars = ["Ford", "Volvo", "BMW"]')
cars = ["Ford", "Volvo", "BMW"]
typeInfo('cars', cars)
typeInfo('len(cars)', len(cars))

# -------------------------------------------------------------
title("Iterating --------------------")
# -------------------------------------------------------------

print('\nTesting iteration methods...')

len = len(cars)
i = 0
for car in cars:
	writeIteration(i == 0, i, car)
	i += 1
print()

for i in range(3):
	writeIteration(i == 0, i, cars[i])
print()

i = 0
while (i < len):
	writeIteration(i == 0, i, cars[i])
	i += 1
print()

# -------------------------------------------------------------
title("Weird Iterating --------------------")
# -------------------------------------------------------------

print('\nFun times for all...')
i = 0
for y in range(10, 30, 3):
	writeIteration(y == 10, i, str(y))
	i += 1
print()

for i in range(12):
	write('.')
else:
	write("All done!")
print()

for i in range(12):
	write('.')
	if (i == 7):
		write("Oh no, I broke!")
		break
else:
	write("This will never print!")
print()

for i in range(12):
	write('.')
	if (i % 2 == 1):
		continue
	if (i == 7):
		write("Oh no, I broke!")
		break
else:
	write("I beat all the odds!")
print()

# -------------------------------------------------------------
title("Classy iteration --------------------")
# -------------------------------------------------------------

print("\nAdvanced iteration with enumerate class:")
typeInfo("enumerate(cars)", enumerate(cars))
for i, car in enumerate(cars):
    writeIteration(i == 0, i, car)
print()

programEnd()
