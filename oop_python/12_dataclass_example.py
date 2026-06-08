"""Dataclass example."""

from dataclasses import dataclass


@dataclass
class Student:
    # dataclass creates __init__, __repr__, and comparison helpers.
    name: str
    department: str
    cgpa: float

    def is_passed(self):
        return self.cgpa >= 2.0


student = Student("Moshiur", "CSE", 3.75)

print(student)
print(student.is_passed())
