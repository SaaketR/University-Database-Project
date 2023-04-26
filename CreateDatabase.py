import sqlite3

conn = sqlite3.connect('CreateDatabase.db')

c = conn.cursor()

#create tables
c.execute( '''CREATE TABLE "Course" ( "Course_ID"	INTEGER, "Course_Name" TEXT, "CourseDesc"	TEXT,
	"Credits"	INTEGER,
	PRIMARY KEY("Course_ID" AUTOINCREMENT)
);
c.execute( '''CREATE TABLE BOOK( [ISBN] TEXT PRIMARY KEY, [author] text, [year] integer, [title] text, [price] integer)''')
