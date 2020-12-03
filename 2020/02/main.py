import argparse
import re
from typing import List

parser = argparse.ArgumentParser(description='Run an Advent of Code program')
parser.add_argument(
    'input_file', type=str, help='the file containing input data'
)
args = parser.parse_args()

input_data: List = []
with open(args.input_file) as f:
    for line in f.readlines():
        m = re.match(r"([0-9]+)-([0-9]+) ([a-zA-Z]): ([a-zA-Z]+)", line)
        input_data.append(
            (
                int(m.group(1)),  # type: ignore
                int(m.group(2)),  # type: ignore
                m.group(3),  # type: ignore
                m.group(4),  # type: ignore
            )
        )

# Part 1
good_passwords = 0
for (lower_bound, upper_bound, letter, password) in input_data:
    occurrences = password.count(letter)
    if int(lower_bound) <= occurrences <= int(upper_bound):
        good_passwords += 1

print(f'Part 1 - Good Passwords: {good_passwords}')

# Part 2
good_passwords = 0
for (lower_index, upper_index, letter, password) in input_data:
    # Use XOR (`^`) to get one and only one
    if (password[lower_index - 1] == letter) ^ (
        password[upper_index - 1] == letter
    ):
        good_passwords += 1

print(f'Part 2 - Good Passwords: {good_passwords}')
