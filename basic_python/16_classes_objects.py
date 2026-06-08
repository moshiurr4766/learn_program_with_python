"""Classes and objects."""


class Student:
    def __init__(self, name, course):
        self.name = name
        self.course = course

    def introduce(self):
        return f"My name is {self.name}. I am learning {self.course}."


student_one = Student("Moshiur", "Python")
student_two = Student("Nadia", "Django")

print(student_one.introduce())
print(student_two.introduce())

