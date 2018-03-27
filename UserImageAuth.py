from PIL import Image
from sqlalchemy.orm import sessionmaker
from usr_cls import *

def check():
	engine = create_engine('sqlite:///Tables.db', echo=True)
	# create a Session
	Session = sessionmaker(bind=engine)
	ses=Session()

	for stud in ses.query(Student).order_by(Student.SId):
		print "6"
		img = Image.open(stud.UserImage)
		img.show()

check()
		

