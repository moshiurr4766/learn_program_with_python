"""Class and object example."""


class Student:
    # A class is a blueprint for creating objects.
    def study(self):
        # A method is a function that belongs to a class.
        return "I am studying Python."


# An object is a real item created from a class.
student_one = Student()

print(student_one.study())
