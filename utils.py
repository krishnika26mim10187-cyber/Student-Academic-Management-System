
def get_valid_marks(subject):
    while True:
        try:
            marks = float(input(f"Enter marks for {subject}: "))

            if 0 <= marks <= 100:
                return marks

            print("Marks must be between 0 and 100.")

        except ValueError:
            print("Please enter a valid number.")


def get_valid_attendance():
    while True:
        try:
            total = int(input("Enter total classes: "))
            attended = int(input("Enter attended classes: "))

            if total <= 0:
                print("Total classes must be greater than 0.")
                continue

            if attended < 0 or attended > total:
                print("Attended classes must be between 0 and total classes.")
                continue

            return total, attended

        except ValueError:
            print("Please enter valid numbers.")
