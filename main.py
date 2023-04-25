import sqlite3

import admin
import user
import new_user
import user
import admin

def main():
    while True:
        """
        Login interface goes here
            1. User Login
            2. Admin Login
            3. New User
            4. Exit

        """

        try:
            choice = int(input("Enter choice: "))

            match choice:
                case 1:     # User Login 
                    UID = int(input("Enter UID: "))
                    password = input("Enter Password: ")
                    login_success = user.main(UID=UID, password=password)
                    if (login_success==0):
                        print("Login failed. Try again")


                case 2:     # Admin Login 
                    username = input("Enter Username: ")
                    password = input("Enter Password: ")
                    login_success = admin.main(username, password)
                    if (login_success==0):
                        print("Login failed. Try again")


                case 3:     # New User Login 
                    print("Please enter your details below: ")

                    first_name = input("Enter First Name: ")
                    last_name = input("Enter Last Name: ")
                    birth = input("Enter Date of Birth: ")
                    gpa = int(input("Enter GPA: "))
                    major_ID = int(input("Enter Major ID: "))

                    undergraduate_check = input("Are you an undergraduate student? (Y/N): ")
                    undergraduate = 1
                    if (undergraduate_check.upper() == "N"):
                        undergraduate = 0
                    
                    class_standing = input("Enter class standing (Freshman/Sophomore/Junior/Senior): ")

                    email = input("Enter Email: ")
                    phone = int(input("Enter Phone Number: "))
                    address = input("Enter Address: ")
                    

                    new_UID = new_user.generate_UID()

                    password_success = 0
                    while (password_success==0):
                        print("Your new UID is {}. Password should contain 8-15 characters and should be a mix of upper case alphabets, digits, and special characters\n")
                        password = input("Enter password: ")
                        password_success = new_user.check_password(password)
                        if (password_success==0):
                            print("Password does not meet requirement, try again.\n")
                            continue
                    
                    new_user.create_new(UID=new_UID, 
                                        first_name=first_name, 
                                        last_name=last_name, 
                                        DOB=birth, 
                                        GPA=gpa,
                                        major_ID=major_ID,
                                        undergraduate=undergraduate,
                                        class_standing=class_standing,
                                        email=email,
                                        phone_number=phone,
                                        address=address,
                                        password=password
                                        )

                    print("Welcome aboard {}! Your details are now in our record. You are now being redirected to our homepage.")


                case 4:     # Exit 
                    print("Thank you, bye!")
                    break


                case __:    # <--- Confirm default case syntax surrounding Exceptions 
                    raise ValueError

        except ValueError:
            print("Choice not found, please try again.\n")

main()
