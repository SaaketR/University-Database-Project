"""
All functions related to a Students (student):
    1. View personal information
    2. Edit personal information
    3. Access registered classes
    4. Modiying the list of registered classes (add/remove)
    5. Obtain a list of all professors within the department of the students major

"""

import sqlite3

# Database connections
conn = sqlite3.connect("Database.db")
cursor = conn.cursor()

import os
from InquirerPy import prompt
import shutil
from pwinput import pwinput

class tcol:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def print_centre(s):
    print(s.center(shutil.get_terminal_size().columns))

def clrscr():
    os.system('cls' if os.name=='nt' else 'clear')


# Printing a Students information given a student's UID; returns void 
def view_personal_info(UID): 
    cursor.execute("SELECT * FROM students WHERE UID=?", (UID,))
    Students_info = cursor.fetchall()
    print("First Name:\t\t\t", Students_info[0][1])
    print("Last Name:\t\t\t", Students_info[0][2])
    print("Date of Birth:\t\t\t", Students_info[0][3])
    print("Grade Point Average (GPA):\t", Students_info[0][4])
    print("Major ID:\t\t\t", Students_info[0][5])
    print("Undergraduate:\t\t\t", Students_info[0][6])
    print("Class Standing:\t\t\t", Students_info[0][7])
    print("Email:\t\t\t\t", Students_info[0][8])
    print("Phone Number:\t\t\t", Students_info[0][9])
    print("Address:\t\t\t", Students_info[0][10])
    print("\n")



# Editing personal information: return 0 for successful change, 1 for unsuccessful change 
def edit_personal_info(UID): 
    """
    Present all editable personal information as a list of choices:
        1. First Name
        2. Last Name
        3. Date of Birth
        4. GPA
        5. Major ID
        6. Undergraduate
        7. Class Standing
        8. Email
        9. Phone Number
        10. Address

    """

    choice = prompt({
                    "type": "list",
                    "message" : "",
                    "choices": ["First Name","Last Name","Date of Birth","GPA","Major ID","Undergraduate","Class Standing","Email","Phone Number","Address","CANCEL"]
                })

    match choice[0]:
        case "First Name":     # 1. First Name
            new_info = input("Enter new First Name: ")
            cursor.execute("UPDATE Students SET First_Name=? WHERE UID=?", (new_info, UID,))
        
        case "Last Name":     # 2. Last Name
            new_info = input("Enter new Last Name: ")
            cursor.execute("UPDATE Students SET Last_Name=? WHERE UID=?", (new_info, UID,))

        case "Date of Birth":     # 3. Date of Birth
            new_info = input("Enter new Date of Birth: ")
            cursor.execute("UPDATE Students SET Date_of_Birth=? WHERE UID=?", (new_info, UID,))

        case "GPA":     # 4. GPA
            new_info = input("Enter new GPA: ")
            cursor.execute("UPDATE Students SET GPA=? WHERE UID=?", (new_info, UID,))

        case "Major ID":     # 5. Major ID
            new_info = input("Enter new Major ID: ")
            cursor.execute("UPDATE Students SET Major_ID=? WHERE UID=?", (new_info, UID,))

        case "Undergraduate":     # 6. Undergraduate
            new_info = 0
            cursor.execute("UPDATE Students SET Undergraduate=? WHERE UID=?", (new_info, UID,))

        case "Class Standing":     # 7. Class Standing
            new_info = input("Enter new Class Standing (Freshman/Sophomore/Junior/Senior): ")
            cursor.execute("UPDATE Students SET Class_Standing=? WHERE UID=?", (new_info, UID,))

        case "Email":     # 8. Email
            new_info = input("Enter new Email: ")
            cursor.execute("UPDATE Students SET First_Name=? WHERE UID=?", (new_info, UID,))

        case "Phone Number":     # 9. Phone Number
            new_info = input("Enter new Phone Number: ")
            cursor.execute("UPDATE Students SET Phone=? WHERE UID=?", (new_info, UID,))

        case "Address":    # 10. Address
            new_info = input("Enter new Address: ")
            cursor.execute("UPDATE Students SET Address=? WHERE UID=?", (new_info, UID,))

        case "CANCEL":
            return 1

        case __:
            return 0

    print("Personal information successfully editted\n")
    conn.commit()
    return 1


# Printing the registered classes given a student's UID; returns void
def view_registered_classes(UID):
    cursor.execute("""
                    SELECT Registered.Section_ID, Section.Section_Number, Section.Course_ID, Course.Course_Name, Professor.Name, Section.Term, Course.Credits
                    FROM Registered, Section, Course, Professor
                    WHERE Registered.UID=?
                        AND Section.Section_ID=Registered.Section_ID
                        AND Course.Course_ID=Section.Course_ID
                        AND Professor.PID=Section.Professor_ID
                    """, (UID,))        # Joining Registered, Section, COurse, and Professor
    query = cursor.fetchall()
    
    if (len(query) > 0):
        print("{:<20} {:<20} {:<20} {:<20} {:<20} {:<20} {:<20}\n".format("Section_ID", "Section_Number", "Course_ID", "Course_Name", "Professor_Name", "Term", "Credits"))
        print("-----------------------------------------------------------------")
        i = 0
        while (i < len(query)):
            print("{:<20} {:<20} {:<20} {:<20} {:<20} {:<20} {:<20}\n".format(query[i][0], query[i][1], query[i][2], query[i][3], query[i][4], query[i][5], query[i][6]))
            i+=1
    else:
        print("No classes found\n")


# Ability to modify registered classes given a student's UID; returns void. Presents the user with the choice to either add class by Section_ID or remove class by Section_ID
def edit_registered_classes(UID):
    """
    Edit Registered Classes interface goes here. Present the user with 2 options:
        1. Add Class
        2. Remove Class

    """
    choice = prompt({
        "type" : "list",
        "message" : "",
        "choices" : ["Register Class","Remove Class","CANCEL"]
    })
    try:
        match choice[0]:
            case "Register Class":     # Add class
                section_To_Add = int(input("Enter Section ID to add: "))
                cursor.execute("SELECT * FROM Registered WHERE Registered.UID=? AND Registered.Section_ID=?", (UID, section_To_Add))
                query = cursor.fetchall()
                if (query):
                    print("Class already added in your list!\n")
                else:
                    cursor.execute("INSERT INTO Registered VALUES (?,?)", (UID, section_To_Add,))
                    conn.commit()
                    print("Course successfully added!\n")


            case "Remove Class":     # Remove class
                section_To_Remove = int(input("Enter Section ID to add: "))
                cursor.execute("SELECT * FROM Registered WHERE Registered.UID=? AND Registered.Section_ID=?", (UID, section_To_Remove))
                query = cursor.fetchall()
                if (query):
                    cursor.execute("DELETE FROM Registered WHERE Registered.Section_ID=?", (section_To_Remove,))
                    conn.commit()
                    print("Course successfully deleted!\n")
                else:
                    print("No such class in your list!\n")

            case __:
                raise ValueError
    except ValueError:
        print("Enter valid choice.")


# Obtaining a list of all professors within the department of the students major; returns void
def list_professors(UID):
    cursor.execute("""
                    SELECT Professor.Name, Professor.Email
                    FROM Professor, Students, Majors
                    WHERE Students.UID=?
                        AND Majors.Major_ID=Students.Major_ID
                        AND Majors.Department_ID=Professor.Department_ID
                    """, (UID,))
    query = cursor.fetchall()

    if (query):     # Checking if any professor exists
        print("{:<20} {:<20}\n".format("Professor Name", "Professor Email"))
        print("-----------------------------------------\n")
        i = 0
        while (i < len(query)):
            print("{:<20} {:<20}\n".format(query[i][0], query[i][1]))
            i+=1
    else:
        print("No such professors found!\n")


# returns 0 for unsuccessful login and 1 for successful login
def main(UID, password):      
    EXIT_SUCCESS = 1
    cursor.execute("SELECT * FROM Students WHERE UID=? AND password=?", (UID, password,))
    query = cursor.fetchall()

    if (query):     # condition for successful login
        while (True):
            """
            Student interface goes here:
                1. View personal information
                2. Edit personal information
                3. Access registered classes
                4. Modiying the list of registered classes (add/remove)
                5. Obtain a list of all professors within the department of the students major
            """

            try:
                clrscr()
                print_centre(f"{tcol.HEADER}{tcol.BOLD}STUDENT PORTAL{tcol.ENDC}")
                choice = prompt({
                    "type": "list",
                    "message" : "",
                    "choices": ["View personal information","Edit personal information", "Access registered classes", "Modiying the list of registered classes (add/remove)","Obtain a list of all professors within the department of the students major","LOGOUT"]
                })
                match choice[0]:
                    case "LOGOUT":
                        break

                    case "View personal information":     # Viewing personal information
                        view_personal_info(UID=UID)
                        input("Press Enter to continue...")

                    case "Edit personal information":     # Editing personal information by calling the edit_personal_info() function declared in this file
                        edit_success = edit_personal_info(UID=UID)
                        while (edit_success==0):
                            print("Error adding information, try again.\n")
                            edit_success = edit_personal_info(UID=UID)
                        input("Press Enter to continue...")
                    
                    case "Access registered classes":     # Viewing registered classes
                        view_registered_classes(UID=UID)
                        input("Press Enter to continue...")

                    case "Modiying the list of registered classes (add/remove)":     # Modiying classes list
                        edit_registered_classes(UID=UID)
                        input("Press Enter to continue...")
                        

                    case "Obtain a list of all professors within the department of the students major":     # Viewing all professors within the department
                        list_professors(UID=UID)
                        input("Press Enter to continue...")

                    case __:        # Default
                        raise ValueError
            except ValueError:
                print("Choice not found, try again.\n")


    else:           # condition for unsuccessful login
        EXIT_SUCCESS = 0
    
    return EXIT_SUCCESS
    
