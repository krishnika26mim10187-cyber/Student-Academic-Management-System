
class Report:
    def __init__(self, student, marks, attendance):
        self.student = student
        self.marks = marks
        self.attendance = attendance

    def generate_report(self):
        total, percentage, grade = self.marks.calculate_result()
        attendance_percentage, status = self.attendance.calculate_attendance()

        print("\n==============================")
        print("       STUDENT REPORT")
        print("==============================")

        print("\n--- Student Details ---")
        print("Student ID:", self.student.student_id)
        print("Name:", self.student.name)
        print("Course:", self.student.course)
        print("Semester:", self.student.semester)
        print("Email:", self.student.email)

        print("\n--- Academic Result ---")
        print("Total:", total)
        print("Percentage:", percentage)
        print("Grade:", grade)

        print("\n--- Attendance ---")
        print("Attendance:", round(attendance_percentage, 2), "%")
        print("Status:", status)

        print("==============================")
