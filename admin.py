"""
All functions related to an admin:
    1. Addition to a table
    2. Removal from a table
    3. Modifying a table

"""

import sqlite3

conn = sqlite3.connect("Database.db")
cursor = conn.cursor()

def main(username, password):      # returns 0 for unsuccessful login and 1 for successful login
    EXIT_SUCCESS = 1
    cursor.execute("SELECT * FROM admin WHERE username=? AND password=?", (username, password,))
    query = cursor.fetchall()

    if (query):     # condition for successful login
        # <--- code for admin menu
        pass
    else:           # condition for unsuccessful login
        EXIT_SUCCESS = 0
    
    return EXIT_SUCCESS
