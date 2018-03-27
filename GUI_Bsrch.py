from bk_cls import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, query
import os

def srchBname():
	os.system('clear')
	bname=raw_input("Enter Book Name : ")

	engine = create_engine('sqlite:///Tables.db', echo=False)

	# create a Session
	Session = sessionmaker(bind=engine)
	bksrch = Session()
	bk_list=[]

	# Create objects  
	for bk in bksrch.query(Book).order_by(Book.Bname):
		if(bname.lower() in bk.Bname.lower()):
			print bk.Bname
			bk_list.append(bk)		
				
	return bk_list


	'''
	srch = bksrch.query(Book).\
		order_by(Book.Bname)
		##.\filter(Book.Bname.like("%C")

	print srch
	'''


srchBname()
		

