"""Mini project: simple student grade calculator."""


def get_grade(score):
    if score >= 90:
        return "A"
    if score >= 80:
        return "B"
    if score >= 70:
        return "C"
    if score >= 60:
        return "D"
    return "F"


def average(scores):
    return sum(scores) / len(scores)


students = {
    "Arafat": [80, 85, 90],
    "Nadia": [92, 95, 88],
    "Rafi": [70, 75, 72],
}

for name, scores in students.items():
    avg_score = average(scores)
    grade = get_grade(avg_score)
    print(f"{name}: average={avg_score:.2f}, grade={grade}")

