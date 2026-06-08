"""Question: Print a butterfly star pattern.

Sample for n = 5:
*                 *
* *             * *
* * *         * * *
* * * *     * * * *
* * * * * * * * * *
* * * *     * * * *
* * *         * * *
* *             * *
*                 *
"""


def build_pattern(n):
    lines = []

    for row in range(1, n + 1):
        left = "* " * row
        spaces = "  " * (2 * (n - row))
        right = "* " * row
        lines.append((left + spaces + right).rstrip())

    for row in range(n - 1, 0, -1):
        left = "* " * row
        spaces = "  " * (2 * (n - row))
        right = "* " * row
        lines.append((left + spaces + right).rstrip())

    return lines


def print_pattern(n):
    for line in build_pattern(n):
        print(line)


def dry_run():
    print("\nDry run for n = 3:")
    print("Upper half stars on each side -> 1, 2, 3")
    print("Middle spaces decrease -> 4, 2, 0 units")
    print("Lower half stars on each side -> 2, 1")


if __name__ == "__main__":
    size = 5
    print("Butterfly star pattern:")
    print_pattern(size)
    dry_run()

