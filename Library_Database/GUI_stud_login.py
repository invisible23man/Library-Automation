from Tkinter import *
from usr_srch import *
import tkFont
import os
win = Tk()

myFont = tkFont.Font(family = 'Helvetica', size = 36, weight = 'bold')

def user_log():
        uname=t1.get()
        upass=t2.get()
        y=srchName(uname,upass)
        if y==0:
            print("failed")
            os.system("GUI_stud_login.py")

	else:
	    print ("success")
	    return 1
        

l1=Label(win,text='User :')
l2=Label(win,text='Password :')
t1=Entry(win,textvariable=StringVar())
t2=Entry(win,show='*',textvariable=StringVar())
b1= Button(win,text='Log In',command=user_log)

win.title("Login Page")
win.geometry('900x600')
l1.pack(side = TOP)
t1.pack(side = TOP)
l2.pack(side = TOP)

t2.pack(side = TOP)
b1.pack(side = BOTTOM)
win.mainloop()

user_log()
