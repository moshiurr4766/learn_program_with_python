"""Question: Print a right triangle star pattern.

Sample for n = 5:
*
* *
* * *
* * * *
* * * * *
"""


def build_pattern(n):
    lines = []

    for row in range(1, n + 1):
        line = "* " * row
        lines.append(line.rstrip())

    return lines


def print_pattern(n):
    for line in build_pattern(n):
        print(line)


def dry_run():
    print("\nDry run for n = 4:")
    print("row = 1 -> 1 star")
    print("row = 2 -> 2 stars")
    print("row = 3 -> 3 stars")
    print("row = 4 -> 4 stars")


if __name__ == "__main__":
    size = 5
    print("Right triangle star pattern:")
    print_pattern(size)
    dry_run()

