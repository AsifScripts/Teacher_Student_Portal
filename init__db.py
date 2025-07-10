import sqlite3
from werkzeug.security import generate_password_hash

def init_database():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    c.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        email TEXT NOT NULL,
        password TEXT NOT NULL
    )
    ''')

    c.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        subject TEXT NOT NULL,
        marks INTEGER NOT NULL
    )
    ''')

    hashed_pwd = generate_password_hash("Wild@Asif12")
    c.execute("INSERT INTO users (username, email, password) VALUES (?, ?, ?)",
              ("asif", "asif1bit@gmail.com", hashed_pwd))

    conn.commit()
    conn.close()
