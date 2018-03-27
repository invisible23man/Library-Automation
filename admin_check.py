from admin_cls import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

engine = create_engine('sqlite:///Tables.db', echo=True)

# create a Session
Session = sessionmaker(bind=engine)
ad_check = Session()

def admin_check(adm, pass_):
	os.system('clear')	
	
	# Create objects  
	for ad in ad_check.query(Admin).order_by(Admin.AId):
		if(adm==ad.AName):
			if(pass_==ad.APass):
				print "Admin Authenticated!"
				return 1
			else:
				print "Invalid Password!"
				return 0	
	print "Admin Not Found!"	
	return 0


