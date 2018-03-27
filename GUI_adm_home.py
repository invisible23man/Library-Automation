from Tkinter import *
from admin_check import *
import tkFont
import os
win = Tk()

myFont = tkFont.Font(family = 'Helvetica', size = 36, weight = 'bold')

def admin_log():
        a=t1.get()
        b=t2.get()
        y=admin_check(a,b)
        if y==0:
            print("failed")
            os.system("GUI_adm_home.py")

	else:
	    return 1
        

l1=Label(win,text='ADMIN :')
l2=Label(win,text='Password :')
t1=Entry(win,textvariable=StringVar())
t2=Entry(win,show='*',textvariable=StringVar())
b1= Button(win,text='Log In',command=Admin)

win.title("Login Page")
win.geometry('900x600')
l1.pack(side = TOP)
t1.pack(side = TOP)
l2.pack(side = TOP)

t2.pack(side = TOP)
b1.pack(side = BOTTOM)
win.mainloop()
