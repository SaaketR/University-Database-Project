import sqlite3
import os
from InquirerPy import prompt
import shutil
from pwinput import pwinput

import admin
import student

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

def main():
    while True:
        clrscr()
        print_centre(f"{tcol.BOLD}{tcol.UNDERLINE}{tcol.HEADER}Welcome to Database University{tcol.ENDC}")
        print_centre(f"{tcol.OKGREEN}Go DB's!{tcol.ENDC}")
        try:
            choice = prompt({
                "type": "list",
                "message" : "",
                "choices": ["Student Login", "Admin Login", "QUIT"]
            })
            clrscr()
            match choice[0]:
                case "Student Login":     # User Login 
                    print_centre(f"{tcol.BOLD}{tcol.HEADER}Student Login{tcol.ENDC}")
                    UID = int(input(f"{tcol.BOLD}{tcol.OKCYAN}Enter UID:\t\t{tcol.ENDC}"))
                    password = pwinput(f"{tcol.BOLD}{tcol.OKCYAN}Enter Password:\t\t{tcol.ENDC}")
                    login_success = student.main(UID=UID, password=password)
                    if (login_success==0):
                        print_centre(f"{tcol.BOLD}{tcol.FAIL}Login failed. Try again{tcol.ENDC}")
                        input("Press Enter to continue...")


                case "Admin Login":     # Admin Login 
                    print_centre(f"{tcol.BOLD}{tcol.HEADER}Admin Login{tcol.ENDC}")
                    username = input(f"{tcol.BOLD}{tcol.OKCYAN}Enter Email:\t\t{tcol.ENDC}")
                    password = pwinput(f"{tcol.BOLD}{tcol.OKCYAN}Enter Password:\t\t{tcol.ENDC}")
                    login_success = admin.main(username, password)
                    if (login_success==0):
                        print_centre(f"{tcol.BOLD}{tcol.FAIL}Login failed. Try again{tcol.ENDC}")
                        input("Press Enter to continue...")

                case "QUIT":     # Exit 
                    print("Thank you, bye!")
                    break

                case __:    # <--- Confirm default case syntax surrounding Exceptions 
                    raise ValueError

        except ValueError:
            print("Choice not found, please try again.\n")


main()
