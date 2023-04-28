"""
All functionalities related to creating a new user:
    1. Generating a unique UID
    2. Checking if new user's password meets requirements (8-15 characters, at least one upper case, one digit, and one special character)
    3. Inserting the new user into the database
"""

import sqlite3
from random import randint

conn = sqlite3.connect("Database.db")
cursor = conn.cursor()

# Generating a unique UID
def generate_UID(num):        # return available UID
    new_UID = 0000000
    while (True):
        new_UID = randint((10**num), ((10**(num+1))-1))      # a proposed UID for the new user; can be any 7 digit number
        cursor.execute("SELECT * FROM Students WHERE Students.UID=?", (new_UID,))
        query = cursor.fetchall()      # obtaining query results
        if len(query) == 0:     # condition for proposed UID to be unique
            break

    return new_UID


# Checking if new user's password meets requirements (8-15 characters, at least one upper case, one digit, and one special character)
def check_password(ToCheck):        # return 0 is password does not meet requirements and 1 if the password meets the criteria
    password_success = 0
    containsCapital = 0
    containsSpecial = 0
    containsDigit = 0

    if ((len(ToCheck) >= 8) and (len(ToCheck) <= 15)):      # checking if length requirements are met
        # Checking if password contains atleast one capital letter, one special character, and one digit
        i = 0
        while (i < len(ToCheck)):
            if (ToCheck[i].isupper()):      # Capitals
                containsCapital = 1
            if (ToCheck[i].isalnum() == False):      # Special character
                containsSpecial = 1
            if (ToCheck[i].isdigit()):      # Digit
                containsDigit = 1
            i += 1
            password_success = (containsCapital and containsSpecial and containsDigit)
            if (password_success):
                break
            
    return password_success


# Inserting the new user into the database
def create_new(UID, first_name, last_name, DOB, GPA, major_ID, undergraduate, class_standing, email, password,phone_number,address):      # void function??
    cursor.execute("INSERT INTO Students VALUES (?,?,?,?,?,?,?,?,?,?,?,?)",
                        [UID, first_name, last_name, DOB, GPA, major_ID, email, undergraduate, class_standing, password, phone_number, address])
    conn.commit()
