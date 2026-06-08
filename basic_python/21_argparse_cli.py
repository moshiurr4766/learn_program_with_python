"""Simple command-line argument example.

Run:
    python3 21_argparse_cli.py Moshiur --age 25
"""

import argparse


parser = argparse.ArgumentParser(description="Greet a user.")
parser.add_argument("name", help="User name")
parser.add_argument("--age", type=int, default=None, help="User age")

args = parser.parse_args()

print(f"Hello, {args.name}!")

if args.age is not None:
    print(f"You are {args.age} years old.")

