def decorStud(func):
	def wrap(Student):
		print("===============================================")
		print(" SId	    Name	Class	BId1	BId2  ")
		func()
		print("===============================================")
		
	return wrap

def decorBook(func):
	def wrap(Book):
		print("=========================================================================================")
		print(" BId	  Book Name	Author     Subject	Location Availability SId   DOI   DOR   ")
		func()
		print("=========================================================================================")
		
	return wrap


'''
def print_text():
	print("Hello world 123456")

decorated=decor(print_text)
decorated()



@decorStud
def pr():
	print("Hello world 123")

pr()
'''

