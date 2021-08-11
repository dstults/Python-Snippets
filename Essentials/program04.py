from dUtilities import *

# -------------------------------------------------------------
title("Basic List Functions")
# -------------------------------------------------------------

# Most of this was copied directly from here:
# https://dev.to/aumayeung/many-things-you-can-do-with-python-lists-you-may-have-missed-261p

print("\nfruits = ['apple', 'orange', 'orange', 'grape', 'pear']")
fruits = ['apple', 'orange', 'orange', 'grape', 'pear']
typeInfo("fruits", fruits)

print("\ntemp = fruits.sort()")
print("(Note: python list operations affect the list as is, temp will be 'NoneType'!!!)")
temp = fruits.sort()
typeInfo("temp", temp)
typeInfo("fruits", fruits)

print("\nfruits.reverse()")
fruits.reverse()
typeInfo("fruits", fruits)

print("\norange_count = fruits.count('orange')")
orange_count = fruits.count('orange')
typeInfo("orange_count", orange_count)

print("\nRemoving that duplicate orange...")
print("fruits2 = []")
fruits2 = []
print("[fruits2.append(f) for f in fruits if f not in fruits2]")
[fruits2.append(f) for f in fruits if f not in fruits2]
typeInfo("fruits", fruits)
typeInfo("fruits2", fruits2)

print("\norange_count = fruits2.count('orange')")
orange_count = fruits2.count('orange')
typeInfo("orange_count", orange_count)

# -------------------------------------------------------------
title("More Basic List Functions")
# -------------------------------------------------------------

print("\nshallowCopy = fruits.copy()")
shallowCopy = fruits.copy()
typeInfo("shallowCopy", shallowCopy)

# -------------------------------------------------------------
title("Pop and Append ('push') and Insert ('shift') and Pop(0) ('unshift')")
# -------------------------------------------------------------

print('\n"Pushing" "cherry"... ==> fruits.append("cherry")')
fruits.append("cherry")
print(fruits)
print("Popping it ...")
typeInfo("fruits.pop()", fruits.pop())
print(fruits)

print('\n"Shifting" "kiwi"... ==> fruits.insert(0, "kiwi")')
fruits.insert(0, "kiwi")
print(fruits)
print('"Unshifting" it...')
typeInfo("fruits.pop(0)", fruits.pop(0))
print(fruits)

programEnd()
