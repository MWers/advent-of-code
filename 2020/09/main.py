import argparse
from typing import List

parser = argparse.ArgumentParser(description='Run an Advent of Code program')
parser.add_argument(
    'input_file', type=str, help='the file containing input data'
)
args = parser.parse_args()

input_data: List = []
with open(args.input_file) as f:
    input_data = [int(line) for line in f.read().splitlines()]

preamble_size = 5 if 'sample' in args.input_file else 25


def preamble_contains_target(target, preamble):
    for addend_1 in preamble:
        addend_2 = target - addend_1
        if addend_2 != addend_1 and addend_2 in preamble:
            return True

    return False


encryption_weakness_sum = 0
for index, number in enumerate(input_data[preamble_size:]):
    if not preamble_contains_target(
        number, input_data[index : index + preamble_size]
    ):
        encryption_weakness_sum = number
        break


print(f'Part 1: {encryption_weakness_sum}')

running_total = 0
running_addends = []
for outer_cursor in range(len(input_data)):
    inner_cursor = outer_cursor
    found_addends = False
    while running_total < encryption_weakness_sum:
        addend = input_data[inner_cursor]

        running_total += addend
        running_addends.append(addend)

        if running_total == encryption_weakness_sum:
            found_addends = True
            break

        inner_cursor += 1

    if found_addends:
        print(f'Part 2: {min(running_addends) + max(running_addends)}')
        break

    running_total = 0
    running_addends = []
