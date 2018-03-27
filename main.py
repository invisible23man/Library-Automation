### Login Menu
import os
import sys
from bk_cls import *
from usr_cls import *
from usr_authorize import stud_login
from bk_srch_menu import srch_bk
from data_commits import tk_commit,ret_commit

os.system('clear')

###use decor/wrapper
print ("======================================== ")
print ("= AUTONOMOUS LIBRARY MANAGEMENT SYSTEM = ")
print ("======================================== ")
print ("			              	 ")
print ("			              	 ")
print ("			              	 ")

task=raw_input("What do you want to do : ")

if "take" in task.lower():
	print ("			              	")
	print ("We'll help you take book!!!		")
	print ("........................................")
	print ("But first, authenticate yourself please!")
	print ("........................................")
	print ("			              	")


	barID=input("Enter Student ID : ") # barcode id
	login=stud_login(barID)
	os.system('clear')
		
	if login:
		print("User Authenticated!")

		if login.BId1 and login.BId2:
			print "Please return a book before continuing!"
			sys.exit()	

		obj=srch_bk("take")
		
		if obj:
			tk_commit(login,obj)

	else:		
		print("Login Failed	 !")



###rest of the code		

elif "return" in task.lower():
	print ("			              	")
	print ("We'll help you return the book!!!	")
	print ("........................................")
	print ("But first, authenticate yourself please!")
	print ("........................................")
	print ("			              	")


	barID=input("Enter Student ID : ") # barcode id
	login=stud_login(barID)
	os.system('clear')
		
	if login:
		print("User Authenticated!")

		if not(login.BId1 or login.BId2):
			print "You have not taken any book!"
			sys.exit()	

		obj=srch_bk("return")

		if obj:
			ret_commit(login,obj)

	else:		
		print("Login Failed	 !")


else:
	
	print ("Sorry, didn't catch you!")
        # call method	




