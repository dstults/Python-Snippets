
window = tk.Tk()
window.title("The Big Calculator\u2122")
greeting = tk.Label(text="Welcome!")
window.geometry("480x250")
window.resizable(width=False, height=False)

buttonWidth = 40
buttonHeight = 30
button_margin = 10
x_offset = 20
y_offset = 20

def getX(input):
	return x_offset + input * (buttonWidth + button_margin)

def getY(input):
	return y_offset + input * (buttonHeight + button_margin)

def getWidth(input):
	return input * buttonWidth + (input - 1) * button_margin
	
def getHeight(input):
	return input * buttonHeight + (input - 1) * button_margin

# numbers, decimal
cnt = 0
for i in reversed(range(3)):
	btn_y = y_offset + (buttonHeight + button_margin) * i
	for j in range(3):
		cnt += 1
		btn_x = x_offset + (buttonWidth + button_margin) * j
		button = tk.Button(text=cnt, command=lambda i=cnt: textBox.insert(tk.END, i))
		button.place(x=getX(j), y=getY(i), height=getHeight(1), width=getWidth(1))

textBox = tk.Text(height=4, width=28)
textBox.place(x=getX(5), y=getY(0), height=getHeight(3), width=getWidth(4))

# places an output box under the input box
outputBox = tk.Text(height=4, width=28)
outputBox.place(x=getX(5), y=getY(3), height=getHeight(1.5), width=getWidth(4))

posNeg = tk.Button(text='+/-', height=getHeight(1), width=getWidth(1), command=lambda: swapPositiveNegative())
posNeg.place(x=getX(0), y=getY(3), height=getHeight(1), width=getWidth(1))
zero = tk.Button(text=0, command=lambda i=i: textBox.insert(tk.END, 0))
zero.place(x=getX(1), y=getY(3), height=getHeight(1), width=getWidth(1))
point = tk.Button(text='.', height=getHeight(1), width=getWidth(1), command=lambda: appendpoint())
point.place(x=getX(2), y=getY(3), height=getHeight(1), width=getWidth(1))

# special case buttons
plus = tk.Button(text='+', command=lambda: textBox.insert(tk.END, " + "))
plus.place(x=getX(3), y=getY(0), height=getHeight(1), width=getWidth(1))
minus = tk.Button(text='-', command=lambda: textBox.insert(tk.END, " - "))
minus.place(x=getX(3), y=getY(1), height=getHeight(1), width=getWidth(1))
times = tk.Button(text='x', command=lambda: textBox.insert(tk.END, " * "))
times.place(x=getX(3), y=getY(2), height=getHeight(1), width=getWidth(1))
divide = tk.Button(text='\u00F7', command=lambda: textBox.insert(tk.END, " / "))
divide.place(x=getX(3), y=getY(3), height=getHeight(1), width=getWidth(1))
clear = tk.Button(text='C', command=lambda: deleteBoxes())
clear.place(x=getX(4), y=getY(0), height=getHeight(1), width=getWidth(1))
equals = tk.Button(text="=", command=lambda: calculate())
equals.place(x=getX(4), y=getY(1), height=getHeight(3), width=getWidth(1))
Backspace = tk.Button(text='\u2190', command=lambda: textBox.delete("end-2c"))
Backspace.place(x=getX(4), y=getY(4), height=getHeight(1), width=getWidth(1))
exponent = tk.Button(text='^', command=lambda: textBox.insert(tk.END, " ** "))
exponent.place(x=getX(3), y=getY(4), height=getHeight(1), width=getWidth(1))
Answer = tk.Button(text='ans', command=lambda: textBox.insert(tk.END, outputBox.get("1.0", "end-1c")))
Answer.place(x=getX(4), y=getY(5), height=getHeight(1), width=getWidth(1))


# constant buttons
e = tk.Button(text="e", command=lambda: textBox.insert(tk.END, "e"))
e.place(x=getX(1), y=getY(4), height=getHeight(1), width=getWidth(1))
pi = tk.Button(text="\u03C0", command=lambda: textBox.insert(tk.END, "\u03C0"))
pi.place(x=getX(2), y=getY(4), height=getHeight(1), width=getWidth(1))

# button that flips to other functions
funcs = tk.Button(text="funcs", command=lambda: textBox.insert(tk.END, "\u2665")) # PLACEHOLDER FOR FUTURE BUTTON
funcs.place(x=getX(0), y=getY(4), height=getHeight(1), width=getWidth(1))
	# functions to add (for actual calculations, the math library will be used):
	# log_a(x)
	# ln(x)
	# cos(x)
	# sin(x)
	# tan(x)
	# sec(x)
	# csc(x)
	# cot(x)
	# |x|
	# d/dx
	# (sigma?)
	# sqrt(x)

