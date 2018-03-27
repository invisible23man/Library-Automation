from datetime import date
import time
from sqlalchemy import *
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from sqlalchemy.orm import sessionmaker
from decor import decorBook
from usr_cls import *

 
engine = create_engine('sqlite:///Tables.db', echo=True)
Base = declarative_base()
 
########################################################################
class Book(Base):
	""""""
	__tablename__ = "books"
 
	BId   = Column(Integer, primary_key=True)
	Bname = Column(String)
	Aname= Column(String)
	Subject= Column(String)
	Loc= Column(String)
	BAvail = Column(Integer)
#	SId = Column(Integer, ForeignKey('Students.SId'))	     	
#	stu = relationship("Student", back_populates="boo")	

	SId = Column(Integer)	
	DOI = Column(Date)  
	DOR = Column(Date)  

	#----------------------------------------------------------------------
    	
	def __init__(self):
        	""""""
		self.BId= 0
		self.SId= 0
		BAvail = 1
		self.DOI= date.today()
		self.DOR= date.today()

	
	def createBook(self):
        	""""""
		# create a Session
		Session = sessionmaker(bind=engine)
		crtBooksess = Session()
		
		self.BId     = raw_input("Enter Book Id     : ")  	
		self.Bname   = raw_input("Enter Book Name   : ")
		self.Aname   = raw_input("Enter Author Name : ")
		self.Subject = raw_input("Enter Subject     : ")
		self.Loc     = raw_input("Enter Location    : ")

		crtBooksess.add(self)

		# commit the record the database
		crtBooksess.commit()

	### @decorStud	
	def getBook(self):
        	""""""
		print(" "+ str(self.BId) +" "+ self.Bname +" "+ self.Aname +" "+ self.Subject+" "+ self.Loc+" "+ str(self.BAvail) +" "+ str(self.SId)+" "+ str(self.DOI)+" "+ str(self.DOR))
	
	def takeBook(self,stud):
		print "taKE"	
		
      	
# create tables
Base.metadata.create_all(engine)
