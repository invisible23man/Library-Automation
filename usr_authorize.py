import datetime
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from usr_cls import *

engine = create_engine('sqlite:///Tables.db', echo=True)

# create a Session
Session = sessionmaker(bind=engine)
usr_log = Session()

def stud_login(barID):
	# Create objects  
	for user in usr_log.query(Student).order_by(Student.SId):
    		if (barID==user.SId):
			return user
	return 0
