"""Question: Print an inverted right triangle star pattern.

Sample for n = 5:
* * * * *
* * * *
* * *
* *
*
"""


def build_pattern(n):
    lines = []

    for row in range(n, 0, -1):
        line = "* " * row
        lines.append(line.rstrip())

    return lines


def print_pattern(n):
    for line in build_pattern(n):
        print(line)


def dry_run():
    print("\nDry run for n = 4:")
    print("row value = 4 -> 4 stars")
    print("row value = 3 -> 3 stars")
    print("row value = 2 -> 2 stars")
    print("row value = 1 -> 1 star")


if __name__ == "__main__":
    size = 5
    print("Inverted right triangle star pattern:")
    print_pattern(size)
    dry_run()

