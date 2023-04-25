"""
All functions related to a user (student):
    1. Access and modify personal information
    2. Access and modify registered classes
    3. Obtain a list of all professors within the department of their major
    
"""

import sqlite3

user_conn = sqlite3.connect("user.db")
user_cursor = user_conn.cursor()

def main(UID, password):      # returns 0 for unsuccessful login and 1 for successful login
    EXIT_SUCCESS = 1
    user_cursor.execute("SELECT * FROM users WHERE UID=? AND password=?", (UID, password))
    query = user_cursor.fetchall()

    if (query):     # condition for successful login
        # <--- code for user menu
        pass
    else:           # condition for unsuccessful login
        EXIT_SUCCESS = 0
    
    return EXIT_SUCCESS
    
