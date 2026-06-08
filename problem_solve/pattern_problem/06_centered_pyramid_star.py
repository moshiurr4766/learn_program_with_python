"""Question: Print a centered pyramid star pattern.

Sample for n = 5:
        *
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *
"""


def build_pattern(n):
    lines = []

    for row in range(1, n + 1):
        spaces = "  " * (n - row)
        stars = "* " * (2 * row - 1)
        lines.append((spaces + stars).rstrip())

    return lines


def print_pattern(n):
    for line in build_pattern(n):
        print(line)


def dry_run():
    print("\nDry run for n = 3:")
    print("row = 1 -> spaces = 2, stars = 1")
    print("row = 2 -> spaces = 1, stars = 3")
    print("row = 3 -> spaces = 0, stars = 5")


if __name__ == "__main__":
    size = 5
    print("Centered pyramid star pattern:")
    print_pattern(size)
    dry_run()

