import os
from usr_cls import *
from usr_srch import *

def srch_usr(type_=None):

	os.system('clear')

	###use decor/wrapper
	print (" SEARCH STUDENT ")
	print (" ============== ")
	print ("1.SId		")
	print ("2.Name		")
	print ("3.Class		")
	print ("		")
	
	ch=input("Enter Choice : ")

	if ch==1:
		stud=srchId()
		if(stud==1):
			print("Student not found!")
		else:
			stud.getStud()
	elif ch==2:
		stud=srchName()
		if(stud==1):
			print("Student not found!")
		else:
			stud.getStud()

	elif ch==3:
		flag=srchClass()
		if(flag==1):
			print("No Students or Incorrect Class!")

	else:
		print("Invalid Choice")

	if type_=="update" :
		return stud
	else:
		return 0

###make code simpler
