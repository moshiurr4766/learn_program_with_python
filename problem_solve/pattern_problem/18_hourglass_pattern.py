"""Question: Print an hourglass star pattern.

Sample for n = 5:
* * * * * * * * *
  * * * * * * *
    * * * * *
      * * *
        *
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *
"""


def build_pattern(n):
    lines = []

    for row in range(n, 0, -1):
        spaces = "  " * (n - row)
        stars = "* " * (2 * row - 1)
        lines.append((spaces + stars).rstrip())

    for row in range(2, n + 1):
        spaces = "  " * (n - row)
        stars = "* " * (2 * row - 1)
        lines.append((spaces + stars).rstrip())

    return lines


def print_pattern(n):
    for line in build_pattern(n):
        print(line)


def dry_run():
    print("\nDry run for n = 3:")
    print("Top half stars -> 5, 3, 1")
    print("Bottom half stars -> 3, 5")
    print("Total rows = 2 * n - 1 = 5")


if __name__ == "__main__":
    size = 5
    print("Hourglass star pattern:")
    print_pattern(size)
    dry_run()

