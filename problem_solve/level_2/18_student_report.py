"""Problem: Generate a student report."""

# Problem:
# Store student data and print a simple report.


class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def average(self):
        return sum(self.marks) / len(self.marks)

    def grade(self):
        avg = self.average()
        if avg >= 80:
            return "A+"
        if avg >= 70:
            return "A"
        if avg >= 60:
            return "B"
        return "C"

    def report(self):
        return f"{self.name}: Avg={self.average():.2f}, Grade={self.grade()}"


# Solution:
students = [
    Student("Moshiur", [88, 76, 91]),
    Student("Nadia", [72, 69, 75]),
]

for student in students:
    print(student.report())

# Logic:
# 1. Put marks inside a class.
# 2. Calculate average and grade.
# 3. Print a readable report.

# Explanation:
# This is a small real-world use of OOP and lists together.
