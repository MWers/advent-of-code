import argparse
from typing import List

parser = argparse.ArgumentParser(description='Run an Advent of Code program')
parser.add_argument(
    'input_file', type=str, help='the file containing input data'
)
args = parser.parse_args()

input_data: List = []
with open(args.input_file) as f:
    input_data = [int(line) for line in f.readlines()]

# Iterate over two-digit permutations until sum is 2020
for num, entry_1 in enumerate(input_data):
    for entry_2 in input_data[num + 1 :]:
        if entry_1 + entry_2 == 2020:
            product = entry_1 * entry_2
            print(f'Part 1: {entry_1} * {entry_2} = {product}')
            break

# Iterate over three-digit permutations until sum is 2020
for num_1, entry_1 in enumerate(input_data):
    for num_2, entry_2 in enumerate(input_data[num_1 + 1 :]):
        for entry_3 in input_data[num_1 + num_2 + 2 :]:
            if entry_1 + entry_2 + entry_3 == 2020:
                product = entry_1 * entry_2 * entry_3
                print(f'Part 2: {entry_1} * {entry_2} * {entry_3} = {product}')
                break
