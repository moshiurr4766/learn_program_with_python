"""Constructor and self example."""


class Student:
    def __init__(self, name, age):
        # __init__ runs automatically when we create an object.
        # self means "this current object".
        self.name = name
        self.age = age

    def introduce(self):
        return f"My name is {self.name}. I am {self.age} years old."


student = Student("Moshiur", 22)

print(student.introduce())
