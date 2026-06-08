"""Question: Print a repeated number triangle.

Sample for n = 5:
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
"""


def build_pattern(n):
    lines = []

    for row in range(1, n + 1):
        values = [str(row)] * row
        lines.append(" ".join(values))

    return lines


def print_pattern(n):
    for line in build_pattern(n):
        print(line)


def dry_run():
    print("\nDry run for n = 3:")
    print("row = 1 -> print 1 one time")
    print("row = 2 -> print 2 two times")
    print("row = 3 -> print 3 three times")


if __name__ == "__main__":
    size = 5
    print("Repeated number triangle:")
    print_pattern(size)
    dry_run()

