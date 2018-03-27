import sqlite3 as lite
import datetime

def update_take(bk,stud):

	# create a database connection
    	conn = lite.connect('Tables.db')

	if stud.BId1==0:
		sql2 = " UPDATE Students SET BId1= '%d' WHERE SId = '%d'" % (bk.BId,stud.SId)
   	else:
		if stud.BId2==0:
			sql2 = " UPDATE Students SET BId2= '%d' WHERE SId = '%d'" % (bk.BId,stud.SId)
    		else:
			print "You have already taken two books!"
    			return
	
	today = datetime.date.today()
	dur = datetime.timedelta(days=14)
	ret_date= today+ dur
    	
	sql1 = " UPDATE Books SET BAvail=0, SId= '%d', DOI= '%s', DOR= '%s' WHERE BId = '%d'" % (stud.SId,str(today),str(ret_date),bk.BId)

	cur = conn.cursor()
    	cur.execute(sql1)
	cur.execute(sql2)

	conn.commit()
	print "Updated"

	
	cur.execute("SELECT * FROM Books")
	rows = cur.fetchall()
 
    	for row in rows:
        	print(row)

def update_ret(bk,stud):

	# create a database connection
    	conn = lite.connect('Tables.db')	
	
	if stud.BId1==bk.BId:
		sql2 = " UPDATE STudents SET BId1=0 WHERE SId = '%d'" % (stud.SId)
    	elif stud.BId2==bk.BId:
		sql2 = " UPDATE STudents SET BId2=0 WHERE SId = '%d'" % (stud.SId)
    	else:
		print "You don't have any books to return!"
	
	sql1 = " UPDATE Books SET BAvail=1, SId= null, DOI= null, DOR= null WHERE BId = '%d'" % (bk.BId)
    	cur = conn.cursor()
    	cur.execute(sql1)
	cur.execute(sql2)

	conn.commit()
	print "Updated"

	cur.execute("SELECT * FROM Books")
	rows = cur.fetchall()
 
    	for row in rows:
        	print(row)
