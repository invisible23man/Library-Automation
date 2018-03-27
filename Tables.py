import sqlite3 as lite
import sys

con=lite.connect('Tables.db')

with con:

	cur = con.cursor()
	cur.execute("CREATE TABLE IF NOT EXISTS Students(SId INT, Name TEXT, Class TEXT, BId1 INT, BId2 INT, PRIMARY KEY (SId))")

	'''	
	cur.execute("INSERT INTO Users VALUES(1, 'Melvin')")
	cur.execute("INSERT INTO Users VALUES(2,'Sonya')")
    	cur.execute("INSERT INTO Users VALUES(3,'Greg')")
	'''
	cur.execute("CREATE TABLE IF NOT EXISTS Books(BId INT, Bname TEXT, Aname TEXT, Subject TEXT, Loc TEXT, BAvail INT, SId INT, DOI DATE, DOR DATE, PRIMARY KEY (BId))")
    	
	'''
	cur.execute("INSERT INTO Books VALUES(1,1,'Wadhwa')")
    	cur.execute("INSERT INTO Books VALUES(2,2,'Shawney')")
    	cur.execute("INSERT INTO Books VALUES(3,3,'Bimbra')")
	'''
