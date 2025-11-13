import sqlite3 as database
from datetime import datetime

from faker import Faker

connection = database.connect("my_sql_lite.db")
cursor = connection.cursor()


def create_tables():
    query = """
            CREATE TABLE IF NOT EXISTS student
            (
                id
                INTEGER
                PRIMARY
                KEY
                AUTOINCREMENT,
                name
                TEXT
                NOT
                NULL,
                date_of_birth
                TEXT,
                email
                TEXT
                UNIQUE,
                enrollment_date
                TEXT
            );"""

    cursor.execute(query)
    connection.commit()


class User():
    def __init__(self, id, name, email, date_of_birth, enrollment_date):
        self.id = id
        self.name = name
        self.email = email
        self.date_of_birth = date_of_birth
        self.enrollment_date = enrollment_date

    def __repr__(self):
        return f"id={self.id}, name={self.name}, email={self.email}, date_of_birth={self.date_of_birth}, enrollment_date={self.enrollment_date}"


def insert_into_student():
    students = prepare_insert_data()
    print('students', students)
    if students:
        query = """
                INSERT INTO student (name, email, date_of_birth, enrollment_date)
                values (?, ?, ?, ?) \
                """
        cursor.executemany(query, students)
        connection.commit()


def prepare_insert_data():
    faker: Faker = Faker()

    users = []
    for a in range(0, 0):
        first_name = faker.first_name()
        last_name = faker.last_name()
        name = "{} {}".format(first_name, last_name)

        email = "{}{}@gmail.com".format(first_name, last_name)
        enrollment_date = datetime.now()
        fake_dob = faker.date_of_birth(minimum_age=18, maximum_age=90)  # You can specify age range
        user = User(id, name, email, fake_dob, enrollment_date)
        users.append((name, email, fake_dob, enrollment_date))
        # users.append(user)
    return users


def update_student():
    cursor.execute("Update student set date_of_birth='1997-07-27' where email='MaryBarnes@gmail.com'")
    connection.commit()


def get_students():
    cursor.execute("select * from student")
    rows = cursor.fetchall()
    for row in rows:
        print("row = ", row)


create_tables()
insert_into_student()
update_student()
get_students()
