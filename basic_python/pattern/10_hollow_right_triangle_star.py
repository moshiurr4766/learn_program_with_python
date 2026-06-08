"""Question: Print a hollow right triangle star pattern.

Sample for n = 5:
*
* *
*   *
*     *
* * * * *
"""


def build_pattern(n):
    lines = []

    for row in range(1, n + 1):
        columns = []
        for column in range(1, row + 1):
            if column == 1 or column == row or row == n:
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
    print("row = 1 -> first edge -> *")
    print("row = 2 -> first and last column -> * *")
    print("row = 3 -> middle column is blank -> *   *")
    print("row = 4 -> last row -> all stars")


if __name__ == "__main__":
    size = 5
    print("Hollow right triangle star pattern:")
    print_pattern(size)
    dry_run()

