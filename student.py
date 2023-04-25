"""
All functions related to a user (student):
    1. View personal information
    2. Edit personal information
    3. Access registered classes
    4. Modiying the list of registered classes (add/remove)
    5. Obtain a list of all professors within the department of the students major

"""

import sqlite3

# Database connections
            # conn = sqlite3.connect("Students.db")              # Students
            # cursor = conn.cursor()
            # registered_conn = sqlite3.connect("Registered.db")          # Registered
            # registered_cursor = registered_conn.cursor()
            # section_conn = sqlite3.connect("Section.db")                # Section
            # section_cursor = section_conn.cursor()
            # courses_conn = sqlite3.connect("Courses.db")                # Courses
            # courses_cursor = courses_conn.cursor()
            # professor_conn = sqlite3.connect("Professor.db")            # Professor
            # professor_cursor = professor_conn.cursor()
conn = sqlite3.connect("Database.db")
cursor = conn.cursor()


# Printing a user information given a student's UID; returns void 
def view_personal_info(UID): 
    cursor.execute("SELECT * FROM users")
    user_info = cursor.fetchall()
    print("First Name: ", user_info[0][1])
    print("Last Name: ", user_info[0][2])
    print("Date of Birth: ", user_info[0][3])
    print("Grade Point Average (GPA): ", user_info[0][4])
    print("Major ID: ", user_info[0][5])
    print("Undergraduate: ", user_info[0][6])
    print("Class Standing: ", user_info[0][7])
    print("Email: ", user_info[0][8])
    print("Phone Number: ", user_info[0][9])
    print("Address: ", user_info[0][10])


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
            cursor.execute("UPDATE user SET First_Name=? WHERE UID=?", (new_info, UID,))
        
        case 2:     # 2. Last Name
            new_info = input("Enter new Last Name: ")
            cursor.execute("UPDATE user SET Last_Name=? WHERE UID=?", (new_info, UID,))

        case 3:     # 3. Date of Birth
            new_info = input("Enter new Date of Birth: ")
            cursor.execute("UPDATE user SET Date_of_Birth=? WHERE UID=?", (new_info, UID,))

        case 4:     # 4. GPA
            new_info = input("Enter new GPA: ")
            cursor.execute("UPDATE user SET GPA=? WHERE UID=?", (new_info, UID,))

        case 5:     # 5. Major ID
            new_info = input("Enter new Major ID: ")
            cursor.execute("UPDATE user SET Major_ID=? WHERE UID=?", (new_info, UID,))

        case 6:     # 6. Undergraduate
            new_info = 0
            cursor.execute("UPDATE user SET Undergraduate=? WHERE UID=?", (new_info, UID,))

        case 7:     # 7. Class Standing
            new_info = input("Enter new Class Standing (Freshman/Sophomore/Junior/Senior): ")
            cursor.execute("UPDATE user SET Class_Standing=? WHERE UID=?", (new_info, UID,))

        case 8:     # 8. Email
            new_info = input("Enter new Email: ")
            cursor.execute("UPDATE user SET First_Name=? WHERE UID=?", (new_info, UID,))

        case 9:     # 9. Phone Number
            new_info = input("Enter new Phone Number: ")
            cursor.execute("UPDATE user SET Phone_Number=? WHERE UID=?", (new_info, UID,))

        case 10:    # 10. Address
            new_info = input("Enter new Address: ")
            cursor.execute("UPDATE user SET Address=? WHERE UID=?", (new_info, UID,))

        case __:
            return 0

    conn.commit()
    return 1


# Printing the registered classes given a student's UID; returns void
def view_registered_classes(UID):
    """
    Proposed query:

    SELECT Registered.sectionID, Section.sectionName, Section.courseID, courses.courseName, Professor.Name, Section.term
    FROM Registered, Section, courses, Professor
    WHERE Registered.UID=UID 
            AND Section.sectionID=Registered.sectionID
            AND courses.courseID=Section.courseID
            AND professor.PID=Section.professorID
    """


    
    pass


# returns 0 for unsuccessful login and 1 for successful login
def main(UID, password):      
    EXIT_SUCCESS = 1
    cursor.execute("SELECT * FROM users WHERE UID=? AND password=?", (UID, password,))
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

                    case 4:     # Modifying registered classes
                        pass

                    case 5:     # Viewing all professors within the department
                        pass

                    case __:        # Default
                        raise ValueError
            except ValueError:
                print("Choice not found, try again.\n")


    else:           # condition for unsuccessful login
        EXIT_SUCCESS = 0
    
    return EXIT_SUCCESS
    
