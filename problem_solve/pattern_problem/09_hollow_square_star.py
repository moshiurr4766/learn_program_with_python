"""Question: Print a hollow square star pattern.

Sample for n = 5:
* * * * *
*       *
*       *
*       *
* * * * *
"""


def build_pattern(n):
    lines = []

    for row in range(1, n + 1):
        columns = []
        for column in range(1, n + 1):
            if row == 1 or row == n or column == 1 or column == n:
                columns.append("*")
            else:
                columns.append(" ")
        lines.append(" ".join(columns))

    return lines


def print_pattern(n):
    for line in build_pattern(n):
        print(line)


def dry_run():
    print("\nDry run for n = 4:")
    print("row = 1 -> border row -> print all stars")
    print("row = 2 -> first and last columns are stars")
    print("row = 3 -> first and last columns are stars")
    print("row = 4 -> border row -> print all stars")


if __name__ == "__main__":
    size = 5
    print("Hollow square star pattern:")
    print_pattern(size)
    dry_run()

