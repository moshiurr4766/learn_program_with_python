"""Question: Print a hollow diamond star pattern.

Sample for n = 5:
        *
      *   *
    *       *
  *           *
*               *
  *           *
    *       *
      *   *
        *
"""


def make_line(n, row):
    outer_spaces = "  " * (n - row)

    if row == 1:
        return outer_spaces + "*"

    inner_spaces = "  " * (2 * row - 3)
    return outer_spaces + "*" + inner_spaces + " *"


def build_pattern(n):
    lines = []

    for row in range(1, n + 1):
        lines.append(make_line(n, row))

    for row in range(n - 1, 0, -1):
        lines.append(make_line(n, row))

    return lines


def print_pattern(n):
    for line in build_pattern(n):
        print(line)


def dry_run():
    print("\nDry run for n = 3:")
    print("row = 1 -> one star")
    print("row = 2 -> outer spaces = 1, inner spaces = 1")
    print("row = 3 -> outer spaces = 0, inner spaces = 3")
    print("then repeat rows 2 and 1 for the lower half")


if __name__ == "__main__":
    size = 5
    print("Hollow diamond star pattern:")
    print_pattern(size)
    dry_run()

