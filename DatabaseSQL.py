import sqlite3

conn = sqlite3.connect("database.db")

c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS user_logins(
        username text,
        password text
        )""")  # creates the database with the users credentials

conn.commit()
