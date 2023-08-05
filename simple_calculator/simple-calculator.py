from tkinter import *
from tkinter.messagebox import *
from math import *

def input(num):
	global ip_eq
	ip_eq = ip_eq + str(num)
	eq_label.set(str(ip_eq))

def divide_percents(numer):
	numer_rev = numer[::-1]
	percent_rev = numer_rev.find("%")
	#print("numer_rev: ", numer_rev)
	div_rev = numer_rev.find("/")
	#print("div_rev: ", div_rev)
	#print(div_rev, numer_rev[div_rev - 1].isnumeric(), numer_rev[div_rev + 1])
	if (div_rev != -1) and (numer_rev[div_rev - 1].isnumeric()) and (numer_rev[div_rev + 1] == "%"):
		numerator = numer_rev[div_rev+1: len(numer_rev)]
		denominator = numer_rev[0: div_rev]
		numerator = numerator[::-1]
		denominator = denominator[::-1]
		numerator = divide_percents(numerator)
		percent_num = numerator.find("%")
		percent_den = denominator.find("%")
		#print("numerator: ", numerator,"denominator: ", denominator)
		if (percent_num == 0) or (percent_den == 0):	
			showerror("'%' Error", "Syntax Error: % cannot be before a number")
			return eq_label.set("Error")
		if (percent_num + 1 != len(numerator)):	
			if (numerator[percent_num + 1].isnumeric()) and (percent_num != -1):
				showerror("'%' Error", "Syntax Error: % should not\nbe followed by a number.")
				return eq_label.set("Error")
		if (percent_den + 1 != len(denominator)):	
			if (denominator[percent_den + 1].isnumeric()) and (percent_den != -1):
				showerror("'%' Error", "Syntax Error: % should not\nbe followed by a number.")
				return eq_label.set("Error")
		numerator = numerator.replace("%", "/100")
		denominator = denominator.replace("%", "/100")
		#print("numerator: ", numerator,"denominator: ", denominator)
		sol = str(eval(numerator)/eval(denominator))
		print("sol: ", sol)
		return sol
	elif (div_rev == -1):
		return numer
	elif (div_rev != -1) and (percent_rev == -1):
		return numer
	elif (div_rev != -1) and (numer_rev[div_rev + 1] != "%"):
		return numer
	else:
		showerror("Error", "Invalid Input")
		return eq_label.set("Syntax Error")
def equals():
	try:
		global ip_eq
		#print("1st: ", ip_eq)
		if (ip_eq == ""):
			showerror("Input Error", "Input cannot be empty")
			return eq_label.set("")
		
		percent = ip_eq.find("%")
		
		#print("ip_eq[percent + 1]: ", ip_eq[percent + 1])
		#print("ip_eq[percent + 1].isnumeric: ", ip_eq[percent + 1].isnumeric())
		
		if (percent == 0):	
			showerror("'%' Error", "Syntax Error: % cannot be\nat the start")
			return eq_label.set("Error")
		if (percent + 1 != len(ip_eq)):	
			if (ip_eq[percent + 1].isnumeric()) and (percent != -1):
				showerror("'%' Error", "Syntax Error: % should not\nbe followed by a number.")
				return eq_label.set("Error")
		
		ip_eq = divide_percents(ip_eq)
		if ip_eq is None:
			ip_eq = "Error"
			eq_label.set(ip_eq)
		else:			
			if (percent != -1):
				ip_eq = ip_eq.replace("%", "/100")
			mul = ip_eq.find("x")
			#print("mul:", mul)
		
			if (ip_eq[mul] == "x") and (ip_eq != -1):
				ip_eq = ip_eq.replace("x", "*")
			#print("after mul: ", ip_eq)

			ans = str(eval(ip_eq))
			eq_label.set(ans)
			ip_eq = ans
	
	except ZeroDivisionError:
		eq_label.set("Error")
		showerror("Error", "Cannot divide by 0")
	
	except SyntaxError:
		eq_label.set("Error")
		showerror("Error", "Syntax Error")
	except AttributeError:
		eq_label.set("Error")
		showerror("Error", "Attribute Error")

def clear():
	global ip_eq
	eq_label.set("")
	ip_eq = ""

def revert():
	global ip_eq
	ip_eq = ip_eq[:len(ip_eq) - 1]
	eq_label.set(str(ip_eq))

mw = Tk()
mw.title("Calculator")
mw.geometry("600x850+700+75")
mw.config(bg = "gray16")
f = ("DejaVu Sans", 25)
f1 = ("DejaVu Sans", 15)

ip_eq = ""

eq_label = StringVar()
eq_label.set("")

lab_eq = Label(mw, textvariable = eq_label, font = f, width = 25, height = 2, bg = "white")
lab_eq.pack(pady = 20)

frame = Frame(mw)
frame.pack()

btn_obracket = Button(frame, text = '(', width = 8, height = 4,  fg = "cyan", bg = "gray18", font = f1, command =  lambda: input('('))
btn_obracket.grid(row = 0, column = 0)

btn_cbracket = Button(frame, text = ')', width = 8, height = 4,  fg = "cyan", bg = "gray18", font = f1, command =  lambda: input(')'))
btn_cbracket.grid(row = 0, column = 1)

btn_1 = Button(frame, text = 1, width = 8, height = 4,  fg = "gray98", bg = "gray18", font = f1, command = lambda: input(1))
btn_1.grid(row = 1, column = 0)

btn_2 = Button(frame, text = 2, width = 8, height = 4,  fg = "gray98", bg = "gray18", font = f1, command = lambda: input(2))
btn_2.grid(row = 1, column = 1)

btn_3 = Button(frame, text = 3, width = 8, height = 4,  fg = "gray98", bg = "gray18", font = f1, command = lambda: input(3))
btn_3.grid(row = 1, column = 2)

btn_4 = Button(frame, text = 4, width = 8, height = 4,  fg = "gray98", bg = "gray18", font = f1, command = lambda: input(4))
btn_4.grid(row = 2, column = 0)

btn_5 = Button(frame, text = 5, width = 8, height = 4,  fg = "gray98", bg = "gray18", font = f1, command = lambda: input(5))
btn_5.grid(row = 2, column = 1)

btn_6 = Button(frame, text = 6, width = 8, height = 4,  fg = "gray98", bg = "gray18", font = f1, command = lambda: input(6))
btn_6.grid(row = 2, column = 2)

btn_7 = Button(frame, text = 7, width = 8, height = 4,  fg = "gray98", bg = "gray18", font = f1, command = lambda: input(7))
btn_7.grid(row = 3, column = 0)

btn_8 = Button(frame, text = 8, width = 8, height = 4,  fg = "gray98", bg = "gray18", font = f1, command = lambda: input(8))
btn_8.grid(row = 3, column = 1)

btn_9 = Button(frame, text = 9, width = 8, height = 4,  fg = "gray98", bg = "gray18", font = f1, command = lambda: input(9))
btn_9.grid(row = 3, column = 2)

btn_0 = Button(frame, text = 0, width = 8, height = 4,  fg = "gray98", bg = "gray18", font = f1, command = lambda: input(0))
btn_0.grid(row = 4, column = 0)

btn_plus = Button(frame, text = '+', width = 8, height = 4,  fg = "cyan", bg = "gray18", font = f1, command =  lambda: input('+'))
btn_plus.grid(row = 1, column = 3)

btn_minus = Button(frame, text = '-', width = 8, height = 4,  fg = "cyan", bg = "gray18", font = f1, command = lambda: input('-'))
btn_minus.grid(row = 2, column = 3)

btn_mul = Button(frame, text = 'x', width = 8, height = 4,  fg = "cyan", bg = "gray18", font = f1, command = lambda: input('x'))
btn_mul.grid(row = 3, column = 3)

btn_div = Button(frame, text = '/', width = 8, height = 4,  fg = "cyan", bg = "gray18", font = f1, command = lambda: input('/'))
btn_div.grid(row = 4, column = 3)

btn_decimal = Button(frame, text = '.', width = 8, height = 4,  fg = "gray98", bg = "gray18", font = f1, command = lambda: input('.'))
btn_decimal.grid(row = 4, column = 1)

btn_percent = Button(frame, text = '%', width = 8, height = 4,  fg = "cyan", bg = "gray18", font = f1, command = lambda: input('%'))
btn_percent.grid(row = 0, column = 2)

btn_clear = Button(mw, text = "C", width = 34, height = 2,  fg = "gray18", font = f1, bg = "cyan", command = clear)
btn_clear.place(x = 74, y =695)

btn_equals = Button(frame, text = '=', width = 8, height = 4,  fg = "cyan", bg = "gray18", font = f1, command = equals)
btn_equals.grid(row = 4, column = 2)

btn_revert = Button(frame, text = "⌫", width = 8, height = 4,  fg = "gray18", font = f1, bg= "cyan", command = revert)
btn_revert.grid(row = 0, column = 3)

label = Label(mw, text = "Calculator App ⓒ", font = ("Coolvetica", 8), fg = "gray98", bg = "gray16").place(x = 255, y = 800)

def on_closing():
	if askokcancel("Quit", "Do you want to quit?"):
		mw.destroy()
mw.protocol("WM_DELETE_WINDOW", on_closing)

mw.mainloop()