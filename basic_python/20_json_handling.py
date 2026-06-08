"""JSON handling."""

import json

student = {
    "name": "Moshiur",
    "age": 25,
    "skills": ["Python", "Django", "SQL"],
}

json_text = json.dumps(student, indent=2)
print("Python dictionary to JSON:")
print(json_text)

data = json.loads(json_text)
print("\nJSON back to Python:")
print(data)
print("Name:", data["name"])

