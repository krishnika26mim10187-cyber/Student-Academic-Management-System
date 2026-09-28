
class Marks:

    def __init__(self, python, calculus, english, evs):
        self.python = python
        self.calculus = calculus
        self.english = english
        self.evs = evs

    def calculate_result(self):
        total = self.python + self.calculus + self.english + self.evs
        percentage = total / 4

        if percentage >= 90:
            grade = "A+"
        elif percentage >= 80:
            grade = "A"
        elif percentage >= 70:
            grade = "B"
        elif percentage >= 60:
            grade = "C"
        elif percentage >= 50:
            grade = "D"
        else:
            grade = "F"

        return total, percentage, grade
