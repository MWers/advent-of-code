import argparse
from typing import List, Set

parser = argparse.ArgumentParser(description='Run an Advent of Code program')
parser.add_argument(
    'input_file', type=str, help='the file containing input data'
)
args = parser.parse_args()

input_data: List = []
with open(args.input_file) as f:
    input_data = [line for line in f.read().splitlines()]

letters: Set[str] = set()
groups_of_letters = []
for line in input_data:
    # New record?
    if line == '' and letters:
        groups_of_letters.append(letters)
        letters = set()

    for letter in line:
        letters.add(letter)

groups_of_letters.append(letters)

letter_count = sum([len(x) for x in groups_of_letters])
print(f'Part 1: {letter_count}')

letters = set()
groups_of_people = []
people: List[Set[str]] = []
for line in input_data:
    # New record?
    if line == '' and people:
        groups_of_people.append(people)
        letters = set()
        people = []
        continue

    people.append(set([letter for letter in line]))

groups_of_people.append(people)

letter_count = sum(
    [len(x) for x in [set.intersection(*group) for group in groups_of_people]]
)
print(f'Part 2: {letter_count}')
