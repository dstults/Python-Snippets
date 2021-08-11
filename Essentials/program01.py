from dUtilities import *

# -------------------------------------------------------------
title("stdout & concatenation:")
# -------------------------------------------------------------

print("Hello 'world'!")
print('Hello "world"!')
print("Hello \"world\"!")
print("Hello " + "world!")
print("Hello", "world!")           # Note: no space
mystring1 = "Hello " + "world!"    # type = string
mystring2 = "Hello ", "world!"     # type = list
print(mystring1)
print(mystring2)
print("Hello \"world\"!")

# -------------------------------------------------------------
title("String interpolation:")
# -------------------------------------------------------------

var1 = "my"
var2 = "big"
print(f"Hello {var1} world!")
print(f'Hello {var2} world!')

# -------------------------------------------------------------
title("stdin / conditionals / string case and find")
# -------------------------------------------------------------

haslove = input("Do you love me? ")
haslove = haslove.lower()
if (haslove.find("yes") >= 0 or haslove == "y"):
	print("Yay!")
elif (not haslove):
	print("Silence is painful.")
else:
	print("Darn it!")

# -------------------------------------------------------------
title("String split, join, replace")
# -------------------------------------------------------------

var3 = "Let's rock the house!"
print(var3)
print(var3.split(" "))
print("_".join(var3.split(" "))) # Not: var3.split(" ").join("_") !!!
print("-".join(var3.split(" ")).replace("_", "-"))

programEnd()
