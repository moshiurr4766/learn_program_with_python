"""Question: Print a diamond star pattern.

Sample for n = 5:
        *
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *
  * * * * * * *
    * * * * *
      * * *
        *
"""


def build_pattern(n):
    lines = []

    for row in range(1, n + 1):
        spaces = "  " * (n - row)
        stars = "* " * (2 * row - 1)
        lines.append((spaces + stars).rstrip())

    for row in range(n - 1, 0, -1):
        spaces = "  " * (n - row)
        stars = "* " * (2 * row - 1)
        lines.append((spaces + stars).rstrip())

    return lines


def print_pattern(n):
    for line in build_pattern(n):
        print(line)


def dry_run():
    print("\nDry run for n = 3:")
    print("Upper half -> stars: 1, 3, 5")
    print("Lower half -> stars: 3, 1")
    print("Total rows = 2 * n - 1 = 5")


if __name__ == "__main__":
    size = 5
    print("Diamond star pattern:")
    print_pattern(size)
    dry_run()

