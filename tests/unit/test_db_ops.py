import unittest
import sqlite3
import sys
import os

# Add the project root to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from app import get_db_connection  # (optional: only if you plan to test this)

class TestDatabaseOps(unittest.TestCase):
    def setUp(self):
        # Use in-memory database for isolation and speed
        self.conn = sqlite3.connect(":memory:")
        self.conn.execute('''
            CREATE TABLE students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                subject TEXT NOT NULL,
                marks INTEGER NOT NULL
            )
        ''')

    def test_add_student(self):
        self.conn.execute("INSERT INTO students (name, subject, marks) VALUES (?, ?, ?)", ("Asif", "Math", 90))
        student = self.conn.execute("SELECT * FROM students WHERE name = 'Asif'").fetchone()

        # Assert that student was inserted correctly
        self.assertIsNotNone(student)
        self.assertEqual(student[1], "Asif")
        self.assertEqual(student[2], "Math")
        self.assertEqual(student[3], 90)

    def tearDown(self):
        self.conn.close()

if __name__ == "__main__":
    unittest.main()