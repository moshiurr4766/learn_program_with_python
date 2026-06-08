"""Tuple and set examples."""

# Tuple: ordered and cannot be changed.
point = (10, 20)
print("Tuple:", point)
print("X:", point[0])
print("Y:", point[1])

# Set: unique values, unordered.
skills = {"Python", "Django", "Python", "SQL"}
print("\nSet:", skills)

skills.add("Git")
skills.remove("SQL")
print("Updated set:", skills)

frontend = {"HTML", "CSS", "JavaScript"}
backend = {"Python", "Django", "SQL"}

print("Union:", frontend | backend)
print("Common:", frontend & backend)
print("Backend only:", backend - frontend)

