
# console colors
CEND      = '\33[0m'
CBOLD     = '\33[1m'
CITALIC   = '\33[3m'
CURL      = '\33[4m'
CBLINK    = '\33[5m'
CBLINK2   = '\33[6m'
CSELECTED = '\33[7m'

CBLACK    = '\33[30m'
CRED      = '\33[31m'
CGREEN    = '\33[32m'
CYELLOW   = '\33[33m'
CBLUE     = '\33[34m'
CVIOLET   = '\33[35m'
CCYAN     = '\33[36m'
CWHITE    = '\33[37m'

CBLACKBG  = '\33[40m'
CREDBG    = '\33[41m'
CGREENBG  = '\33[42m'
CYELLOWBG = '\33[43m'
CBLUEBG   = '\33[44m'
CVIOLETBG = '\33[45m'
CCYANBG   = '\33[46m'
CWHITEBG  = '\33[47m'

CGREY     = '\33[90m'
CRED2     = '\33[91m'
CGREEN2   = '\33[92m'
CYELLOW2  = '\33[93m'
CBLUE2    = '\33[94m'
CVIOLET2  = '\33[95m'
CCYAN2    = '\33[96m'
CWHITE2   = '\33[97m'

def title(text):
	length = len(text) + 4
	print('\n' + "=" * length)
	print("| " + text + " |")
	print("=" * length)

def programEnd():
	print()
	print("-----------------------------------------")
	print("Program gracefully terminated.")
	print()
	print()

def typeInfo(name, var):
	print('"' + CWHITE2 + name + CEND + '" = ' + CGREEN2 + CBOLD + str(var) + CEND + " ... type: " + CCYAN2 + str(type(var)) + CEND)

def write(txt):
	print(txt, end = "")

def writeIteration(isFirst, i, val):
	if (not isFirst):
		write(CGREY + " ... " + CEND)
	write("[ (" + str(i + 1) + ") " + CYELLOW + val + CEND + " ]")

def printYellow(importantText):
	print(CYELLOW2 + importantText + CEND)
