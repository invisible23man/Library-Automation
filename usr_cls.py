from PIL import Image
from sqlalchemy import *
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from sqlalchemy.orm import sessionmaker
from decor import decorStud
from bk_cls import *


 
engine = create_engine('sqlite:///Tables.db', echo=True)
Base = declarative_base()
 
########################################################################
class Student(Base):
	""""""
	__tablename__ = "Students"
 
	SId   = Column(Integer, primary_key=True)
	Name = Column(String)
	Class= Column(String)
#	BId1 = Column(Integer, ForeignKey('books.BId'))	
#	BId2 = Column(Integer, ForeignKey('books.BId'))	
#	stu = relationship("Book", back_populates="stu")
     	BId1 = Column(Integer)
	BId2 = Column(Integer)
	UserImage = Column(String)
	
	#----------------------------------------------------------------------
    	
	def __init__(self):
        	""""""
		self.BId1= 0
		self.BId2= 0
	     	
	def createStud(self):
        	""""""
		# create a Session
		Session = sessionmaker(bind=engine)
		crtStudsess = Session()
		
		self.SId   = raw_input("Enter SId   : ")  	
		self.Name  = raw_input("Enter Name  : ")
		self.Class = raw_input("Enter Class : ")

		crtStudsess.add(self)

		# commit the record the database
		crtStudsess.commit()

	'''
	def usr_image_auth(self):

		# create a Session
		Session = sessionmaker(bind=engine)
		imag_sess = Session()
		
		img=self.UserImage  	
		
		# commit the record the database
		crtStudsess.commit()
	'''	
        

	### @decorStud	
	def getStud(self):
        	""""""
		print(" "+ str(self.SId) +" "+ self.Name +" "+ self.Class +" "+ str(self.BId1) +" "+ str(self.BId2))
	
	def updateStud(self):
        	""""""
		'''
		metadata = MetaData()
		Students = Table('Students', metadata,
   		Column('SId', Integer, primary_key=True),
   		Column('Name', String(50)),
   		Column('Class', String(50)),
   		)
		
		.update().values(SId=raw_input("Enter New SId  : "),
 					Name=raw_input("Enter New Name  : "),
					Class=raw_input("Enter New Class  : ")
			

		'''		
		'''
		# create a Session
		Session = sessionmaker(bind=engine)
		updatesess = Session()
		
		self.SId   = raw_input("Enter New SId   : ")  	
		self.Name  = raw_input("Enter New Name  : ")
		self.Class = raw_input("Enter New Class : ")

		self.getStud()
		###updatesess.update(self)
		print updatesess.dirty

		# commit the record the database
		updatesess.commit()
		
		self.getStud()
		'''

	def take(self,bk):
        	""""""
		# create a Session
		Session = sessionmaker(bind=engine)
		take_book = Session()
		
		self.BId1   = bk.BId  

		print take_book.dirty

		# commit the record the database
		take_book.commit()
		
		
#		take_book.update(self)

		# commit the record the database
		take_book.commit()
        

	
# create tables
Base.metadata.create_all(engine)
