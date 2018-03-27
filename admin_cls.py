from datetime import date
import time
from sqlalchemy import *
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from sqlalchemy.orm import sessionmaker

 
engine = create_engine('sqlite:///Tables.db', echo=True)
Base = declarative_base()
 
########################################################################
class Admin(Base):
	""""""
	__tablename__ = "admin"
 
	AId   = Column(Integer, primary_key=True)
	AName = Column(String)
	APass = Column(String)
	#----------------------------------------------------------------------
    			
	def createAdmin(self):
        	""""""
		# create a Session
		Session = sessionmaker(bind=engine)
		crtAdmin = Session()
		
		self.AId     = raw_input("Enter Admin Id     : ")  	
		self.AName   = raw_input("Enter Admin Name   : ")
		self.APass   = raw_input("Enter Author Pass  : ")

		crtAdmin.add(self)

		# commit the record the database
		crtAdmin.commit()

	### @decorStud	
	def getAdmin(self):
        	""""""
		print(" "+ str(self.AId) +" "+ self.AName +" ")
		
      	
# create tables
Base.metadata.create_all(engine)


