import argparse
from typing import List

parser = argparse.ArgumentParser(description='Run an Advent of Code program')
parser.add_argument(
    'input_file', type=str, help='the file containing input data'
)
args = parser.parse_args()

input_data: List = []
with open(args.input_file) as f:
    input_data = [line for line in f.read().splitlines()]

row_count = 128
col_count = 8


def split_space(space, half):
    middle = int(space[0] + ((space[1] - space[0]) / 2))
    if half == 'first':
        return [space[0], middle]
    else:
        return [middle, space[1]]


def parse_seats(input_data):
    seats = []
    for boarding_pass in input_data:
        row_data = boarding_pass[:7]
        col_data = boarding_pass[7:]

        row_space = [0, row_count]
        for char in row_data:
            row_space = split_space(
                row_space, 'first' if char == 'F' else 'second'
            )
        row = row_space[0]

        col_space = [0, col_count]
        for char in col_data:
            col_space = split_space(
                col_space, 'first' if char == 'L' else 'second'
            )
        col = col_space[0]

        seat_id = row * 8 + col

        seats.append((boarding_pass, row, col, seat_id))

    return seats


seats = parse_seats(input_data)

max_seat_id = max([seat[3] for seat in seats])
print(f'Part 1: {max_seat_id}')

seats.sort(key=lambda x: x[3])
previous_seat = None
for seat in seats:
    if previous_seat and seat[3] - previous_seat[3] > 1:
        print(f'Part 2: {previous_seat[3] + 1}')
        break
    else:
        previous_seat = seat
