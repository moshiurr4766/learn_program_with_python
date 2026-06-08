"""if, elif, and else examples."""

score = 82

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print("Score:", score)
print("Grade:", grade)

temperature = 30

if temperature > 35:
    print("Very hot")
elif temperature >= 25:
    print("Warm")
else:
    print("Cool")

