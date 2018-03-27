import os
from bk_cls import *
from bk_srch import *

os.system('clear')

bk=0

def srch_bk(type_=None):

	###use decor/wrapper
	print (" SEARCH BOOK 		")
	print (" ====================== ")
	print ("1.Book    Id		")
	print ("2.Book 	  Name		")
	print ("3.Author  Name		")
	print ("4.Subject Name		")
	print ("5.Book    Location	")
	print ("			")

	ch=input("Enter Choice : ")

	if ch==1:
		bk=srchBId()
		if(bk==1):
			print("Book not found!")
		else:
			bk.getBook()
	elif ch==2:
		bk=srchBname()
		if(bk==1):
			print("Book not found!")
		else:
			bk.getBook()

	elif ch==3:
		flag=srchAname()
		if(flag==1):
			print("No Books or Unknown Author!")

	elif ch==4:
		flag=srchSub()
		if(flag==1):
			print("No Books or Unknown Subject!")

	elif ch==5:
		bk=srchLoc()
		if(bk==1):
			print("Book not found!")
		else:
			bk.getBook()
	else:
		print("Invalid Choice")

	###make code simpler

	###return book in case of take/return prompt from user	
	if type_=="take" or type_=="return":
		return bk
	else:
		return 0

	
