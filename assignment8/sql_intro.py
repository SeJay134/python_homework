import sqlite3 

# publishers
def publishers_add(cursor, name):
    try:
        cursor.execute("INSERT INTO publishers (name) VALUES (?)", (name,) )
    except sqlite3.IntegrityError:
        print(f"{name} is already in the database.")

# magazines
def magazines_add(cursor, name, publisher_id):
    try:
        cursor.execute("INSERT INTO magazines (name, publisher_id) VALUES (?,?)", (name, publisher_id) )
    except sqlite3.IntegrityError:
        print(f"{name} is already in the database.")

# subscribers
def subscribers_add(cursor, name, address):
    cursor.execute(
        "SELECT * FROM subscribers WHERE name = ? AND address = ?",
        (name, address)
    )

    if cursor.fetchall():
        print("Subscriber already exists.")
        return

    cursor.execute(
        "INSERT INTO subscribers (name, address) VALUES (?, ?)",
        (name, address)
    )

# subscriptions
def subscriptions_add(cursor, subscriber_name, magazine_name, expiration_date):
    try:
        # subscriber_id
        cursor.execute("SELECT subscribers_id FROM subscribers WHERE name = ?", (subscriber_name,))
        result = cursor.fetchall()
        if len(result) == 0:
            print(f"There was no subscriber named {subscriber_name}.")
            return
        subscriber_id = result[0][0]

        # magazines_id
        cursor.execute("SELECT magazines_id FROM magazines WHERE name = ?", (magazine_name,))
        result = cursor.fetchall()
        if len(result) == 0:
            print(f"There was no magazine named {magazine_name}.")
            return
        magazines_id = result[0][0]

        cursor.execute(
            """
            INSERT INTO subscriptions (subscriber_id, magazines_id, expiration_date)
            VALUES (?, ?, ?)
            """,
            (subscriber_id, magazines_id, expiration_date)
        )

    except sqlite3.IntegrityError:
        print("This subscription already exists.")

try:
    with sqlite3.connect("../db/magazines.db") as conn:
        conn.execute("PRAGMA foreign_keys = 1")
        cursor = conn.cursor()

# publishers
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS publishers (
            publishers_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL UNIQUE
        )
        """)

# magazines
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS magazines (
            magazines_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL UNIQUE,
            publisher_id INTEGER NOT NULL,
            FOREIGN KEY (publisher_id) REFERENCES publishers (publishers_id)
        )
        """)

# subscribers
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS subscribers (
            subscribers_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            address TEXT NOT NULL
        )
        """)

# subscriptions
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

        publishers_add(cursor, 'Computer Science')
        publishers_add(cursor, "Tech Press")
        publishers_add(cursor, "Science World")

        magazines_add(cursor, "AI Monthly", 1)
        magazines_add(cursor, "Data Weekly", 1)
        magazines_add(cursor, "Science Today", 2)

        subscribers_add(cursor, "Alice", "NY")
        subscribers_add(cursor, "Bob", "LA")
        subscribers_add(cursor, "Charlie", "TX")

        subscriptions_add(cursor, "Alice", "AI Monthly", "2026-01-01")
        subscriptions_add(cursor, "Bob", "Data Weekly", "2025-12-31")
        subscriptions_add(cursor, "Charlie", "Science Today", "2026-06-01")

        conn.commit()
        print()

# All subscribers
        cursor.execute("SELECT * FROM subscribers")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        print()

# all magazines sorted by name
        cursor.execute("SELECT * FROM magazines ORDER BY name")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        print()

# magazines for a particular publisher
        publisher_name = "Computer Science"
        cursor.execute("SELECT magazines.name FROM magazines JOIN publishers ON magazines.publisher_id = publishers.publishers_id WHERE publishers.name = ?", (publisher_name,))
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        print()
        
        print("Tables created successfully.")
except sqlite3.Error as e:
    print("An error occurred:", e)




