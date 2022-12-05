import argparse
import logging
import os
from typing import List

LOGLEVEL = os.environ.get('LOGLEVEL', 'INFO').upper()
logging.basicConfig(level=LOGLEVEL)
logger = logging.getLogger(__name__)
ROCK = ['A', 'X']
PAPER = ['B', 'Y']
SCISSORS = ['C', 'Z']

LOSE = 'X'
DRAW = 'Y'
WIN = 'Z'


def get_round_score(opponent_move, your_move):
    total = 0

    # Add your move score
    total += (
        1
        if your_move in ROCK
        else 2
        if your_move in PAPER
        else 3
        if your_move in SCISSORS
        else 0
    )

    # Add victory score
    round_outcome = get_round_outcome(opponent_move, your_move)
    total += (
        0 if round_outcome == 'lose' else 3 if round_outcome == 'draw' else 6
    )

    return total


def get_round_outcome(opponent_move, your_move):
    return (
        'win'
        if (opponent_move in ROCK and your_move in PAPER)
        or (opponent_move in PAPER and your_move in SCISSORS)
        or (opponent_move in SCISSORS and your_move in ROCK)
        else 'lose'
        if (your_move in ROCK and opponent_move in PAPER)
        or (your_move in PAPER and opponent_move in SCISSORS)
        or (your_move in SCISSORS and opponent_move in ROCK)
        else 'draw'
    )


def get_move_needed_for_outcome(opponent_move, outcome):
    if outcome is DRAW:
        return opponent_move
    elif outcome is WIN:
        return (
            ROCK[0]
            if opponent_move in SCISSORS
            else SCISSORS[0]
            if opponent_move in PAPER
            else PAPER[0]
        )
    else:
        return (
            ROCK[0]
            if opponent_move in PAPER
            else SCISSORS[0]
            if opponent_move in ROCK
            else PAPER[0]
        )


def do_part_1(input_data: List) -> None:
    total_score = 0
    for moves in input_data:
        [opponent_move, your_move] = moves.split()
        total_score += get_round_score(opponent_move, your_move)
    logger.info(f"Part 1: {total_score}")


def do_part_2(input_data: List) -> None:
    total_score = 0
    for moves in input_data:
        [opponent_move, outcome] = moves.split()
        your_move = get_move_needed_for_outcome(opponent_move, outcome)
        total_score += get_round_score(opponent_move, your_move)
    logger.info(f"Part 2: {total_score}")


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
