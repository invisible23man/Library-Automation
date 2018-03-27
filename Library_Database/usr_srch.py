from usr_cls import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

engine = create_engine('sqlite:///Tables.db', echo=True)

# create a Session
Session = sessionmaker(bind=engine)
srch = Session()

def srchId(mode="default"):
	if str(mode)=="default":
		os.system('clear')	
		sid=input("Enter SId : ")

	# Create objects  
	for stud in srch.query(Student).order_by(Student.SId):
		if(mode==stud.SId):
			return stud	
	return 1

def srchName():
	os.system('clear')	
	name=raw_input("Enter Name : ")
	# Create objects  
	for stud in srch.query(Student).order_by(Student.Name):
		if(name.lower()==stud.Name.lower()):
			return stud	
	return 1

### Note:
### Search by name currently applicable only for full name
### Make search available for part of name and show multiple records

def srchClass():
	os.system('clear')	
	cls=raw_input("Enter Class : ")
	flag=1
	# Create objects  
	for stud in srch.query(Student).order_by(Student.Class):
		if(cls.lower()==stud.Class.lower()):
			stud.getStud()
			flag=0	
	return flag

