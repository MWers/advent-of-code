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

instructions = [
    (instruction[0], int(instruction[1]))
    for instruction in [line.split() for line in input_data]
]


def run_part_1(instructions):
    acc = 0
    cursor = 0
    visited: Set[int] = set()
    while cursor <= len(instructions):
        op, arg = instructions[cursor]
        visited.add(cursor)

        next_cursor = cursor + 1
        if op == 'acc':
            acc += arg

        if op == 'jmp':
            next_cursor = cursor + arg

        if next_cursor in visited:
            break

        cursor = next_cursor
    return acc


print(f'Part 1: {run_part_1(instructions)}')


def run_part_2(instructions, change_index):
    """
    Run program recursively trying changes at successive nop/jmp instructions
    until program completes successfully
    """
    acc = 0
    cursor = 0
    jmp_nop_index = 0
    visited = set()
    while cursor < len(instructions):
        op, arg = instructions[cursor]
        visited.add(cursor)

        next_cursor = cursor + 1
        if op == 'acc':
            acc += arg

        if op == 'jmp':
            if jmp_nop_index == change_index:
                next_cursor = cursor + 1
            else:
                next_cursor = cursor + arg
            jmp_nop_index += 1

        if op == 'nop':
            if jmp_nop_index == change_index:
                next_cursor = cursor + arg
            else:
                next_cursor = cursor + 1
            jmp_nop_index += 1

        if next_cursor in visited:
            acc = run_part_2(instructions, change_index + 1)
            break

        cursor = next_cursor

    return acc


print(f'Part 2: {run_part_2(instructions, 0)}')
