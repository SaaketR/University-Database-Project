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


# Printing a Students information given a student's UID; returns void 
def view_personal_info(UID): 
    cursor.execute("SELECT * FROM students WHERE UID=?", (UID,))
    Students_info = cursor.fetchall()
    print("First Name: ", Students_info[0][1])
    print("Last Name: ", Students_info[0][2])
    print("Date of Birth: ", Students_info[0][3])
    print("Grade Point Average (GPA): ", Students_info[0][4])
    print("Major ID: ", Students_info[0][5])
    print("Undergraduate: ", Students_info[0][6])
    print("Class Standing: ", Students_info[0][7])
    print("Email: ", Students_info[0][8])
    print("Phone Number: ", Students_info[0][9])
    print("Address: ", Students_info[0][10])


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
    choice = int(input("What information would you like to edit? (1-10): "))

    match choice:
        case 1:     # 1. First Name
            new_info = input("Enter new First Name: ")
            cursor.execute("UPDATE Students SET First_Name=? WHERE UID=?", (new_info, UID,))
        
        case 2:     # 2. Last Name
            new_info = input("Enter new Last Name: ")
            cursor.execute("UPDATE Students SET Last_Name=? WHERE UID=?", (new_info, UID,))

        case 3:     # 3. Date of Birth
            new_info = input("Enter new Date of Birth: ")
            cursor.execute("UPDATE Students SET Date_of_Birth=? WHERE UID=?", (new_info, UID,))

        case 4:     # 4. GPA
            new_info = input("Enter new GPA: ")
            cursor.execute("UPDATE Students SET GPA=? WHERE UID=?", (new_info, UID,))

        case 5:     # 5. Major ID
            new_info = input("Enter new Major ID: ")
            cursor.execute("UPDATE Students SET Major_ID=? WHERE UID=?", (new_info, UID,))

        case 6:     # 6. Undergraduate
            new_info = 0
            cursor.execute("UPDATE Students SET Undergraduate=? WHERE UID=?", (new_info, UID,))

        case 7:     # 7. Class Standing
            new_info = input("Enter new Class Standing (Freshman/Sophomore/Junior/Senior): ")
            cursor.execute("UPDATE Students SET Class_Standing=? WHERE UID=?", (new_info, UID,))

        case 8:     # 8. Email
            new_info = input("Enter new Email: ")
            cursor.execute("UPDATE Students SET First_Name=? WHERE UID=?", (new_info, UID,))

        case 9:     # 9. Phone Number
            new_info = input("Enter new Phone Number: ")
            cursor.execute("UPDATE Students SET Phone_Number=? WHERE UID=?", (new_info, UID,))

        case 10:    # 10. Address
            new_info = input("Enter new Address: ")
            cursor.execute("UPDATE Students SET Address=? WHERE UID=?", (new_info, UID,))

        case __:
            return 0

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
    else:
        print("No classes found\n")


# Ability to modify registered classes given a student's UID; returns void. Presents the user with the choice to either add class by Section_ID or remove class by Section_ID
def edit_registered_classes(UID):
    """
    Edit Registered Classes interface goes here. Present the user with 2 options:
        1. Add Class
        2. Remove Class

    """
    choice = int(input("Enter your choice here: "))
    try:
        match choice:
            case 1:     # Add class
                section_To_Add = int(input("Enter Section ID to add: "))
                cursor.execute("SELECT * FROM Registered WHERE Registered.UID=? AND Registered.Section_ID=?", (UID, section_To_Add))
                query = cursor.fetchall()
                if (query):
                    print("Class already added in your list!\n")
                else:
                    cursor.execute("INSERT INTO Registered VALUES (?,?)", (UID, section_To_Add,))
                    conn.commit()
                    print("Course successfully added!\n")


            case 2:     # Remove class
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
                    WHERE Student.UID=?
                        AND Majors.Major_ID=Student.Major_ID
                        AND Major.Department_ID=Professor.Department_ID
                    """, (UID,))
    query = cursor.fetchall()

    if (query):     # Checking if any professor exists
        print("{:<20} {:<20}\n".format("Professor Name", "Professor Email"))
        print("-----------------------------------------\n")
        i = 0
        while (i < len(query)):
            print("{:<20} {:<20}\n".format(query[i][0], query[i][1]))
    else:
        print("No such professors found!\n")


# returns 0 for unsuccessful login and 1 for successful login
def main(UID, password):      
    EXIT_SUCCESS = 1
    cursor.execute("SELECT * FROM Studentss WHERE UID=? AND password=?", (UID, password,))
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
                choice = int(input("Enter your choice: "))
                match choice:
                    case 1:     # Viewing personal information
                        view_personal_info(UID=UID)

                    case 2:     # Editing personal information by calling the edit_personal_info() function declared in this file
                        edit_success = edit_personal_info(UID=UID)
                        while (edit_success==0):
                            print("Error adding information, try again.\n")
                            edit_success = edit_personal_info(UID=UID)
                        print("Personal information successfully editted\n")
                    
                    case 3:     # Viewing registered classes
                        view_registered_classes(UID=UID)

                    case 4:     # Modiying classes list
                        edit_registered_classes(UID=UID)
                        

                    case 5:     # Viewing all professors within the department
                        list_professors(UID=UID)

                    case __:        # Default
                        raise ValueError
            except ValueError:
                print("Choice not found, try again.\n")


    else:           # condition for unsuccessful login
        EXIT_SUCCESS = 0
    
    return EXIT_SUCCESS
    
