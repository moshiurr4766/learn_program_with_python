"""Question: Print a palindrome number pyramid.

Sample for n = 5:
        1
      1 2 1
    1 2 3 2 1
  1 2 3 4 3 2 1
1 2 3 4 5 4 3 2 1
"""


def build_pattern(n):
    lines = []

    for row in range(1, n + 1):
        spaces = "  " * (n - row)
        increasing = [str(number) for number in range(1, row + 1)]
        decreasing = [str(number) for number in range(row - 1, 0, -1)]
        lines.append(spaces + " ".join(increasing + decreasing))

    return lines


def print_pattern(n):
    for line in build_pattern(n):
        print(line)


def dry_run():
    print("\nDry run for n = 3:")
    print("row = 1 -> spaces = 2 -> 1")
    print("row = 2 -> spaces = 1 -> 1 2 1")
    print("row = 3 -> spaces = 0 -> 1 2 3 2 1")


if __name__ == "__main__":
    size = 5
    print("Palindrome number pyramid:")
    print_pattern(size)
    dry_run()

