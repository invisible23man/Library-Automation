from admin_cls import *

print "ADD ADMIN"

ch=1
while(ch):

	adm=Admin()
	adm.createAdmin()
	adm.getAdmin()
	ch=input("Enter '0' to exit!")
