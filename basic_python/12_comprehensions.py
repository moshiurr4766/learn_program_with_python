"""List and dictionary comprehensions."""

numbers = [1, 2, 3, 4, 5]

squares = [number * number for number in numbers]
even_numbers = [number for number in numbers if number % 2 == 0]

print("Numbers:", numbers)
print("Squares:", squares)
print("Even numbers:", even_numbers)

names = ["arafat", "nadia", "rafi"]
title_names = [name.title() for name in names]
print("Title names:", title_names)

score_by_name = {name: len(name) for name in names}
print("Dictionary comprehension:", score_by_name)

