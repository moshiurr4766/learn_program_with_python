"""Problem: Calculate student grade."""

# Problem:
# Find average and grade from marks.

marks = [88, 76, 91, 69]

# Solution:
total = sum(marks)
average = total / len(marks)

if average >= 80:
    grade = "A+"
elif average >= 70:
    grade = "A"
elif average >= 60:
    grade = "B"
elif average >= 50:
    grade = "C"
else:
    grade = "F"

print("Average:", round(average, 2))
print("Grade:", grade)

# Logic:
# 1. Add all marks.
# 2. Divide by number of subjects.
# 3. Compare average with grade ranges.

# Explanation:
# This combines arithmetic and decision making.
