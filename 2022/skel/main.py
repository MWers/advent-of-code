import argparse
import logging
import os
from typing import List

LOGLEVEL = os.environ.get('LOGLEVEL', 'INFO').upper()
logging.basicConfig(level=LOGLEVEL)
logger = logging.getLogger(__name__)


def do_part_1(input_data: List) -> None:
    pass


def do_part_2(input_data: List) -> None:
    pass


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
        input_data = [line for line in f.read().splitlines()]
    return input_data


if __name__ == "__main__":
    main()
