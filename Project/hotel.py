from tkinter import *

from tkinter import Button


import mysql.connector
from tkinter import Tk, StringVar, ttk

root=Tk()
root.title("MENU CARD")


root.iconbitmap('food.ico')




def f1():
	con=None
	cursor=None
	print("User Details")
	con=mysql.connector.connect(
		host="localhost",
		user="root",
		passwd="root",
                database="hotel")
	cursor = con.cursor()
	cursor.execute('use hotel')
	cursor.execute('Select * from guest')
	data=cursor.fetchall()
	print(data)


btnUser=Button(root,text="View User Details",font=('Alegrian', 20) , width= 25,height=2,command=f1)
btnUser.pack(pady=10)

def f2():
	con=None
	cursor=None
	print("Ordered Items")
	con=mysql.connector.connect(
		host="localhost",
		user="root",
		passwd="root",
                database="hotel")
	cursor = con.cursor()
	cursor.execute('use hotel')
	cursor.execute('Select * from Items')
	data=cursor.fetchall()
	print(data)
btnItems=Button(root,text="Items Ordered",font=('Alegrian', 20) , width= 25,height=2,command=f2)
btnItems.pack(pady=10)

def f3():
	con=None
	cursor=None
	print("Reset Done")
	con=mysql.connector.connect(
		host="localhost",
		user="root",
		passwd="root",
                database="hotel")
	cursor = con.cursor()
	cursor.execute('use hotel')
	cursor.execute('Drop table Items')
	cursor.execute('Drop table guest')
	
btnReset=Button(root,text="Reset",font=('Alegrian', 20) , width= 25,height=2,command=f3)
btnReset.pack(pady=10)

root.mainloop()
