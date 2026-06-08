"""Variables and basic data types."""

name = "Moshiur"
age = 25
height = 5.8
is_student = True
nothing = None

print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Is student:", is_student)
print("Empty value:", nothing)

print("\nData types:")
print(type(name))
print(type(age))
print(type(height))
print(type(is_student))
print(type(nothing))

# Type conversion
age_text = str(age)
number_text = "100"
number = int(number_text)

print("\nConverted age:", age_text, type(age_text))
print("Converted number:", number, type(number))

