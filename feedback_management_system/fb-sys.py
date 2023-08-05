from tkinter import *
from tkinter.messagebox import *
from tkinter.scrolledtext import *
from sqlite3 import *

def save():
	con = None
	try:
		con = connect("fb.db")
		cursor = con.cursor()
		sql = "insert into feedback values('%s', '%s', '%s', '%d', '%s')"
		
		test_first_name = ent_user_first_name.get()
		test_first_name = test_first_name.strip()
		if (test_first_name == "") or (not test_first_name.isalpha()):
			return showerror("Input Error", "First name cannot be blank or not alphabetical")
		first_name = test_first_name

		test_last_name = ent_user_last_name.get()
		test_last_name = test_last_name.strip()
		if (test_last_name == "") or (not test_last_name.isalpha()):
			return showerror("Input Error", "Last name cannot be blank or not alphabetical")
		last_name = test_last_name

		test_email_add = ent_user_email.get()
		test_email_add = test_email_add.strip()
		if (test_email_add == "") or (test_email_add.find("@") == -1) or (test_email_add[-4:] != ".com"):
			return showerror("Input Error", "Email Address cannot be blank and must end with @[Domain Name].com")
		email = test_email_add
		
		stars = s.get()
		test_feedback = st_user_feedback.get(1.0, END)
		test_feedback = test_feedback.strip()
		if (test_feedback == ""):
			return showinfo("Message", "Please enter some feedback since this is a feedback app")
		feedback = test_feedback
		cursor.execute(sql % (first_name, last_name, email, stars, feedback))
		con.commit()
		showinfo("Success", "Records Saved")
	except Exception as e:
		con.rollback()
		showerror("SQL error", e)
	finally:
		if con is not None:
			con.close()
		ent_user_first_name.delete(0, END)
		ent_user_last_name.delete(0, END)
		ent_user_email.delete(0, END)
		s.set(5)
		st_user_feedback.delete(1.0, END)
		ent_user_first_name.focus()

def open_alw():
	alw.deiconify()

def close_alw():
	alw.withdraw()

admin_login_status = False

def login():
	global admin_login_status
	con = None
	try:
		con = connect("admin.db")
		cursor = con.cursor()
		sql = "select * from credentials where email = '%s'"
		email_add = ent_alw_email.get()
		email = email_add.strip()
		password = ent_alw_password.get()
		password = password.strip()
		if (email == "") and (password == ""):
			return showerror("Failed Login", "Please fill the fields with a valid details to login.")
		elif (email == ""):
			return showerror("Failed Login", "Please fill the email address field with a valid email address to login.")
		elif (password == ""):
			return showerror("Failed Login", "Please fill the password field with a valid password to login.")	 
		cursor.execute(sql % (email))
		data = cursor.fetchall()
		for d in data:
			if (d[0] == email) and (d[1] == password):
				showinfo("Success", "Logged in successfully")
				admin_login_status = True
			elif (d[0] == email) and (d[1] != password):
				showerror("Failed Login", "Incorrect password, please try again")
			elif (d[0] != email):
				showerror("Failed Login", "Email is not found, please try again")
	
	except Exception as e:
		showerror("SQL Error", e)
	finally:
		if con is not None:
			con.close()
		ent_alw_email.delete(0, END)
		ent_alw_password.delete(0, END)
		ent_alw_email.focus()
	
	if admin_login_status == True:
		open_aw()
		alw.withdraw()

def open_aw():
	aw.deiconify()
	root.withdraw()
def close_aw():
	global admin_login_status
	aw.withdraw()
	root.deiconify()
	admin_login_status = False

def show():
	sw.deiconify()
	root.withdraw()
	con  = None
	fb = ""
	try:
		con = connect("fb.db")
		cursor = con.cursor()
		sql = "select rowid, * from feedback"
		cursor.execute(sql)
		data = cursor.fetchall()
		for d in data:
			fb += "ID: " + str(d[0]) + " | " + "Name: " + str(d[1]) + " " + str(d[2]) +  " | " + "Email: " + str(d[3]) +  " | " + "Rating: " + str(d[4]) + " | " + "Feedback: " + str(d[5]) + "\n"
	
	except Exception as e:
		showerror("SQL error", e)
	finally:
		if con is not None:
			con.close()
	
	st_sw_feedback.insert(INSERT, fb)
		
def close_sw():
	st_sw_feedback.delete(1.0, END)
	sw.withdraw()

def open_uw():
	uw.deiconify()
	root.withdraw()

def close_uw():
	uw.withdraw()

def update():
	con = None
	try:
		con = connect("fb.db")
		cursor = con.cursor()
		sql = "update feedback set first_name = '%s', last_name = '%s', email = '%s', stars = '%d', feedback = '%s' where rowid = '%d'"
		
		test_first_name = ent_uw_first_name.get()
		test_first_name = test_first_name.strip()
		if (test_first_name == "") or (not test_first_name.isalpha()):
			return showerror("Input Error", "First name cannot be blank or not alphabetical")
		first_name = test_first_name

		test_last_name = ent_uw_last_name.get()
		test_last_name = test_last_name.strip()
		if (test_last_name == "") or (not test_last_name.isalpha()):
			return showerror("Input Error", "Last name cannot be blank or not alphabetical")
		last_name = test_last_name

		test_email_add = ent_uw_email.get()
		test_email_add = test_email_add.strip()
		if (test_email_add == "") or (test_email_add.find("@") == -1) or (test_email_add[-4:] != ".com"):
			return showerror("Input Error", "Email Address cannot be blank and must end with @[Domain Name].com")
		email = test_email_add
		
		stars = r.get()
		test_feedback = st_uw_feedback.get(1.0, END)
		test_feedback = test_feedback.strip()
		if (test_feedback == ""):
			return showinfo("Message", "Please enter some feedback since this is a feedback app")
		feedback = test_feedback
		
		test_rowid = int(ent_uw_id.get())
		if (test_rowid == ""):
			return showerror("Input Error", "ID cannot be empty")
		if (test_rowid < 1):
			return showerror("Input Error", "ID can only be more than 0")
		if (not str(test_rowid).isnumeric):
			return showerror("Input Error", "ID can only be an integer")
		rowid = test_rowid
		

		cursor.execute(sql % (first_name, last_name, email, stars, feedback, rowid))
		if cursor.rowcount == 1:
			con.commit()
			showinfo("Success", "Record Updated")
		else:
			showinfo("Failed", "Record does not exist")
	except Exception as e:
		con.rollback()
		showerror("SQL error", e)
	finally:
		if con is not None:
			con.close()
		ent_uw_first_name.delete(0, END)
		ent_uw_last_name.delete(0, END)
		ent_uw_email.delete(0, END)
		r.set(5)
		st_uw_feedback.delete(1.0, END)
		ent_uw_id.focus()

def open_dw():
	dw.deiconify()
	root.withdraw()

def close_dw():
	dw.withdraw()

def delete():
	con = None
	try:
		con = connect("fb.db")
		cursor = con.cursor()
		sql = "delete from feedback where rowid = '%d'"
		test_rowid = int(ent_dw_id.get())
		if (test_rowid == 0):
			return showerror("Input Error", "ID cannot be empty")
		if (test_rowid < 1):
			return showerror("Input Error", "ID can only be more than 0")
		if (not str(test_rowid).isnumeric):
			return showerror("Input Error", "ID can only be an integer")
		rowid = test_rowid
		cursor.execute(sql % (rowid))
		if cursor.rowcount == 1:
			con.commit()
			showinfo("Success", "Record Deleted")
		else:
			showinfo("Failed", "Record does not exist")
	except Exception as e:
		con.rollback()
		showerror("SQL error", e)
	finally:
		if con is not None:
			con.close()
		ent_dw_id.delete(0, END)
		ent_dw_id.focus()
		


root = Tk()
root.title("Feedback Management System")
root.geometry("600x920+600+50")
root.configure(bg = "grey16")

f = ("Apple Garamond", 20)
f1 = ("Apple Garamond", 15)

lab_user_first_name = Label(root, text = "Enter first name", font = f, bg = "grey16", fg = "grey98")
ent_user_first_name = Entry(root, font = f)
lab_user_last_name = Label(root, text = "Enter last name", font = f, bg = "grey16", fg = "grey98")
ent_user_last_name = Entry(root, font = f)
lab_user_email = Label(root, text = "Enter email address", font = f, bg = "grey16", fg = "grey98")
ent_user_email = Entry(root, font = f)

lab_user_feedback = Label(root, text = "Feedback", font = f, bg = "grey16", fg = "grey98")

s = IntVar()
s.set(5)
rb_1 = Radiobutton(root, text = "1★", font = f, bg = "grey16", fg = "grey98", variable = s, value = 1)
rb_2 = Radiobutton(root, text = "2★", font = f, bg = "grey16", fg = "grey98", variable = s, value = 2)
rb_3 = Radiobutton(root, text = "3★", font = f, bg = "grey16", fg = "grey98", variable = s, value = 3)
rb_4 = Radiobutton(root, text = "4★", font = f, bg = "grey16", fg = "grey98", variable = s, value = 4)
rb_5 = Radiobutton(root, text = "5★", font = f, bg = "grey16", fg = "grey98", variable = s, value = 5)

st_user_feedback = ScrolledText(root, font = f, width = 35, height = 10)

btn_save = Button(root, text = "Save", font = f, width = 14, bg = "aqua", command = save)
btn_admin_login = Button(root, text = "Admin Log- In", font = f, width = 14, bg = "aqua", command = open_alw)

lab_user_first_name.pack(pady = 10)
ent_user_first_name.pack(pady = 10)
lab_user_last_name.pack(pady = 10)
ent_user_last_name.pack(pady = 10)
lab_user_email.pack(pady = 10)
ent_user_email.pack(pady = 10)
lab_user_feedback.pack(pady = 10)


rb_1.place(x = 85, y =385)
rb_2.place(x = 170, y =385)
rb_3.place(x = 255, y =385)
rb_4.place(x = 340, y =385)
rb_5.place(x = 425, y =385)

st_user_feedback.place(x = 80, y = 440)

btn_save.place(x = 200, y = 770)
btn_admin_login.place(x = 200, y = 830)

alw = Toplevel(root)
alw.title("Administrator Login")
alw.geometry("600x500+600+200")
alw.configure(bg = "grey16")

lab_alw_email = Label(alw, text = "Enter email address", font = f, bg = "grey16", fg = "grey98")
ent_alw_email = Entry(alw, font = f)
lab_alw_password = Label(alw, text = "Enter password", font = f, bg = "grey16", fg = "grey98")
ent_alw_password = Entry(alw, font = f, show = '*')

btn_alw_login = Button(alw, text = "Log- In", font = f, width = 14, bg = "aqua", command = login)
btn_alw_back = Button(alw, text = "Back", font = f, width = 14, bg = "aqua", command = close_alw)

lab_alw_email.pack(pady = 10)
ent_alw_email.pack(pady = 10)
lab_alw_password.pack(pady = 10)
ent_alw_password.pack(pady = 10)

btn_alw_login.pack(pady = 10)
btn_alw_back.pack(pady = 10)

alw.withdraw()

aw = Toplevel(root)
aw.title("Administrator Feedback Control")
aw.geometry("400x350+700+325")
aw.configure(bg = "grey16")

btn_aw_show = Button(aw, text = "Show Feedbacks", font = f, width = 16, bg = "aqua", command = show)
btn_aw_update = Button(aw, text = "Update Feedbacks", font = f, width = 16, bg = "aqua", command = open_uw)
btn_aw_delete = Button(aw, text = "Delete Feedbacks", font = f, width = 16, bg = "aqua", command = open_dw)
btn_aw_logout = Button(aw, text = "Admin Log - Out", font = f, width = 16, bg = "aqua", command = close_aw)

btn_aw_show.pack(pady = 10)
btn_aw_update.pack(pady = 10)
btn_aw_delete.pack(pady = 10)
btn_aw_logout.pack(pady = 10)

aw.withdraw()

sw = Toplevel(aw)
sw.title("Show Feedbacks")
sw.geometry("1300x450+250+300")
sw.configure(bg = "grey16")

st_sw_feedback = ScrolledText(sw, font = f1, width = 120, height = 15)
btn_sw_back = Button(sw, text = "Back", font = f, width = 10, bg = "aqua", command = close_sw)

st_sw_feedback.pack(pady = 10)
btn_sw_back.pack(pady = 10)

sw.withdraw()

uw = Toplevel(aw)
uw.title("Update Feedbacks")
uw.geometry("600x960+600+30")
uw.configure(bg = "grey16")

lab_uw_id = Label(uw, text = "Enter the ID to be updated", font = f, bg = "grey16", fg = "grey98")
ent_uw_id = Entry(uw, font = f)

lab_uw_id.pack(pady = 10)
ent_uw_id.pack(pady = 10)

lab_uw_first_name = Label(uw, text = "Enter updated first name", font = f, bg = "grey16", fg = "grey98")
ent_uw_first_name = Entry(uw, font = f)
lab_uw_last_name = Label(uw, text = "Enter updated last name", font = f, bg = "grey16", fg = "grey98")
ent_uw_last_name = Entry(uw, font = f)
lab_uw_email = Label(uw, text = "Enter updated email address", font = f, bg = "grey16", fg = "grey98")
ent_uw_email = Entry(uw, font = f)

lab_uw_feedback = Label(uw, text = "Enter updated Feedback", font = f, bg = "grey16", fg = "grey98")

r = IntVar()
r.set(5)
rb_uw_1 = Radiobutton(uw, text = "1★", font = f, bg = "grey16", fg = "grey98", variable = r, value = 1)
rb_uw_2 = Radiobutton(uw, text = "2★", font = f, bg = "grey16", fg = "grey98", variable = r, value = 2)
rb_uw_3 = Radiobutton(uw, text = "3★", font = f, bg = "grey16", fg = "grey98", variable = r, value = 3)
rb_uw_4 = Radiobutton(uw, text = "4★", font = f, bg = "grey16", fg = "grey98", variable = r, value = 4)
rb_uw_5 = Radiobutton(uw, text = "5★", font = f, bg = "grey16", fg = "grey98", variable = r, value = 5)

st_uw_feedback = ScrolledText(uw, font = f, width = 35, height = 7)

lab_uw_first_name.pack(pady = 10)
ent_uw_first_name.pack(pady = 10)
lab_uw_last_name.pack(pady = 10)
ent_uw_last_name.pack(pady = 10)
lab_uw_email.pack(pady = 10)
ent_uw_email.pack(pady = 10)
lab_uw_feedback.pack(pady = 10)


rb_uw_1.place(x = 85, y = 515)
rb_uw_2.place(x = 170, y = 515)
rb_uw_3.place(x = 255, y = 515)
rb_uw_4.place(x = 340, y = 515)
rb_uw_5.place(x = 425, y = 515)

st_uw_feedback.place(x = 80, y = 570)

btn_uw_update = Button(uw, text = "Update", font = f,  width = 14, bg = "aqua", command = update)
btn_uw_back = Button(uw, text = "Back", font = f, width = 14, bg = "aqua", command = close_uw)

btn_uw_update.place(x = 200, y = 810)
btn_uw_back.place(x = 200, y = 880)

uw.withdraw()

dw = Toplevel(aw)
dw.title("Delete Feedbacks")
dw.geometry("400x300+700+325")
dw.configure(bg = "grey16")

lab_dw_id = Label(dw, text = "Enter the ID to be deleted", font = f, bg = "grey16", fg = "grey98")
ent_dw_id = Entry(dw, font = f)
btn_dw_delete = Button(dw, text = "Delete", font = f,  width = 14, bg = "aqua", command = delete)
btn_dw_back = Button(dw, text = "Back", font = f, width = 14, bg = "aqua", command = close_dw)

lab_dw_id.pack(pady = 10)
ent_dw_id.pack(pady = 10)
btn_dw_delete.pack(pady = 10)
btn_dw_back.pack(pady = 10)

dw.withdraw()

def on_closing_root():
	if askokcancel("Quit", "Do you want to quit?"):
		root.destroy()
root.protocol("WM_DELETE_WINDOW", on_closing_root)

def on_closing_alw():
	if askokcancel("Back", "Do you want to go back to main window?"):
		alw.withdraw()
alw.protocol("WM_DELETE_WINDOW", on_closing_alw)

def on_closing_aw():
	if askokcancel("Back", "Do you want to go back to main window?"):
		aw.withdraw()
		root.destroy()
aw.protocol("WM_DELETE_WINDOW", on_closing_aw)

def on_closing_sw():
	if askokcancel("Back", "Do you want to go back to Administrator Control window?"):
		sw.withdraw()
sw.protocol("WM_DELETE_WINDOW", on_closing_sw)

def on_closing_dw():
	if askokcancel("Back", "Do you want to go back to Administrator Control window?"):
		dw.withdraw()
dw.protocol("WM_DELETE_WINDOW", on_closing_dw)

def on_closing_uw():
	if askokcancel("Back", "Do you want to go back to Administrator Control window?"):
		uw.withdraw()
uw.protocol("WM_DELETE_WINDOW", on_closing_uw)


root.mainloop()