"""Input and output examples."""

# input() always returns text.
name = input("Enter your name: ")
age_text = input("Enter your age: ")

age = int(age_text)

print("Hello,", name)
print(f"Next year you will be {age + 1} years old.")

