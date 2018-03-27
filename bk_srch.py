from bk_cls import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

engine = create_engine('sqlite:///Tables.db', echo=False)

# create a Session
Session = sessionmaker(bind=engine)
bksrch = Session()

def srchBId():
	os.system('clear')	
	bid=input("Enter Book Id : ")
	# Create objects  
	for bk in bksrch.query(Book).order_by(Book.BId):
		if(bid==bk.BId):
			return bk	
	return 1

def srchBname():
	os.system('clear')	
	bname=raw_input("Enter Book Name : ")
	# Create objects  
	for bk in bksrch.query(Book).order_by(Book.Bname):
		if(bname.lower()==bk.Bname.lower()):
			return bk	
	return 1

### Note:
### Search by Bname currently applicable only for full Bname
### Make search available for part of Bname and show multiple records

def srchAname():
	os.system('clear')	
	aname=raw_input("Enter Author Name : ")
	flag=1
	# Create objects  
	for bk in bksrch.query(Book).order_by(Book.Aname):
		if(aname.lower()==bk.Aname.lower()):
			bk.getBook()
			flag=0	
	return flag

def srchSub():
	os.system('clear')	
	sub=raw_input("Enter Subject : ")
	flag=1
	# Create objects  
	for bk in bksrch.query(Book).order_by(Book.Subject):
		if(sub.lower()==bk.Subject.lower()):
			bk.getBook()
			flag=0	
	return flag

def srchLoc():
	os.system('clear')	
	loc=raw_input("Enter Location : ")
	# Create objects  
	for bk in bksrch.query(Book).order_by(Book.Loc):
		if(loc==bk.Loc):
			return bk	
	return 1




### Define Search Modules for :
###
### 1.Books to be returned within date bound
### 2.Books taken by particular student (SId)
### 3.Books issued on or within particular date bound


