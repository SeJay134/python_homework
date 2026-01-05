import sqlite3 

try:
    with sqlite3.connect("../db/magazines.db") as conn:
        print("Database created and connected successfully.")
except sqlite3.Error as e:
    print("An error occurred:", e)

    