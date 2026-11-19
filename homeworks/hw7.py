import sqlite3

connect = sqlite3.connect("user.db")
cursor = connect.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS bookings(
        booking_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(30),
        rooms VARCHAR(100),
        check_in NUMERIC,
        check_out NUMERIC,
        booking_date NUMERIC,
        status VARCHAR(20),
        price INT,
        commission INT
    )
''')
connect.commit()


def create_booking(name, rooms, check_in, check_out, booking_date, status, price, commission):
    cursor.execute(
        'INSERT INTO bookings(name, rooms, check_in, check_out, booking_date, status, price, commission) VALUES(?,?,?,?,?,?,?,?)',
        (name, rooms, check_in, check_out, booking_date, status, price, commission)
    )
    print("Новое бронирование!")
    connect.commit()

def get_booking():
    cursor.execute('SELECT * FROM bookings')
    data = cursor.fetchall()
    for i in data:
        print(i)

def update_booking(row_id, name):
    cursor.execute(
        'UPDATE bookings SET name = ? WHERE rowid = ?',
        ( name, row_id)
    )
    print("Бронирование обнавлено!")
    connect.commit()

def deleate_booking(rowid):
    cursor.execute(
        'DELETE FROM bookings WHERE rowid = ?',
        (rowid,)

    )
    connect.commit()
    print('бронирование удалено!')




# create_booking('David Jackson', 'стандарт', '15-12-2026', '17-12-2026', '10-12-2026', 'Cancelled', 70, 7)
# get_booking()
# update_booking(2,'GOAT')
deleate_booking(3)