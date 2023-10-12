class Student:
    def __init__(self, roll_number, name):
        self.roll_number = roll_number
        self.name = name
        self.courses = []

    def add_course(self, course_name, marks):
        self.courses.append({"course_name": course_name, "marks": marks})


def add_student(students):
    roll_number = int(input("Enter student roll number: "))
    name = input("Enter student name: ")
    student = Student(roll_number, name)
    students.append(student)
    print("Student added successfully.")


def add_course_for_student(students):
    roll_number = int(input("Enter student roll number: "))
    student = next((s for s in students if s.roll_number == roll_number), None)

    if student:
        course_name = input("Enter course name: ")
        marks = int(input("Enter marks: ")
        student.add_course(course_name, marks)
        print("Course added for the student.")
    else:
        print("Student not found.")


def calculate_results(students):
    print("Student Results:")
    for student in students:
        print(f"Roll Number: {student.roll_number}, Name: {student.name}")
        for course in student.courses:
            print(f"Course: {course['course_name']}, Marks: {course['marks']}")
        total_marks = sum(course['marks'] for course in student.courses)
        average_marks = total_marks / len(student.courses)
        print(f"Total Marks: {total_marks}")
        print(f"Average Marks: {average_marks}\n")


if __name__ == "__main__":
    students = []

    while True:
        print("College Result Management System")
        print("1. Add Student")
        print("2. Add Course for Student")
        print("3. Calculate Results")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_student(students)
        elif choice == "2":
            add_course_for_student(students)
        elif choice == "3":
            calculate_results(students)
        elif choice == "4":
            break
        else:
            print("Invalid choice. Try again.")
