"""List examples."""

numbers = [10, 20, 30, 40]

print("Original:", numbers)
print("First item:", numbers[0])
print("Last item:", numbers[-1])

numbers.append(50)
numbers.insert(1, 15)
numbers.remove(30)

print("After changes:", numbers)
print("Length:", len(numbers))
print("Slice:", numbers[1:4])

numbers.sort()
print("Sorted:", numbers)

total = sum(numbers)
print("Total:", total)

