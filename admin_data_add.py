### Adminstrator acessed file (to be made as such)

import os
from bk_cls import *
from usr_cls import *
from usr_srch_menu import srch_usr

os.system('clear')

###use decor/wrapper
print (" ADMIN OPTIONS 	")
print (" =============	")
print ("1.ADD BOOK 	")
print ("2.ADD STUDENT 	")
print ("3.UPDATE STUDENT")
print ("	 	")

### add methods for updating book,student and deleting the same

ch=input("Enter Choice : ")

if ch==1:
	bk=Book()
	bk.createBook()
elif ch==2:
	stud=Student()
	stud.createStud()
elif ch==3:
	stud=srch_usr("update")
	stud.updateStud()

else :
	print("Invalid Choice!")
	
