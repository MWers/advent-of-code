import argparse
import logging
import os
from typing import List

LOGLEVEL = os.environ.get('LOGLEVEL', 'INFO').upper()
logging.basicConfig(level=LOGLEVEL)
logger = logging.getLogger(__name__)


def do_part_1(input_data: List) -> None:
    prev_value = None
    count = 0
    for value in input_data:
        if prev_value and value > prev_value:
            count += 1

        prev_value = value

    logger.info(f'part 1 count: {count}')


def do_part_2(input_data: List) -> None:
    prev_sum = None
    count = 0
    for index in range(len(input_data) - 2):
        current_sum = (
            input_data[index] + input_data[index + 1] + input_data[index + 2]
        )

        if prev_sum and current_sum > prev_sum:
            count += 1

        prev_sum = current_sum

    logger.info(f'part 2 count: {count}')


def main() -> None:
    input_filename = get_input_filename()
    input_data = get_input_data(input_filename)
    do_part_1(input_data)
    do_part_2(input_data)


def get_input_filename() -> str:
    parser = argparse.ArgumentParser(description='Run Advent of Code program')
    parser.add_argument(
        'input_filename', type=str, help='the file containing input data'
    )
    args = parser.parse_args()
    return args.input_filename


def get_input_data(input_filename: str) -> List:
    input_data: List = []
    with open(input_filename) as f:
        input_data = [int(line) for line in f.read().splitlines()]
    return input_data


if __name__ == "__main__":
    main()
