"""Question: Print Pascal's triangle.

Sample for n = 5:
        1
      1   1
    1   2   1
  1   3   3   1
1   4   6   4   1
"""


def build_pattern(n):
    lines = []
    previous_row = []

    for row_index in range(n):
        current_row = []

        for column in range(row_index + 1):
            if column == 0 or column == row_index:
                current_row.append(1)
            else:
                current_row.append(previous_row[column - 1] + previous_row[column])

        spaces = "  " * (n - row_index - 1)
        values = "   ".join(str(number) for number in current_row)
        lines.append(spaces + values)
        previous_row = current_row

    return lines


def print_pattern(n):
    for line in build_pattern(n):
        print(line)


def dry_run():
    print("\nDry run for n = 4:")
    print("row 1 -> 1")
    print("row 2 -> 1 1")
    print("row 3 -> middle value = 1 + 1 -> 1 2 1")
    print("row 4 -> middle values = 1 + 2 and 2 + 1 -> 1 3 3 1")


if __name__ == "__main__":
    size = 5
    print("Pascal triangle:")
    print_pattern(size)
    dry_run()

