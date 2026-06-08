"""Dictionary examples."""

student = {
    "name": "Moshiur",
    "age": 25,
    "course": "Python",
}

print("Student:", student)
print("Name:", student["name"])
print("Course:", student.get("course"))

student["age"] = 26
student["city"] = "Dhaka"

print("\nAfter update:", student)

print("\nKeys and values:")
for key, value in student.items():
    print(key, "=>", value)

students = [
    {"name": "Arafat", "score": 85},
    {"name": "Nadia", "score": 92},
    {"name": "Rafi", "score": 78},
]

for item in students:
    print(f"{item['name']} scored {item['score']}")

