"""Question: Print a hollow pyramid star pattern.

Sample for n = 5:
        *
      *   *
    *       *
  *           *
* * * * * * * * *
"""


def build_pattern(n):
    lines = []

    for row in range(1, n + 1):
        spaces = "  " * (n - row)
        values = []

        for column in range(1, 2 * row):
            if column == 1 or column == 2 * row - 1 or row == n:
                values.append("*")
            else:
                values.append(" ")

        lines.append(spaces + " ".join(values))

    return lines


def print_pattern(n):
    for line in build_pattern(n):
        print(line)


def dry_run():
    print("\nDry run for n = 3:")
    print("row = 1 -> spaces = 2, columns = 1 -> one star")
    print("row = 2 -> spaces = 1, columns = 3 -> star blank star")
    print("row = 3 -> spaces = 0, columns = 5 -> all stars")


if __name__ == "__main__":
    size = 5
    print("Hollow pyramid star pattern:")
    print_pattern(size)
    dry_run()

