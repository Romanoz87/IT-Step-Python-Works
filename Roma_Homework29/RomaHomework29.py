import mysql.connector


db_connector = mysql.connector.connect(
    host = "127.0.0.1",
    user = "romanoz",
    password = "Step123456",
    database = "lesson23_25"
)


db_cursor = db_connector.cursor()

create_table = """
CREATE TABLE IF NOT EXISTS students(
  studentID INT PRIMARY KEY AUTO_INCREMENT,
  studentFirstName VARCHAR(50) NOT NULL,
  studentLastName VARCHAR(50) NOT NULL,
  studentAge INT NOT NULL
);
"""

db_cursor.execute(create_table)


students = [
    ['შალიკაშვილი', 'ანდრო', 29],
    ['აბულაძე', 'გრიგოლ', 33],
    ['კახიძე', 'კოტე', 27],
    ['გერგაული', 'ანა', 25],
    ['კახიძე', 'ქეთევან', 26],
    ['ხარაზიშვილი', 'ნინო', 24],
]

insert_students = "INSERT INTO students (studentLastName, studentFirstName, studentAge) VALUES (%s, %s, %s);"

for student in students:
    db_cursor.execute(insert_students, (student[0], student[1], student[2]))
    
db_connector.commit()


student = ['არაბული', 'მაია', 19]
insert_student = "INSERT  INTO students (studentLastName, studentFirstName, studentAge)  VALUES  (%s, %s, %s);"
db_cursor.execute(insert_student, student)

db_connector.commit()


sort = "SELECT * FROM students ORDER BY studentLastName;"

db_cursor.execute(sort)


sorted_students = db_cursor.fetchall()
for student in sorted_students:
    print(student)