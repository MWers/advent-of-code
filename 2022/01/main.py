import argparse
import logging
import os
from typing import List

LOGLEVEL = os.environ.get('LOGLEVEL', 'INFO').upper()
logging.basicConfig(level=LOGLEVEL)
logger = logging.getLogger(__name__)


def get_food_calories_by_elf(input_data: List) -> List:
    food_calories_by_elf = []
    running_calorie_sum = 0
    for value in input_data:
        if value:
            running_calorie_sum += int(value)
        else:
            food_calories_by_elf.append(running_calorie_sum)
            running_calorie_sum = 0

    # Don't forget the last one
    food_calories_by_elf.append(running_calorie_sum)

    return food_calories_by_elf


def do_part_1(input_data: List) -> None:
    food_calories_by_elf = get_food_calories_by_elf(input_data)

    logger.info(f"Part 1: {max(food_calories_by_elf)}")


def do_part_2(input_data: List) -> None:
    food_calories_by_elf = get_food_calories_by_elf(input_data)

    logger.info(f"Part 1: {sum(sorted(food_calories_by_elf)[-3:])}")


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
