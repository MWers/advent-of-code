import argparse
from functools import reduce
import operator
from typing import List

parser = argparse.ArgumentParser(description='Run an Advent of Code program')
parser.add_argument(
    'input_file', type=str, help='the file containing input data'
)
args = parser.parse_args()

input_data: List = []
with open(args.input_file) as f:
    input_data = [line for line in f.read().splitlines()]


def get_tree_count(delta, grid):
    (dx, dy) = delta
    pos = 0
    tree_count = 0
    for line_num, line in enumerate(grid):
        # Skip dy lines
        if line_num % dy != 0:
            continue
        tree_count += 1 if line[pos % len(line)] == '#' else 0
        pos += dx

    return tree_count


print(f'Part 1: {get_tree_count((3, 1), input_data)}')

product = reduce(
    operator.mul,
    [
        get_tree_count(slope, input_data)
        for slope in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    ],
)

print(f'Part 2: {product}')
