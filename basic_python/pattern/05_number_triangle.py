"""Question: Print a number triangle.

Sample for n = 5:
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
"""


def build_pattern(n):
    lines = []

    for row in range(1, n + 1):
        numbers = []
        for column in range(1, row + 1):
            numbers.append(str(column))
        lines.append(" ".join(numbers))

    return lines


def print_pattern(n):
    for line in build_pattern(n):
        print(line)


def dry_run():
    print("\nDry run for n = 3:")
    print("row = 1 -> columns 1 to 1 -> 1")
    print("row = 2 -> columns 1 to 2 -> 1 2")
    print("row = 3 -> columns 1 to 3 -> 1 2 3")


if __name__ == "__main__":
    size = 5
    print("Number triangle:")
    print_pattern(size)
    dry_run()

