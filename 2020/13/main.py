import argparse
from math import gcd
from typing import List

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

earliest_ts = int(input_data[0])
numbered_buses = [
    int(bus_id) for bus_id in input_data[1].split(',') if bus_id != 'x'
]

debug(f'{earliest_ts}: {numbered_buses}')

earliest_bus = 0
least_wait_time = 99999999999
for bus in numbered_buses:
    wait_time = bus - (earliest_ts % bus)
    debug(f'{bus}: {wait_time}')
    if wait_time < least_wait_time:
        earliest_bus = bus
        least_wait_time = wait_time

print(f'Part 1: {earliest_bus * least_wait_time}')

all_buses = [
    (index, int(bus_id))
    for index, bus_id in enumerate(input_data[1].split(','))
    if bus_id != 'x'
]


def lcm(a, b):
    return abs(a * b) // gcd(a, b)


debug(all_buses)
debug(gcd(13, 7))
debug(lcm(13, 7))
