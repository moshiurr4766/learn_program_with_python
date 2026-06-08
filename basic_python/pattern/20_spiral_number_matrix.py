"""Question: Print a spiral number matrix.

Sample for n = 5:
 1  2  3  4  5
16 17 18 19  6
15 24 25 20  7
14 23 22 21  8
13 12 11 10  9
"""


def build_matrix(n):
    matrix = [[0 for column in range(n)] for row in range(n)]

    top = 0
    bottom = n - 1
    left = 0
    right = n - 1
    number = 1

    while top <= bottom and left <= right:
        for column in range(left, right + 1):
            matrix[top][column] = number
            number += 1
        top += 1

        for row in range(top, bottom + 1):
            matrix[row][right] = number
            number += 1
        right -= 1

        if top <= bottom:
            for column in range(right, left - 1, -1):
                matrix[bottom][column] = number
                number += 1
            bottom -= 1

        if left <= right:
            for row in range(bottom, top - 1, -1):
                matrix[row][left] = number
                number += 1
            left += 1

    return matrix


def build_pattern(n):
    matrix = build_matrix(n)
    width = len(str(n * n))
    lines = []

    for row in matrix:
        values = [str(number).rjust(width) for number in row]
        lines.append(" ".join(values))

    return lines


def print_pattern(n):
    for line in build_pattern(n):
        print(line)


def dry_run():
    print("\nDry run for n = 3:")
    print("Fill top row left to right -> 1 2 3")
    print("Fill right column top to bottom -> 4 5")
    print("Fill bottom row right to left -> 6 7")
    print("Fill left column bottom to top -> 8")
    print("Fill center -> 9")


if __name__ == "__main__":
    size = 5
    print("Spiral number matrix:")
    print_pattern(size)
    dry_run()

