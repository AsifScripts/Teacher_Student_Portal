import sqlite3

conn = sqlite3.connect("database.db")

conn.execute("DROP TABLE IF EXISTS users;")
conn.execute("DROP TABLE IF EXISTS students;")

conn.execute("""
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    password TEXT
)
""")

conn.execute("""
CREATE TABLE students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    subject TEXT,
    marks INTEGER
)
""")

# Insert dummy user (use plain or hashed password based on app logic)
conn.execute("INSERT INTO users (username, password) VALUES (?, ?)", ("asif", "admin123"))

conn.commit()
conn.close()

print("✅ Test DB initialized.")
