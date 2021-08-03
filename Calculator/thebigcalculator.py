import tkinter as tk
import math

# appends a point, if there isn't one already in string
def appendpoint():
	input = textBox.get("1.0", tk.END)
	if '.' not in input and len(input) > 1:
		textBox.insert(tk.END, '.')
	# if nothing is in box add a 0 before point
	elif len(input) == 1:
		textBox.insert(tk.END, '0.')

def deleteBoxes():
	textBox.delete("1.0", tk.END)
	outputBox.delete("1.0", tk.END)

# makes sure there is something in textbox before adding 0, so we can't get something like "029"
def appendzero():
	if len(textBox.get("1.0", tk.END)) > 1:
		textBox.insert(tk.END, 0)
# (4 / 2 + 3) - (3(3*2))
# figure out how to split up terms, maybe make a separate method to split terms up?
def calculate():
	outputBox.delete("1.0", tk.END)
	rawInput = textBox.get("1.0", tk.END)
	calculations = eval(rawInput)
	outputBox.insert(tk.END, calculations)


def swapPositiveNegative():
	iloveyou = 1

def searchparenthesis(input):
	i = 0
	numParens = 0
	while(i<len(input)):
		if(input[i] == "("):
			numParens += 1
		elif(input[i] == ")"):
			numParens -= 1

exec(open("thebigcalculator_gui.py").read())

window.mainloop()
