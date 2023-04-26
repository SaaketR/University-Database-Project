import sqlite3

conn = sqlite3.connect('create_tables.sql')
connCourse = sqlite3.connect('Course.csv')
connDept = sqlite3.connect('Department.csv')
connMajors = sqlite3.connect('Majors.csv')
connProf = sqlite3.connect('Professor.csv')
connRegistered = sqlite3.connect('Registered.csv')
connSection = sqlite3.connect('Section.csv')
connStudents = sqlite3.connect('Students.csv')

c = conn.cursor()
c1 = connCourse.cursor()
c2 = connDept.cursor()
c3 = connMajors.cursor()
c4 = connProf.cursor()
c5 = connRegistered.cursor()
c6 = connSection.cursor()
c7 = connStudents.cursor()

#create tables
c.execute( '''CREATE TABLE COURSE( COURSE_ID INTEGER NOT NULL; COURSE_NAME INTEGER NOT NULL; COURSE_DESC VARCHAR(500) NOT NULL; CREDITS INTEGER NOT NULL; );''')
