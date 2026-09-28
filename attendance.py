
class Attendance:
    def __init__(self, total_classes, attended_classes):
        self.total_classes = total_classes
        self.attended_classes = attended_classes

    def calculate_attendance(self):
        if self.total_classes <= 0:
            return 0, "Invalid"

        if self.attended_classes < 0 or self.attended_classes > self.total_classes:
            return 0, "Invalid"

        percentage = (self.attended_classes / self.total_classes) * 100

        if percentage >= 75:
            status = "Eligible"
        else:
            status = "Not Eligible"

        return percentage, status
