"""Question: Print an alphabet triangle.

Sample for n = 5:
A
A B
A B C
A B C D
A B C D E
"""


def build_pattern(n):
    lines = []

    for row in range(1, n + 1):
        letters = []
        for column in range(row):
            letters.append(chr(65 + column))
        lines.append(" ".join(letters))

    return lines


def print_pattern(n):
    for line in build_pattern(n):
        print(line)


def dry_run():
    print("\nDry run for n = 3:")
    print("row = 1 -> chr(65) -> A")
    print("row = 2 -> chr(65), chr(66) -> A B")
    print("row = 3 -> chr(65), chr(66), chr(67) -> A B C")


if __name__ == "__main__":
    size = 5
    print("Alphabet triangle:")
    print_pattern(size)
    dry_run()

