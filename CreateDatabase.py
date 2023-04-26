import sqlite3

connCourse = sqlite3.connect('Course.csv')
connDept = sqlite3.connect('Department.csv')
connMajors = sqlite3.connect('Majors.csv')
connProf = sqlite3.connect('Professor.csv')
connRegistered = sqlite3.connect('Registered.csv')
connSection = sqlite3.connect('Section.csv')
connStudents = sqlite3.connect('Students.csv')

c1 = connCourse.cursor()
c2 = connDept.cursor()
c3 = connMajors.cursor()
c4 = connProf.cursor()
c5 = connRegistered.cursor()
c6 = connSection.cursor()
c7 = connStudents.cursor()

#create tables
