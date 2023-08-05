from tkinter import *
from tkinter.messagebox import *
from tkinter.scrolledtext import *
from sqlite3 import *
from requests import *
import matplotlib.pyplot as plt
from datetime import *

def open_aw():
	aw.deiconify()
	mw.withdraw()
def close_aw():
	mw.deiconify()
	aw.withdraw()
def open_vw():
	vw.deiconify()
	mw.withdraw()
	con = None
	try:
		con = connect("emp24june23.db")
		cursor = con.cursor()
		sql = "select * from emp"
		cursor.execute(sql)
		emp_data = cursor.fetchall()
		info = ""
		for d in emp_data:
			info += "ID: " + str(d[0]) + " | " + "Name: " + str(d[1]) + " | " + "Salary: " + str(d[2]) + "\n"
		st_vw_info.insert(INSERT, info)
	except Exception as e:
		con.rollback()
		showerror("SQL View Error", e)
	finally:
		if con is not None:
			con.close()
def close_vw():
	mw.deiconify()
	vw.withdraw()
	st_vw_info.delete(1.0, END)
def open_uw():
	uw.deiconify()
	mw.withdraw()
def close_uw():
	mw.deiconify()
	uw.withdraw()
def open_dw():
	dw.deiconify()
	mw.withdraw()
def close_dw():
	mw.deiconify()
	dw.withdraw()
def save_add():
	con = None
	try:
		con = connect("emp24june23.db")
		cursor = con.cursor()
		sql = "insert into emp values('%d', '%s', '%f')"
		test_id = ent_aw_id.get()
		test_id = test_id.strip()
		if (test_id == ""):
			raise Exception("Blank ID is not allowed.")
		try:
			id = int(test_id)
		except ValueError:
			raise Exception("Enter numbers only.")
		if (id < 1):
			raise Exception("Minimum value allowed is 1.")
		name = ent_aw_name.get()
		name = name.strip()
		if (name == "") or (not name.isalpha()):
			raise Exception("Blank names or numbers are not allowed in name.")
		test_salary = ent_aw_salary.get()
		test_salary = test_salary.strip()
		if (test_salary == ""):
			raise Exception("Blank input is not allowed in salary.")
		try:
			salary = float(test_salary)
		except ValueError:
			raise Exception("Enter numbers only in salary.")
		if (salary < 1):
			raise Exception("Minimum value limit is 1.")
		
		cursor.execute(sql % (id, name, salary))
		con.commit()
		showinfo("Success", "Record Saved")
	except Exception as e:
		con.rollback()
		showerror("SQL error", e)
	finally:
		if con is not None:
			con.close()
		ent_aw_id.delete(0, END)
		ent_aw_name.delete(0, END)
		ent_aw_salary.delete(0, END)
		ent_aw_id.focus()
def save_update():
	con = None
	try:
		con = connect("emp24june23.db")
		cursor = con.cursor()
		sql = "update emp set name = '%s', salary = '%f' where id = '%d'"
		test_uid = ent_uw_id.get()
		test_uid = test_uid.strip()
		if (test_uid == ""):
			raise Exception("Blank ID is not allowed.")
		try:
			id = int(test_uid)
		except ValueError:
			raise Exception("Enter numbers only.")
		if (id < 1):
			raise Exception("Minimum value allowed is 1.")
		name = ent_uw_name.get()
		name = name.strip()
		if (name == "") or (not name.isalpha()):
			raise Exception("Blank names or numbers are not allowed in name.")
		test_usalary = ent_uw_salary.get()
		test_usalary = test_usalary.strip()
		if (test_usalary == ""):
			raise Exception("Blank input is not allowed in salary.")
		try:
			salary = float(test_usalary)
		except ValueError:
			raise Exception("Enter numbers only.")
		if (salary < 1):
			raise Exception("Minimum value limit is 1.")
		
		cursor.execute(sql % (name, salary, id))
		if cursor.rowcount == 1:
			con.commit()
			showinfo("Success", "Record Updated.\nCheck View Option to see the change.")
		else:
			showerror("Record Error", "Record does not exist.\nEnter an ID which already exists in order to be updated.")
	except Exception as e:
		con.rollback()
		showerror("SQL error", e)
	finally:
		if con is not None:
			con.close()
		ent_uw_id.delete(0, END)
		ent_uw_name.delete(0, END)
		ent_uw_salary.delete(0, END)
		ent_uw_id.focus()
def delete():
	con = None
	try:
		con = connect("emp24june23.db")
		cursor = con.cursor()
		sql = "delete from emp where id = '%d'"
		test_did = ent_dw_id.get()
		test_did = test_did.strip()
		if (test_did == ""):
			raise Exception("Blank ID is not allowed.")
		try:
			id = int(test_did)
		except ValueError:
			raise Exception("Enter numbers only.")
		if (id < 1):
			raise Exception("Minimum value allowed is 1.")
		cursor.execute(sql % (id))
		if cursor.rowcount == 1:
			con.commit()
			showinfo("Success", "Record Deleted.\nCheck View Option to see the change.")
		else:
			showerror("Record Error", "Record does not exist.\nEnter an ID which already exists in order to be deleted.")
	except Exception as e:
		con.rollback()
		showerror("SQL Delete Error", e)
	finally:
		if con is not None:
			con.close()
		ent_dw_id.delete(0, END)
		ent_dw_id.focus()

def get_chart():
	con = None
	try:
		con = connect("emp24june23.db")
		cursor = con.cursor()
		sql = "select * from emp"
		cursor.execute(sql)
		emp_data = cursor.fetchall()   #fetching emp_data
		
		name_list = []
		salary_list = []
		for n in emp_data:
			name_list.append(n[1])    #creating lists from data
			salary_list.append(n[2])

		res = {}
		for i in range(len(name_list)):
			res[name_list[i]] = salary_list[i]  #creating dictionary from both lists

		value_key_pairs = ((value, key) for (key,value) in res.items())  #forming v:k pairs
		sorted_value_key_pairs = sorted(value_key_pairs, reverse = True)  #descending order
		sorted_dict = {k:v for v,k in sorted_value_key_pairs}	#rearranging as key:value		
		xname = []
		ysalary = []
		for key,val in sorted_dict.items():
			xname.append(str(key))  #creating x-axis list
			ysalary.append(float(val))  #creating y-axis list

		xname_sliced = xname[:5]   #slicing for first 5 names
		ysalary_sliced = ysalary[:5]   #slicing for first 5 salaries
		
		#creating bar chart from the above lists
		plt.bar(xname_sliced, ysalary_sliced, color = ["red", "green", "blue", "yellow", 	"pink"], width = 0.3)
		plt.xlabel("Names")
		plt.ylabel("Salary")
		plt.title("Top 5 Highest Paid Employees")
		plt.show()
		if askokcancel("Save", "Do you want to save this chart as .png and .pdf?"):
			plt.bar(xname_sliced, ysalary_sliced, color = ["red", "green", "blue", "yellow", 	"pink"], width = 0.3)
			plt.xlabel("Names")
			plt.ylabel("Salary")
			plt.title("Top 5 Highest Paid Employees")
			plt.savefig("emp_stats.png")
			plt.savefig("emp_stats.pdf")
			showinfo("Saved", "Saved as emp_data.png and emp_data.pdf")
		plt.close()
	except Exception as e:
		con.rollback()
		showerror("SQL View Error", e)
	finally:
		if con is not None:
			con.close()

#main window set-up
mw = Tk()
mw.title("Employee Management System Application")
mw.geometry("550x650+750+200")
mw.configure(bg = "medium purple")
f = ("Hina-Mincho", 25)
f2 = ("Hina-Mincho", 30)

#buttons on main window
btn_mw_add = Button(mw, text = "Add", font = f, bg = "lavender", width = 10, command = open_aw)
btn_mw_view = Button(mw, text = "View", font = f, bg = "lavender", width = 10, command = open_vw)
btn_mw_update = Button(mw, text = "Update", font = f, bg = "lavender", width = 10, command = open_uw)
btn_mw_delete = Button(mw, text = "Delete", font = f, bg = "lavender", width = 10, command = open_dw)
btn_mw_charts = Button(mw, text = "Charts", font = f, bg = "lavender", width = 10, command = get_chart)

btn_mw_add.pack(pady = 20)
btn_mw_view.pack(pady = 20)
btn_mw_update.pack(pady = 20)
btn_mw_delete.pack(pady = 20)
btn_mw_charts.pack(pady = 20)

#borders
lab_mw_border = Label(mw, text = "                                              ", borderwidth = 1, relief = "solid", font = f2)

#location and temp label in main window
lab_mw_loc = Label(mw, text = "Location:", font = f, fg = "red")
lab_mw_loc_ans = Label(mw, text = "Location1", font = f, fg = "blue violet")
lab_mw_temp = Label(mw, text = "Temperature:", font = f, fg = "red")
lab_mw_temp_ans = Label(mw, text = "", font = f, fg = "blue violet")


#getting location
try:
	wa = "https://ipinfo.io/"
	res = get(wa)
	data = res.json()
	city_name = data["city"]
	lab_mw_loc_ans.configure(text = str(city_name))
except Exception as e:
	showerror("Location Fetch Issue: ", e)

#getting temp
try:
	
	a1 = "https://api.openweathermap.org/data/2.5/"
	a2 = "weather?q=" + str(city_name)
	a3 = "&appid=e3a43739dd0a1fbdfe835c58b6b1397b"
	a4 = "&units=metric"
	wa = a1 + a2 + a3 + a4

	res = get(wa)
	data = res.json()
	temp = data["main"]["temp"]
	temp = str(temp) + "C"
	lab_mw_temp_ans.configure(text = str(temp))
except Exception as e:
	showerror("Temp Fetch Issue: ", e)

#border placement
lab_mw_border.place(x = 0, y = 549)

lab_mw_loc.place(x = 20, y = 550)
lab_mw_loc_ans.place(x = 140, y = 550)
lab_mw_temp.place(x = 270, y = 550)
lab_mw_temp_ans.place(x = 440, y = 550)

#add window set-up
aw = Toplevel(mw)
aw.title("Add Employee Info")
aw.geometry("550x650+750+200")
aw.configure(bg = "coral")

lab_aw_id = Label(aw, text = "Enter Employee ID", font = f, bg = "coral")
ent_aw_id = Entry(aw, font = f)
lab_aw_name = Label(aw, text = "Enter Employee Name", font = f, bg = "coral")
ent_aw_name = Entry(aw, font = f)
lab_aw_salary = Label(aw, text = "Enter Employee's Salary", font = f, bg = "coral")
ent_aw_salary = Entry(aw, font = f)
btn_aw_save = Button(aw, text = "Save", font = f, width = 5, bg = "bisque", command = save_add)
btn_aw_back = Button(aw, text = "Back", font = f, width = 5, bg = "bisque", command = close_aw)

lab_aw_id.pack(pady = 10)
ent_aw_id.pack(pady = 10)
lab_aw_name.pack(pady = 10)
ent_aw_name.pack(pady = 10)
lab_aw_salary.pack(pady = 10)
ent_aw_salary.pack(pady = 10)
btn_aw_save.pack(pady = 20)
btn_aw_back.pack(pady = 10)

aw.withdraw()

#view window set-up
vw = Toplevel(mw)
vw.title("View Employee Info")
vw.geometry("550x650+750+200")
vw.configure(bg = "spring green")
f1 = ("Hina-Mincho", 18)
lab_vw_info = Label(vw, text = "Employee Info", font = f, bg = "spring green")
st_vw_info = ScrolledText(vw, font = f1, width = 40, height = 17, bg = "pale green")
btn_vw_back = Button(vw, text = "Back", font = f, command = close_vw, bg = "pale green")

lab_vw_info.pack(pady = 10)
st_vw_info.pack(pady = 10)
btn_vw_back.pack(pady = 10)

vw.withdraw()

#update window setup
uw = Toplevel(mw)
uw.title("Update Employee Info")
uw.geometry("550x650+750+200")
uw.configure(bg = "dodger blue")

lab_uw_id = Label(uw, text = "Enter Employee ID to be updated", font = f, bg = "dodger blue")
ent_uw_id = Entry(uw, font = f)
lab_uw_name = Label(uw, text = "Enter Updated Employee Name", font = f, bg = "dodger blue")
ent_uw_name = Entry(uw, font = f)
lab_uw_salary = Label(uw, text = "Enter Updated Employee's Salary", font = f, bg = "dodger blue")
ent_uw_salary = Entry(uw, font = f)
btn_uw_save = Button(uw, text = "Save", font = f, width = 5, bg = "lightblue1", command = save_update)
btn_uw_back = Button(uw, text = "Back", font = f, width = 5, bg = "lightblue1", command = close_uw)

lab_uw_id.pack(pady = 10)
ent_uw_id.pack(pady = 10)
lab_uw_name.pack(pady = 10)
ent_uw_name.pack(pady = 10)
lab_uw_salary.pack(pady = 10)
ent_uw_salary.pack(pady = 10)
btn_uw_save.pack(pady = 20)
btn_uw_back.pack(pady = 10)

uw.withdraw()

#delete window setup
dw = Toplevel(mw)
dw.title("Update Employee Info")
dw.geometry("550x650+750+200")
dw.configure(bg = "salmon")

lab_dw_id = Label(dw, text = "Enter Employee ID to be deleted", font = f, bg = "salmon")
ent_dw_id = Entry(dw, font = f)
btn_dw_delete = Button(dw, text = "Delete", font = f, width = 5, bg = "misty rose", command = delete)
btn_dw_back = Button(dw, text = "Back", font = f, width = 5, bg = "misty rose", command = close_dw)

lab_dw_id.pack(pady = 10)
ent_dw_id.pack(pady = 10)
btn_dw_delete.pack(pady = 20)
btn_dw_back.pack(pady = 10)

dw.withdraw()

#in case of closing sub windows without going back to main
def on_closing():
	if askokcancel("Exit", "Do you want to exit?"):
		mw.destroy()
dw.protocol("WM_DELETE_WINDOW", on_closing)
uw.protocol("WM_DELETE_WINDOW", on_closing)
vw.protocol("WM_DELETE_WINDOW", on_closing)
aw.protocol("WM_DELETE_WINDOW", on_closing)
mw.protocol("WM_DELETE_WINDOW", on_closing)

mw.mainloop()