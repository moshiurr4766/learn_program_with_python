"""Question: Print a rectangle star pattern.

Sample for rows = 4 and columns = 6:
* * * * * *
* * * * * *
* * * * * *
* * * * * *
"""


def build_pattern(rows, columns):
    lines = []

    for row in range(1, rows + 1):
        line = "* " * columns
        lines.append(line.rstrip())

    return lines


def print_pattern(rows, columns):
    for line in build_pattern(rows, columns):
        print(line)


def dry_run():
    print("\nDry run for rows = 2, columns = 4:")
    print("row = 1 -> print 4 stars -> * * * *")
    print("row = 2 -> print 4 stars -> * * * *")


if __name__ == "__main__":
    total_rows = 4
    total_columns = 6
    print("Rectangle star pattern:")
    print_pattern(total_rows, total_columns)
    dry_run()

