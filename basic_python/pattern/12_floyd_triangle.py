"""Question: Print Floyd's triangle.

Sample for n = 5:
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
"""


def build_pattern(n):
    lines = []
    number = 1

    for row in range(1, n + 1):
        values = []
        for column in range(1, row + 1):
            values.append(str(number))
            number += 1
        lines.append(" ".join(values))

    return lines


def print_pattern(n):
    for line in build_pattern(n):
        print(line)


def dry_run():
    print("\nDry run for n = 3:")
    print("start number = 1")
    print("row = 1 -> print 1")
    print("row = 2 -> print 2 3")
    print("row = 3 -> print 4 5 6")


if __name__ == "__main__":
    size = 5
    print("Floyd triangle:")
    print_pattern(size)
    dry_run()

