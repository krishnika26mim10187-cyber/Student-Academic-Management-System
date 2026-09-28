
from student import Student
from marks import Marks
from attendance import Attendance
from reports import Report


def main():
    print("================================")
    print(" STUDENT ACADEMIC MANAGEMENT")
    print("================================")

    student = Student(
        "101",
        "Test Student",
        "Artificial Intelligence",
        1,
        "test@gmail.com"
    )

    marks = Marks(85, 78, 82, 90)

    attendance = Attendance(100, 85)

    report = Report(student, marks, attendance)

    report.generate_report()


if __name__ == "__main__":
    main()
