from tkinter import *
from tkinter.messagebox import *
from datetime import *
import time
import pytz

def open_sww():
	sww.deiconify()
	root.withdraw()
def close_sww():
	root.deiconify()
	sww.withdraw()
def open_ctw():
	ctw.deiconify()
	root.withdraw()
def close_ctw():
	root.deiconify()
	ctw.withdraw()

wc_stop = 0

def timezone():
	global wc_stop
	if wc_stop == 0:
		timezones = ['Asia/Kolkata', 'America/New_York', 'Australia/Sydney', 'Europe/London']
	
		tz1 = pytz.timezone(timezones[0])
		local_time = datetime.now(tz1).strftime("%a %H:%M:%S")
		lab_wcw_tz1.configure(text = "India (Kolkata)")
		lab_wcw_time1.configure(text = local_time)
		lab_wcw_time1.after(1000, timezone)
	
		tz2 = pytz.timezone(timezones[1])
		local_time = datetime.now(tz2).strftime("%a %H:%M:%S")
		lab_wcw_tz2.configure(text = "USA (New York)")
		lab_wcw_time2.configure(text = local_time)
		lab_wcw_time2.after(1000, timezone)

		tz3 = pytz.timezone(timezones[2])
		local_time = datetime.now(tz3).strftime("%a %H:%M:%S")
		lab_wcw_tz3.configure(text = "Australia (Sydney)")
		lab_wcw_time3.configure(text = local_time)
		lab_wcw_time3.after(1000, timezone)
	
		tz4 = pytz.timezone(timezones[3])
		local_time = datetime.now(tz4).strftime("%a %H:%M:%S")
		lab_wcw_tz4.configure(text = "UK (London)")
		lab_wcw_time4.configure(text = local_time)
		lab_wcw_time4.after(1000, timezone)

def open_wcw():
	global wc_stop
	wc_stop = 0
	wcw.deiconify()
	root.withdraw()
	timezone()
def close_wcw():
	global wc_stop
	wc_stop = 1
	root.deiconify()
	wcw.withdraw()
def open_acw():
	acw.deiconify()
	root.withdraw()
def close_acw():
	root.deiconify()
	acw.withdraw()

hr = "00"
min = "00"
sec = "00"
stop = 0
def start_sw():
	global hr, min, sec, stop
	hr = int(hr)
	min = int(min)
	sec = int(sec)
	time.sleep(1)
	sec += 1
	if sec == 60:
		sec = 0
		min += 1
	if min == 60:
		min = 0
		hr += 1
	if stop == 0:
		lab_sw.after(100, start_sw)
		hr = "{:02d}".format(hr)
		min = "{:02d}".format(min)
		sec = "{:02d}".format(sec)
		lab_sw.configure(text = f"{hr}:{min}:{sec}")
		btn_sw_start.pack_forget()
def stop_sw():
	global stop
	stop = 1
	btn_sw_stop.pack_forget()
	btn_sw_reset.pack_forget()
	btn_sw_back.pack_forget()
	btn_sw_start.pack(pady = 10)
	btn_sw_stop.pack(pady = 10)
	btn_sw_reset.pack(pady = 10)
	btn_sw_back.pack(pady = 10)

	btn_sw_start.configure(text = "Restart" ,command = restart_sw)
	
def restart_sw():
	global stop
	stop = 0
	start_sw()

def reset_sw():
	global hr, min, sec, stop
	hr = "00"
	min = "00"
	sec = "00"
	stop = 0
	lab_sw.configure(text = f"{hr}:{min}:{sec}")
	btn_sw_start.configure(text = "Start", command = start_sw)

ct_stop = 0

def start_ct():
	global ct_stop
	ct_stop = 0
	try:
		temp = int(hour.get())*3600 + int(minute.get())*60 + int(second.get())
	except:
		showerror("Error", "Invalid Input")
		temp = -1
	while temp > -1:
		if ct_stop == 0:
			mins,secs = divmod(temp,60)
			hours = 0
			if mins >60:
				hours, mins = divmod(mins, 60)
			hour.set("{:02d}".format(hours))
			minute.set("{:02d}".format(mins))
			second.set("{:02d}".format(secs))
  
			ctw.update()
			if (temp != 0):
				time.sleep(1)
			if (temp == 0):
				time.sleep(0.2)
				showinfo("Time Countdown", "Time's up ")
			temp -= 1
	
			btn_ctw_start.configure(text = "Pause", command = pause_ct)
			if (temp == 0):
				btn_ctw_start.configure(text = "Start", command = start_ct)
			btn_ctw_reset = Button(ctw, text = "Reset", font = f1, width = 10, bg = "peachpuff", command = reset_ct)
			btn_ctw_reset.place(x = 260, y = 275)
		elif ct_stop == 1:
			btn_ctw_start.configure(text = "Restart", command = start_ct)
			btn_ctw_reset = Button(ctw, text = "Reset", font = f1, width = 10, bg = "peachpuff", command = reset_ct)
			btn_ctw_reset.place(x = 260, y = 275)
			temp = -1
		elif ct_stop == 2:
			btn_ctw_reset.place_forget()
			temp = -1
			
	if ct_stop == 1: 
		btn_ctw_start.configure(text = "Restart", command = start_ct)
	elif ct_stop == 2: 
		btn_ctw_start.configure(text = "Start", command = start_ct)
	#self-note - when timer reaches 0:0:0 and ct_stop remains 0
	elif ct_stop == 0:
		btn_ctw_start.configure(text = "Start", command = start_ct)
		hour.set("00")
		minute.set("00")
		second.set("00")
			
def pause_ct():
	global ct_stop
	ct_stop = 1
	
def reset_ct():
	global ct_stop
	ct_stop = 2
	hour.set("00")
	minute.set("00")
	second.set("00")
	btn_ctw_start.configure(text = "Start", command = start_ct)

ac_stop = False
show_msg = 0

def set_ac():
	global ac_stop, show_msg
	if ac_stop == False:
		try:
			test_hr = sethour.get()
			if (test_hr == "") or (test_hr.strip() == "") or (not test_hr.isnumeric()):
				raise Exception("No blank spaces or alphabets allowed")
			elif int(test_hr) == 24:
				raise  Exception("Do you mean '00' in hours input?")
			elif (int(test_hr) < 0) or (int(test_hr) > 23):
				raise Exception("Input values for hour should be within 0 - 23")
			else:
				hr = test_hr
			test_min = setminute.get()
			if (test_min == "") or (test_min.strip() == "")  or (not test_min.isnumeric()):
				raise Exception("No blank spaces or alphabets allowed")
			elif (int(test_min) < 0) or (int(test_min) > 59):
				raise Exception("Input values for minutes should be within 0 - 59")
			else:
				min = test_min
			test_sec = setsecond.get()
			if (test_sec == "") or (test_sec.strip() == "") or (not test_sec.isnumeric()):
				raise Exception("No blank spaces or alphabets allowed")
			elif (int(test_sec) < 0) or (int(test_sec) > 59):
				raise Exception("Input values for seconds should be within 0 - 59")
			else:
				sec = test_sec
			if show_msg == 0:
				showinfo("Success", "Alarm has been set!")
			show_msg = show_msg + 1
		except Exception as e:
			showerror("Input error", e)
			hr = ""
			min = ""
			sec = ""
			ent_acw_hrs.delete(0, END)
			ent_acw_min.delete(0, END)
			ent_acw_sec.delete(0, END)
			ent_acw_hrs.focus()
			clear_ac()
			btn_acw_set.place_forget()
			btn_acw_reset = Button(acw, text = "Reset", font = f1, width = 10, bg = "mediumslateblue", command = reset_ac)
			btn_acw_reset.place(x = 260, y = 200)
		
	
		dt_hr = datetime.now().strftime("%H")
		dt_min = datetime.now().strftime("%M")
		dt_sec = datetime.now().strftime("%S")

		if (str(hr) == dt_hr) and (str(min) == dt_min) and (str(sec) == dt_sec):
			showinfo("Alarm Reminder", "Your set alarm time as been reached")
			ent_acw_hrs.delete(0, END)
			ent_acw_min.delete(0, END)
			ent_acw_sec.delete(0, END)
			ent_acw_hrs.focus()
			clear_ac()
			btn_acw_set.place_forget()
			btn_acw_reset = Button(acw, text = "Set", font = f1, width = 10, bg = "mediumslateblue", command = reset_ac)
			btn_acw_reset.place(x = 260, y = 200)
		
		if ac_stop == False:
			lab_acw_time.after(1000, set_ac)

def clear_ac():	
	global ac_stop
	ent_acw_hrs.delete(0, END)
	ent_acw_min.delete(0, END)
	ent_acw_sec.delete(0, END)
	ent_acw_hrs.focus()
	ac_stop = True
def reset_ac():
	global ac_stop, show_msg
	ac_stop = False
	show_msg = 0
	set_ac()
	
	
root = Tk()
root.title("Digital Clock")
root.geometry("700x400+600+350")
root.configure(bg = "mediumspringgreen")
root.iconbitmap("digiclock.ico")
f = ("Fixedsys", 64)
f1 = ("Bergen Text", 25)
f2 = ("Arial", 48)

def time_change():
	x = datetime.now()
	time = x.strftime("%X")
	lab_time.configure(text = str(time))
	lab_time.after(1000, time_change)


lab_time = Label(root, font = f, bg = "honeydew")
time_change()
lab_time.pack(pady = 50)

btn_stopwatch = Button(root, text = "Stopwatch", font = f1, bg = "palegreen", width = 15, command = open_sww)
btn_stopwatch.place(x = 60, y = 200)

btn_timer = Button(root, text = "Countdown Timer", font = f1, bg = "palegreen", width = 15, command = open_ctw)
btn_timer.place(x = 360, y = 200)

btn_timer = Button(root, text = "World Clock", font = f1, bg = "palegreen", width = 15, command = open_wcw)
btn_timer.place(x = 60, y = 300)

btn_timer = Button(root, text = "Alarm", font = f1, bg = "palegreen", width = 15, command = open_acw)
btn_timer.place(x = 360, y = 300)


sww = Toplevel(root)
sww.title("Stopwatch")
sww.geometry("700x600+600+200")
sww.iconbitmap("sw.ico")
sww.configure(bg = "lightcoral")

lab_sw =  Label(sww, text = f"{hr}:{min}:{sec}",  font = f)
lab_sw.pack(pady = 50)
btn_sw_start = Button(sww, text = "Start", font = f1, width = 10, bg = "mistyrose", command = start_sw)
btn_sw_stop = Button(sww, text = "Stop", font = f1, width = 10, bg = "mistyrose", command = stop_sw)
btn_sw_reset = Button(sww, text = "Reset", font = f1, width = 10, bg = "mistyrose", command = reset_sw)
btn_sw_back = Button(sww, text = "Back", font = f1, width = 10, bg = "mistyrose", command = close_sww)
btn_sw_start.pack(pady = 10)
btn_sw_stop.pack(pady = 10)
btn_sw_reset.pack(pady = 10)
btn_sw_back.pack(pady = 10)

sww.withdraw()

ctw = Toplevel(root)
ctw.title("Countdown Timer")
ctw.geometry("700x500+600+250")
ctw.iconbitmap("ct.ico")
ctw.configure(bg = "sandybrown")

hour=StringVar()
minute=StringVar()
second=StringVar()

hour.set("00")
minute.set("00")
second.set("00")

lab_ctw_hms = Label(ctw, text = "Hours : Minutes : Seconds", font = f1, bg = "sandybrown")
ent_ctw_hrs = Entry(ctw, font = f2, width  = 2,  textvariable = hour)
label_ctw_col1 = Label(ctw, text = ":", font = f2, bg = "sandybrown")
ent_ctw_min = Entry(ctw, font = f2, width  = 2, textvariable = minute)
label_ctw_col2 = Label(ctw, text = ":", font = f2, bg = "sandybrown")
ent_ctw_sec = Entry(ctw, font = f2, width  = 2, textvariable = second)
btn_ctw_start = Button(ctw, text = "Start", font  = f1, width = 10, bg = "peachpuff", command = start_ct)
btn_ctw_back = Button(ctw, text = "Back", font  = f1, width = 10, bg = "peachpuff", command = close_ctw)


lab_ctw_hms.pack(pady = 10)
ent_ctw_hrs.place(x = 160, y  = 80)
label_ctw_col1.place(x = 260, y  = 80)
ent_ctw_min.place(x = 310, y  = 80)
label_ctw_col2.place(x = 410, y  = 80)
ent_ctw_sec.place(x = 460, y  = 80)
btn_ctw_start.place(x = 260, y = 200)
btn_ctw_back.place(x = 260, y = 350)
ctw.withdraw()

wcw = Toplevel(root)
wcw.title("World Clock")
wcw.geometry("850x500+525+150")
wcw.iconbitmap("wc.ico")
wcw.configure(bg = "dodger blue")

fr1 = Frame(wcw, bd = 5, bg = "palegreen")
fr1.place(x = 50, y = 50, width = 300, height = 120)

lab_wcw_tz1 = Label(fr1, font = f1, bg = "palegreen")
lab_wcw_time1 = Label(fr1, font = f1, bg = "palegreen")
lab_wcw_tz1.place(x = 20, y = 10)
lab_wcw_time1.place(x = 20, y = 60)

fr2 = Frame(wcw, bd = 5, bg = "palegreen")
fr2.place(x = 500, y = 50, width = 300, height = 120)

lab_wcw_tz2 = Label(fr2, font = f1, bg = "palegreen")
lab_wcw_time2 = Label(fr2, font = f1, bg = "palegreen")
lab_wcw_tz2.place(x = 20, y = 10)
lab_wcw_time2.place(x = 20, y = 60)

fr3 = Frame(wcw, bd = 5, bg = "palegreen")
fr3.place(x = 50, y = 250, width = 300, height = 120)

lab_wcw_tz3 = Label(fr3, font = f1, bg = "palegreen")
lab_wcw_time3 = Label(fr3, font = f1, bg = "palegreen")
lab_wcw_tz3.place(x = 20, y = 10)
lab_wcw_time3.place(x = 20, y = 60)

fr4 = Frame(wcw, bd = 5, bg = "palegreen")
fr4.place(x = 500, y = 250, width = 300, height = 120)

lab_wcw_tz4 = Label(fr4, font = f1, bg = "palegreen")
lab_wcw_time4 = Label(fr4, font = f1, bg = "palegreen")
lab_wcw_tz4.place(x = 20, y = 10)
lab_wcw_time4.place(x = 20, y = 60)

btn_wcw_back = Button(wcw, text = "<< Back", font = f1, width = 10, bg = "palegreen", command = close_wcw)
btn_wcw_back.place(x = 320, y = 400)

wcw.withdraw()

acw = Toplevel(root)
acw.title("Alarm")
acw.geometry("700x500+600+250")
acw.iconbitmap("ac.ico")
acw.configure(bg = "mediumpurple")

sethour=StringVar()
setminute=StringVar()
setsecond=StringVar()

lab_acw_time = Label(acw)
lab_acw_hms = Label(acw, text = "Hours : Minutes : Seconds", font = f1, bg = "mediumpurple")
ent_acw_hrs = Entry(acw, font = f2, width  = 2, textvariable = sethour)
label_acw_col1 = Label(acw, text = ":", font = f2, bg = "mediumpurple")
ent_acw_min = Entry(acw, font = f2, width  = 2, textvariable = setminute)
label_acw_col2 = Label(acw, text = ":", font = f2, bg = "mediumpurple")
ent_acw_sec = Entry(acw, font = f2, width  = 2, textvariable = setsecond)
btn_acw_set = Button(acw, text = "Set", font  = f1, width = 10, bg = "mediumslateblue", command = set_ac)
btn_acw_back = Button(acw, text = "Back", font  = f1, width = 10, bg = "mediumslateblue", command = close_acw)

lab_acw_hms.pack(pady = 10)
ent_acw_hrs.place(x = 160, y  = 80)
label_acw_col1.place(x = 260, y  = 80)
ent_acw_min.place(x = 310, y  = 80)
label_acw_col2.place(x = 410, y  = 80)
ent_acw_sec.place(x = 460, y  = 80)
btn_acw_set.place(x = 260, y = 200)
btn_acw_back.place(x = 260, y = 350)

acw.withdraw()

def on_closing():
	if askokcancel("Exit", "Do you want to exit?"):
		root.destroy()
acw.protocol("WM_DELETE_WINDOW", on_closing)
wcw.protocol("WM_DELETE_WINDOW", on_closing)
ctw.protocol("WM_DELETE_WINDOW", on_closing)
sww.protocol("WM_DELETE_WINDOW", on_closing)
root.protocol("WM_DELETE_WINDOW", on_closing)

root.mainloop()