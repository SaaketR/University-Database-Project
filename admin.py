"""
All functions related to an admin:
    1. Addition to a table
    2. Removal from a table
    3. Modifying a table

"""

import sqlite3
import student
import new_student

conn = sqlite3.connect("Database.db")
cursor = conn.cursor()


# Presents the admin with a list of tables on the database, returns the table of choice
def admin_select_table(): 
    """
    Interface to present the admin the different tables in the database, accepts choice as a number:
        0. GO BACK
        1. Professor
        2. Section
        3. Registered
        4. Course
        5. Department
        6. Students
        7. Majors
        8. Admin
    """
    while (True):
        try:
            choice = int(input("Enter choice here: "))
            if ((choice >= 0) and (choice <= 8)):
                break
        except:
            print("Invalid choice, try again.")
    return choice


# Printing table data based on table selection
def admin_show_table(table_choice):
    try:    
        match table_choice:
            case 1:     # 1. Professor
                print("{:<20} {:<20} {:<20} {:<20} {:<20} {:<20}".format("PID", "Name", "Department_ID", "Salary", "Email", "Tenure"))
                cursor.execute("SELECT * FROM Professor")
                query = cursor.fetchall()
                i = 0
                while (i < len(query)):
                    print("{:<20} {:<20} {:<20} {:<20} {:<20} {:<20}".format(query[i][0], query[i][1], query[i][2], query[i][3], query[i][4], query[i][5]))
                    i += 1

            case 2:     # 2. Section
                print("{:<20} {:<20} {:<20} {:<20} {:<20}".format("Section_ID", "Course_ID", "Term", "Professor_ID", "Section_Number"))
                cursor.execute("SELECT * FROM Section")
                query = cursor.fetchall()
                i = 0
                while (i < len(query)):
                    print("{:<20} {:<20} {:<20} {:<20} {:<20}".format(query[i][0], query[i][1], query[i][2], query[i][3], query[i][4]))
                    i += 1

            case 3:     # 3. Registered
                print("{:<20} {:<20}".format("UID", "Section_ID"))
                cursor.execute("SELECT * FROM Registered")
                query = cursor.fetchall()
                i = 0
                while (i < len(query)):
                    print("{:<20} {:<20}".format(query[i][0], query[i][1]))
                    i += 1

            case 4:     # 4. Course
                print("{:<20} {:<20} {:<20} {:<20}".format("Course_ID", "Course_Name", "CourseDesc", "Credits"))
                cursor.execute("SELECT * FROM Course")
                query = cursor.fetchall()
                i = 0
                while (i < len(query)):
                    print("{:<20} {:<20} {:<20} {:<20}".format(query[i][0], query[i][1], query[i][2], query[i][3]))
                    i += 1

            case 5:     # 5. Department
                print("{:<20} {:<20} {:<20} {:<20} {:<20}".format("Department_ID", "Department_Name", "Year_Founded", "Budget", "Department_Chair"))
                cursor.execute("SELECT * FROM Department")
                query = cursor.fetchall()
                i = 0
                while (i < len(query)):
                    print("{:<20} {:<20} {:<20} {:<20} {:<20}".format(query[i][0], query[i][1], query[i][2], query[i][3], query[i][4]))
                    i += 1

            case 6:     # 6. Students
                print("{:<20} {:<20} {:<20} {:<20} {:<20} {:<20} {:<20} {:<20} {:<20} {:<20} {:<20}".format("UID", "First_Name", "Last_Name", "Date_of_Birth", "GPA", "Major_ID", "Email", "Undergraduate", "Class_Standing", "Phone", "Address"))
                cursor.execute("SELECT * FROM Students")
                query = cursor.fetchall()
                i = 0
                while (i < len(query)):
                    print("{:<20} {:<20} {:<20} {:<20} {:<20} {:<20} {:<20} {:<20} {:<20} {:<20} {:<20}".format(query[i][0], query[i][1], query[i][2], query[i][3], query[i][4], query[i][5], query[i][6], query[i][7], query[i][8], query[i][9], query[i][10], query[i][11]))
                    i += 1

            case 7:     # 7. Majors
                print("{:<20} {:<20} {:<20}".format("Major_ID", "Major_Name", "Department_ID"))
                cursor.execute("SELECT * FROM Majors")
                query = cursor.fetchall()
                i = 0
                while (i < len(query)):
                    print("{:<20} {:<20} {:<20}".format(query[i][0], query[i][1], query[i][2]))
                    i += 1

            case 8:     # 8. Admin
                print("{:<20} {:<20} {:<20}".format("Name", "Email", "Password"))
                cursor.execute("SELECT * FROM Admin")
                query = cursor.fetchall()
                i = 0
                while (i < len(query)):
                    print("{:<20} {:<20} {:<20}".format(query[i][0], query[i][1], query[i][2]))
                    i += 1
            
            case __:
                raise ValueError
    
    except ValueError:
        print("An unexpected error occured.")


# Modifying table data based on table selection
def admin_edit_table(table_choice, action):
    try:    
        match table_choice:
            case 1:     # 1. Professor
                if (action.lower()=='a'):
                    print("Please enter the following details: ")
                    new_PID = input("PID: ")
                    new_Name = input("Name: ")
                    new_Department_ID = input("Department_ID: ")
                    new_Salary = input("Salary: ")
                    new_Email = input("Email: ")
                    new_Tenure = input("Tenure: ")
                    cursor.execute("INSERT INTO Professor VALUES (?,?,?,?,?,?)", (new_PID, new_Name, new_Department_ID, new_Salary, new_Email, new_Tenure,))
                elif (action.lower()=='d'):
                    PID_toRemove = input("Enter PID to Remove: ")
                    cursor.execute("DELETE FROM Professor WHERE Professor.PID=?", (PID_toRemove,))

            case 2:     # 2. Section
                if (action.lower()=='a'):
                    print("Please enter the following details: ")
                    """
                    
                    <-- code to obtain new details goes here

                    """
                    cursor.execute("INSERT INTO Professor VALUES (?,?,?,?,?,?)", (new_PID, new_Name, new_Department_ID, new_Salary, new_Email, new_Tenure,))
                elif (action.lower()=='d'):
                    PID_toRemove = input("Enter PID to Remove: ")
                    cursor.execute("DELETE FROM Professor WHERE Professor.PID=?", (PID_toRemove,))

            case 3:     # 3. Registered
                if (action.lower()=='a'):
                    print("Please enter the following details: ")
                    """
                    
                    <-- code to obtain new details goes here

                    """
                    cursor.execute("INSERT INTO Professor VALUES (?,?,?,?,?,?)", (new_PID, new_Name, new_Department_ID, new_Salary, new_Email, new_Tenure,))
                elif (action.lower()=='d'):
                    PID_toRemove = input("Enter PID to Remove: ")
                    cursor.execute("DELETE FROM Professor WHERE Professor.PID=?", (PID_toRemove,))

            case 4:     # 4. Course
                if (action.lower()=='a'):
                    print("Please enter the following details: ")
                    """
                    
                    <-- code to obtain new details goes here

                    """
                    cursor.execute("INSERT INTO Professor VALUES (?,?,?,?,?,?)", (new_PID, new_Name, new_Department_ID, new_Salary, new_Email, new_Tenure,))
                elif (action.lower()=='d'):
                    PID_toRemove = input("Enter PID to Remove: ")
                    cursor.execute("DELETE FROM Professor WHERE Professor.PID=?", (PID_toRemove,))

            case 5:     # 5. Department
                if (action.lower()=='a'):
                    print("Please enter the following details: ")
                    """
                    
                    <-- code to obtain new details goes here

                    """
                    cursor.execute("INSERT INTO Professor VALUES (?,?,?,?,?,?)", (new_PID, new_Name, new_Department_ID, new_Salary, new_Email, new_Tenure,))
                elif (action.lower()=='d'):
                    PID_toRemove = input("Enter PID to Remove: ")
                    cursor.execute("DELETE FROM Professor WHERE Professor.PID=?", (PID_toRemove,))

            case 6:     # 6. Students
                if (action.lower()=='a'):
                    print("Please enter the following details: ")
                    """
                    
                    <-- code to obtain new details goes here

                    """
                    cursor.execute("INSERT INTO Professor VALUES (?,?,?,?,?,?)", (new_PID, new_Name, new_Department_ID, new_Salary, new_Email, new_Tenure,))
                elif (action.lower()=='d'):
                    PID_toRemove = input("Enter PID to Remove: ")
                    cursor.execute("DELETE FROM Professor WHERE Professor.PID=?", (PID_toRemove,))

            case 7:     # 7. Majors
                if (action.lower()=='a'):
                    print("Please enter the following details: ")
                    """
                    
                    <-- code to obtain new details goes here

                    """
                    cursor.execute("INSERT INTO Professor VALUES (?,?,?,?,?,?)", (new_PID, new_Name, new_Department_ID, new_Salary, new_Email, new_Tenure,))
                elif (action.lower()=='d'):
                    PID_toRemove = input("Enter PID to Remove: ")
                    cursor.execute("DELETE FROM Professor WHERE Professor.PID=?", (PID_toRemove,))

            case 8:     # 8. Admin
                if (action.lower()=='a'):
                    print("Please enter the following details: ")
                    """
                    
                    <-- code to obtain new details goes here

                    """
                    cursor.execute("INSERT INTO Professor VALUES (?,?,?,?,?,?)", (new_PID, new_Name, new_Department_ID, new_Salary, new_Email, new_Tenure,))
                elif (action.lower()=='d'):
                    PID_toRemove = input("Enter PID to Remove: ")
                    cursor.execute("DELETE FROM Professor WHERE Professor.PID=?", (PID_toRemove,))
            
            case __:
                raise ValueError
    
    except ValueError:
        print("An unexpected error occured.")

    cursor.commit()


def main(username, password):      # returns 0 for unsuccessful login and 1 for successful login
    EXIT_SUCCESS = 1
    cursor.execute("SELECT * FROM admin WHERE username=? AND password=?", (username, password,))
    query = cursor.fetchall()

    if (query):     # condition for successful login
        while (True):
            """
            Interface for admin goes here:
                1. Accessing a table (Printing all the rows from a table)
                2. Modifying a table (Addition/Deletion/Editting Details)
                3. Custom SQL Querying
                4. Exit
            """
            choice = int(input("Enter choice here: "))
            try:    
                match choice:
                    case 1:         # 1. Accessing a table (Printing all the rows from a table)
                        table_choice = admin_select_table()
                        if (table_choice != 0):
                            admin_show_table(table_choice=table_choice)

                    case 2:         # 2. Modifying a table (Addition/Deletion/Editting Details)
                        table_choice = admin_select_table()
                        if (table_choice != 0):
                            action = input("Would you like to add or delete a record? (Enter \'a\' to add, \'d\' to delete): ")
                            admin_edit_table(table_choice=table_choice, action=action)

                    case 3:         # 3. Custom SQL Querying
                        pass

                    case 4:         # 4. Exit
                        print("Thank you, bye!\n")
                        break

                    case __:
                        raise ValueError
            except ValueError:
                print("Choice not found, please try again")

            pass
    else:           # condition for unsuccessful login
        EXIT_SUCCESS = 0
    
    return EXIT_SUCCESS
