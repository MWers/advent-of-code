import argparse
from typing import Dict, List

parser = argparse.ArgumentParser(description='Run an Advent of Code program')
parser.add_argument(
    'input_file', type=str, help='the file containing input data'
)
parser.add_argument(
    '--debug', action='store_true', help='print debug messages'
)
args = parser.parse_args()


def debug(log):
    if args.debug:
        print(log)


input_data: List = []
with open(args.input_file) as f:
    input_data = [line for line in f.read().splitlines()]

zeroes_mask = '0' * 64
ones_mask = '1' * 64
mask = 'X' * 64
memory: Dict[int, str] = {}
for line in input_data:
    instruction, value = line.split(' = ')

    if 'mask' == instruction:
        mask = value
        zeroes_mask = value.replace('X', '0')
        ones_mask = value.replace('X', '1')
        print(f'{value} {zeroes_mask} {ones_mask}')

    if 'mem' in instruction:
        address = int(instruction.replace('mem[', '').replace(']', ''))
        value = value.zfill(36)
        value_list = list(value)
        for idx, char in enumerate(mask):
            if char in ['0', '1']:
                value_list[idx] = char
        memory[address] = int(''.join(value_list), 2)

print(memory)

        # masked_value = str(int(value, 2) | int(zeroes_mask, 2))
        # print(f'{masked_value}\t{value}')
        # print(f'{int(masked_value)}')

        # masked_value = str(int(masked_value, 10) & int(ones_mask, 2))
        # # print(f'{instruction}\t{value}\t{masked_value}')
        # print(f'{masked_value}\t{value}\t{zeroes_mask}')
        # # if address in memory:



