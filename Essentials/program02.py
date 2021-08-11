from dUtilities import *
import math

# -------------------------------------------------------------
title("Integers and Floats --------------------")
# -------------------------------------------------------------

print("\nInteger + Type...")
typeInfo("1", 1)
# Note the <Type> (class) of "type" is "type":
print("type's type: ", type(type(1)))

print("\nFloat...")
typeInfo("1.0", 1.0)

# integers automatically get converted to float if decimalized:
print("\nDivide by two...")
typeInfo("1 / 2", 1 / 2)
typeInfo("1.0 / 2", 1.0 / 2)

print("\nModulo preserves float as float but expect errors...")
typeInfo("17 % 5", 17 % 5)
typeInfo("17.0 % 5", 17.0 % 5)
typeInfo("17.3 % 5", 17.3 % 5)

print("\nString and float conversion to integer & explicit conversion to float...")
typeInfo("int('1')", int('1'))
typeInfo("int(1.9)", int(1.9)) # the .9 will be dropped and not rounded
typeInfo("float(1)", float(1))

# -------------------------------------------------------------
title("Rounding --------------------")
# -------------------------------------------------------------

print("\nRounding works as expected for whole numbers, but when rounding to decimals it seems broken:")
typeInfo("round(1.49)", round(1.49))
typeInfo("round(1.50)", round(1.50))
typeInfo("round(1.51)", round(1.51))
typeInfo("round(1.504, 2)", round(1.504, 2))
typeInfo("round(1.505, 2)", round(1.505, 2))
typeInfo("round(1.506, 2)", round(1.506, 2))

print("\nCeiling and Floor (also trunc) (requires 'import math'):")
typeInfo("math.ceil(3.5)", math.ceil(3.5))
typeInfo("math.floor(3.5)", math.floor(3.5))
typeInfo("math.trunc(3.5)", math.trunc(3.5))

# -------------------------------------------------------------
title("Convert literals and strings to and from Binary/Hexidecimal --------------------")
# -------------------------------------------------------------

typeInfo("bin(120)", bin(120))
typeInfo("0b1111000", 0b1111000)
typeInfo("int('0b1111000', 2)", int('0b1111000', 2))
typeInfo("hex(120)", hex(120))
typeInfo("0x78", 0x78)
typeInfo("int('0x78', 16)", int('0x78', 16))

programEnd()
