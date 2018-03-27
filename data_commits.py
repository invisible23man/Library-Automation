### module to make commits into database while taking and returning book
from usr_cls import *
from update import *

def tk_commit(login,obj):
	##login.take(obj)
	if obj.BAvail==0:
		print "Book is not available!"
	else :
		update_take(obj,login)

###	obj.take()
###	obj.getBook()
###	login.getStud()



def ret_commit(login,obj):
	update_ret(obj,login)
