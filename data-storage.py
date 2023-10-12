import sqlite3

# Create a connection and cursor
conn = sqlite3.connect("college_results.db")
cursor = conn.cursor()

# Create the Student and Course tables if they don't exist
cursor.execute("CREATE TABLE IF NOT EXISTS Student (roll_number INTEGER PRIMARY KEY, name TEXT)")
cursor.execute("CREATE TABLE IF NOT EXISTS Course (student_id INTEGER, course_name TEXT, marks INTEGER)")

conn.commit()

class Student:
    def __init__(self, roll_number, name):
        self.roll_number = roll_number
        self.name = name
        self.courses = []

    def add_course(self, course_name, marks):
        self.courses.append({"course_name": course_name, "marks": marks})

    def save_to_database(self):
        cursor.execute("INSERT INTO Student (roll_number, name) VALUES (?, ?)", (self.roll_number, self.name))
        conn.commit()
        self.roll_number = cursor.lastrowid

        for course in self.courses:
            cursor.execute("INSERT INTO Course (student_id, course_name, marks) VALUES (?, ?, ?)",
                           (self.roll_number, course["course_name"], course["marks"]))
            conn.commit()

def add_student(students):
    roll_number = int(input("Enter student roll number: "))
    name = input("Enter student name: ")
    student = Student(roll_number, name)
    students.append(student)
    student.save_to_database()
    print("Student added successfully.")

def retrieve_students():
    cursor.execute("SELECT * FROM Student")
    rows = cursor.fetchall()
    students = []

    for row in rows:
        student = Student(row[0], row[1])
        cursor.execute("SELECT course_name, marks FROM Course WHERE student_id=?", (student.roll_number,))
        courses = cursor.fetchall()
        for course in courses:
            student.add_course(course[0], course[1])
        students.append(student)

    return students

# Modify other functions as needed.

if __name__ == "__main__":
    students = retrieve_students()

    while True:
        # Rest of the program remains the same.
        # Remember to commit changes to the database after adding courses.

    # Close the database connection when done
    conn.close()
