import sqlite3

connect = sqlite3.connect("grades.db")
cursor = connect.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS bookings(
        booking_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(30),
        age INTEGER NOT NULL
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS grades(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
    )
''')