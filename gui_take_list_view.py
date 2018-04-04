from bk_cls import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

def get_list():

  list_view[]=Book()

  engine = create_engine('sqlite:///Tables.db', echo=False)

  # create a Session
  Session = sessionmaker(bind=engine)
  bksrch = Session()

  # Create objects  
  for bk in bksrch.query(Book).order_by(Book.BId):
	  	if(bk.BAvail==1):
		    list_view.append(bk)	
	
  return list_view




