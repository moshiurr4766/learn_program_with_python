"""lambda, map, and filter examples."""

numbers = [1, 2, 3, 4, 5]

square = lambda number: number * number

print("Square of 4:", square(4))

squares = list(map(lambda number: number * number, numbers))
even_numbers = list(filter(lambda number: number % 2 == 0, numbers))

print("Numbers:", numbers)
print("Squares:", squares)
print("Even numbers:", even_numbers)

students = [
    {"name": "Arafat", "score": 85},
    {"name": "Nadia", "score": 92},
    {"name": "Rafi", "score": 78},
]

students.sort(key=lambda student: student["score"], reverse=True)
print("Sorted students:", students)

