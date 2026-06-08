"""Simple project: student grade manager."""


class Student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll
        self.marks = []

    def add_mark(self, mark):
        if mark < 0 or mark > 100:
            return "Mark must be between 0 and 100."

        self.marks.append(mark)
        return f"Added mark {mark} for {self.name}."

    def average(self):
        if not self.marks:
            return 0

        return sum(self.marks) / len(self.marks)

    def grade(self):
        average_mark = self.average()

        if average_mark >= 80:
            return "A+"
        if average_mark >= 70:
            return "A"
        if average_mark >= 60:
            return "B"
        if average_mark >= 50:
            return "C"

        return "F"

    def report(self):
        return (
            f"Name: {self.name}, Roll: {self.roll}, "
            f"Average: {self.average():.2f}, Grade: {self.grade()}"
        )


class GradeManager:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def show_reports(self):
        for student in self.students:
            print(student.report())


manager = GradeManager()

student_one = Student("Moshiur", 101)
student_two = Student("Nadia", 102)

student_one.add_mark(85)
student_one.add_mark(90)
student_one.add_mark(78)

student_two.add_mark(65)
student_two.add_mark(72)
student_two.add_mark(69)

manager.add_student(student_one)
manager.add_student(student_two)

manager.show_reports()
