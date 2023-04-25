"""
All functions related to a user (student):
    1. Access and modify personal information
    2. Access and modify registered classes
    3. Obtain a list of all professors within the department of their major

"""

import sqlite3

user_conn = sqlite3.connect("user.db")
user_cursor = user_conn.cursor()


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
            user_cursor.execute("UPDATE user SET First_Name=? WHERE UID=?", (new_info, UID,))
            user_conn.commit()
        
        case 2:     # 2. Last Name
            new_info = input("Enter new Last Name: ")
            user_cursor.execute("UPDATE user SET Last_Name=? WHERE UID=?", (new_info, UID,))
            user_conn.commit()

        case 3:     # 3. Date of Birth
            new_info = input("Enter new Date of Birth: ")
            user_cursor.execute("UPDATE user SET Date_of_Birth=? WHERE UID=?", (new_info, UID,))
            user_conn.commit()

        case 4:     # 4. GPA
            new_info = input("Enter new GPA: ")
            user_cursor.execute("UPDATE user SET GPA=? WHERE UID=?", (new_info, UID,))
            user_conn.commit()

        case 5:     # 5. Major ID
            new_info = input("Enter new Major ID: ")
            user_cursor.execute("UPDATE user SET Major_ID=? WHERE UID=?", (new_info, UID,))
            user_conn.commit()

        case 6:     # 6. Undergraduate
            new_info = 0
            user_cursor.execute("UPDATE user SET Undergraduate=? WHERE UID=?", (new_info, UID,))
            user_conn.commit()

        case 7:     # 7. Class Standing
            new_info = input("Enter new Class Standing (Freshman/Sophomore/Junior/Senior): ")
            user_cursor.execute("UPDATE user SET Class_Standing=? WHERE UID=?", (new_info, UID,))
            user_conn.commit()

        case 8:     # 8. Email
            new_info = input("Enter new Email: ")
            user_cursor.execute("UPDATE user SET First_Name=? WHERE UID=?", (new_info, UID,))
            user_conn.commit()

        case 9:     # 9. Phone Number
            new_info = input("Enter new Phone Number: ")
            user_cursor.execute("UPDATE user SET Phone_Number=? WHERE UID=?", (new_info, UID,))
            user_conn.commit()

        case 10:    # 10. Address
            new_info = input("Enter new Address: ")
            user_cursor.execute("UPDATE user SET Address=? WHERE UID=?", (new_info, UID,))
            user_conn.commit()

        case __:
            return 0

    return 1


def main(UID, password):      # returns 0 for unsuccessful login and 1 for successful login
    EXIT_SUCCESS = 1
    user_cursor.execute("SELECT * FROM users WHERE UID=? AND password=?", (UID, password,))
    query = user_cursor.fetchall()

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
                        user_cursor.execute("SELECT * FROM users")
                        user_info = user_cursor.fetchall()
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

                    case 2:     # Editing personal information
                        edit_success = edit_personal_info(UID=UID)
                        while (edit_success==0):
                            print("Error adding information, try again.\n")
                            edit_success = edit_personal_info(UID=UID)
                        print("Personal information successfully editted\n")
                    
                    case 3:     # Viewing registered classes
                        pass

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
    
