import sqlite3


connect = sqlite3.connect("cinema.db")
cursor = connect.cursor()


cursor.execute('''
    CREATE TABLE IF NOT  EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(30)
    )
''')
cursor.execute('''
    CREATE TABLE IF NOT EXISTS movies(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title VARCHAR(30),
        genre VARCHAR(20)
    )
''')
cursor.execute('''
    CREATE TABLE IF NOT EXISTS reviews(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        movie_id INTEGER NOT NULL,
        rating INTEGER NOT NULL,
        FOREIGN KEY(user_id) REFERENCES users(id),
        FOREIGN KEY(movie_id) REFERENCES movies(id)   
    )
''')
connect.commit()



def create_user():
    cursor.executemany(
        'INSERT INTO users(name) VALUES (?)',
        [
            ('Dastan',),
            ('Alex',),
            ('John',),
            ('Emma',),
            ('David',)
        ]
    )

def create_movie():
    cursor.executemany(
        'INSERT INTO movies(title, genre) VALUES (?,?)',
        [
            ('Interstellar', 'Sci-Fi'),
            ('Inception', 'Sci-Fi'),
            ('Titanic', 'Romance'),
            ('The Dark Knight', 'Action'),
            ('Avatar', 'Fantasy')
        ]
    )
def create_review():
    cursor.executemany(
        'INSERT INTO reviews(user_id, movie_id, rating) VALUES (?,?,?)',
        [
            (1, 1, 10),
            (2, 3, 8),
            (3, 2, 9),
            (4, 5, 7),
            (5, 4, 10)
        ]
    )
#
# create_review()
# create_movie()
# create_user()

connect.commit()

def get_all():
    cursor.execute('''
        SELECT users.name, movies.title, movies.genre, reviews.rating
        FROM reviews
        JOIN users ON reviews.user_id = users.id
        JOIN movies ON reviews.movie_id = movies.id
    ''')

    data = cursor.fetchall()
    for i in data:
        print(f'пользователь: {i[0]}, просмотренный фильм: {i[1]}, жантр фильма: {i[2]}, оченка ползователя: {i[3]}')

# get_all()

def get_best_rating():
    cursor.execute('''
        SELECT MAX(rating) 
        FROM reviews
        
    ''')
    data = cursor.fetchone()
    print(*data)


def get_worst_rating():
    cursor.execute('''
        SELECT MIN(rating)
        FROM reviews

    ''')


    data = cursor.fetchone()
    print(*data)


def get_avarege_rating():
    cursor.execute('''
        SELECT AVG(rating)
        FROM reviews

    ''')
    data = cursor.fetchone()
    print(*data)



get_best_rating()
get_worst_rating()
get_avarege_rating()