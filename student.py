
class Student:
    def __init__(self, student_id, name, course, semester, email):
        self.student_id = student_id
        self.name = name
        self.course = course
        self.semester = semester
        self.email = email

    def display_student(self):
        print("\n--- Student Details ---")
        print("Student ID:", self.student_id)
        print("Name:", self.name)
        print("Course:", self.course)
        print("Semester:", self.semester)
        print("Email:", self.email)
