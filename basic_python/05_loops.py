"""for loops, while loops, break, and continue."""

print("For loop:")
for number in range(1, 6):
    print(number)

print("\nLoop through a list:")
fruits = ["apple", "banana", "mango"]
for fruit in fruits:
    print(fruit)

print("\nWhile loop:")
count = 1
while count <= 5:
    print(count)
    count += 1

print("\nBreak and continue:")
for number in range(1, 8):
    if number == 3:
        continue
    if number == 6:
        break
    print(number)

