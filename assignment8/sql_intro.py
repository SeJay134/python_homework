import sqlite3 

def publishers_add(cursor, name):
    try:
        cursor.execute("INSERT INTO publishers (name) VALUES (?)", (name,) )
    except sqlite3.IntegrityError:
        print(f"{name} is already in the database.")

def magazines_add(cursor, name, publisher_id):
    try:
        cursor.execute("INSERT INTO magazines (name, publisher_id) VALUES (?,?)", (name, publisher_id) )
    except sqlite3.IntegrityError:
        print(f"{name} is already in the database.")

def subscribers_add(cursor, name, address):
    try:
        cursor.execute("INSERT INTO subscribers (name, address) VALUES (?,?)", (name, address) )
    except sqlite3.IntegrityError:
        print(f"{name} is already in the database.")

def subscriptions_add(cursor, subscriber_id, magazines_id, expiration_date):
    try:
        cursor.execute("SELECT * FROM subscribers WHERE name = ?", (subscriber_id))
        results = cursor.fetchall()
        if len(results) > 0:
            subscriber_id = results[0][0]
        else:
            print(f"There was no subscriber named {subscriber_id}.")
            return
        
        cursor.execute("SELECT * FROM magazines WHERE name = ?", (magazines_id))
        results = cursor.fetchall()
        if len(results) > 0:
            magazines_id = results[0][0]
        else:
            print(f"There was no magazine named {magazines_id}.")
            return

    try:   
        cursor.execute("INSERT INTO subscriptions (expiration_date) VALUES (?)", (expiration_date,) )
    except sqlite3.IntegrityError:
        print(f"{expiration_date} is already in the database.")

    except sqlite3.IntegrityError:
        print(f"{name} is already in the database.")

try:
    with sqlite3.connect("../db/magazines.db") as conn:
        conn.execute("PRAGMA foreign_keys = 1")
        cursor = conn.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS publishers (
            publishers_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL UNIQUE
        )
        """)

        publishers_add(cursor, 'Computer Science')

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS magazines (
            magazines_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL UNIQUE,
            publisher_id INTEGER NOT NULL,
            FOREIGN KEY (publisher_id) REFERENCES publishers (publishers_id)
        )
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS subscribers (
            subscribers_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            address TEXT NOT NULL
        )
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS subscriptions (
            subscription_id INTEGER PRIMARY KEY,
            subscriber_id INTEGER NOT NULL,
            magazines_id INTEGER NOT NULL,
            expiration_date TEXT NOT NULL,
            FOREIGN KEY (subscriber_id) REFERENCES subscribers (subscribers_id),
            FOREIGN KEY (magazines_id) REFERENCES magazines (magazines_id)
        )
        """)

        conn.commit()

        print("Tables created successfully.")
except sqlite3.Error as e:
    print("An error occurred:", e)




