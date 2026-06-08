"""Question: Print a square star pattern.

Sample for n = 5:
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
"""


def build_pattern(n):
    lines = []

    for row in range(1, n + 1):
        line = "* " * n
        lines.append(line.rstrip())

    return lines


def print_pattern(n):
    for line in build_pattern(n):
        print(line)


def dry_run():
    print("\nDry run for n = 3:")
    print("row = 1 -> print 3 stars -> * * *")
    print("row = 2 -> print 3 stars -> * * *")
    print("row = 3 -> print 3 stars -> * * *")


if __name__ == "__main__":
    size = 5
    print("Square star pattern:")
    print_pattern(size)
    dry_run()

