"""String examples."""

message = "python programming"

print("Original:", message)
print("Uppercase:", message.upper())
print("Title case:", message.title())
print("Starts with python:", message.startswith("python"))
print("Replace:", message.replace("python", "Python"))
print("Length:", len(message))

name = "Moshiur"
language = "Python"

print(f"{name} is learning {language}.")

words = message.split()
print("Words:", words)
print("Joined:", "-".join(words))

text = "   extra space   "
print("Stripped:", text.strip())

