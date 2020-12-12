import argparse
import copy
from typing import List

parser = argparse.ArgumentParser(description='Run an Advent of Code program')
parser.add_argument(
    'input_file', type=str, help='the file containing input data'
)
parser.add_argument(
    '--debug', action='store_true', help='print debug messages'
)
args = parser.parse_args()

input_data: List = []
with open(args.input_file) as f:
    input_data = [line for line in f.read().splitlines()]

directions = ['N', 'E', 'S', 'W']

orientation = 'E'
location = [0, 0]
for line in input_data:
    action, distance = line[0], int(line[1:])

    # Move ship forward
    if action == 'F':
        action = orientation

    # Rotate ship
    if action in ['R', 'L']:
        dir_delta = int(distance / 90)
        dir_delta = -dir_delta if action == 'L' else dir_delta
        curr_index = directions.index(orientation)
        orientation = directions[(curr_index + dir_delta) % 4]

    # Move ship
    if action == 'N':
        location[1] += distance
    if action == 'S':
        location[1] += -distance
    if action == 'E':
        location[0] += distance
    if action == 'W':
        location[0] += -distance

    if args.debug:
        print(f'{action} {distance}\t{location}\t{orientation}')

print(f'Part 1: {abs(location[0]) + abs(location[1])}')

ship_loc = [0, 0]
waypoint_rel_loc = [10, 1]
for line in input_data:
    action, distance = line[0], int(line[1:])

    # Move ship in the direction of the waypoint, move waypoint also
    if action == 'F':
        ship_loc[0] = ship_loc[0] + waypoint_rel_loc[0] * distance
        ship_loc[1] = ship_loc[1] + waypoint_rel_loc[1] * distance

    # Rotate waypoint around ship
    if action in ['R', 'L']:
        prev_waypoint_loc = copy.deepcopy(waypoint_rel_loc)

        if distance == 180:
            waypoint_rel_loc[0] = -prev_waypoint_loc[0]
            waypoint_rel_loc[1] = -prev_waypoint_loc[1]

        if (action == 'R' and distance == 90) or (
            action == 'L' and distance == 270
        ):
            waypoint_rel_loc[0] = prev_waypoint_loc[1]
            waypoint_rel_loc[1] = -prev_waypoint_loc[0]

        if (action == 'R' and distance == 270) or (
            action == 'L' and distance == 90
        ):
            waypoint_rel_loc[0] = -prev_waypoint_loc[1]
            waypoint_rel_loc[1] = prev_waypoint_loc[0]

    # Move waypoint in relation to ship
    if action == 'N':
        waypoint_rel_loc[1] += distance
    if action == 'S':
        waypoint_rel_loc[1] += -distance
    if action == 'E':
        waypoint_rel_loc[0] += distance
    if action == 'W':
        waypoint_rel_loc[0] += -distance

    if args.debug:
        print(f'{action} {distance}\t{ship_loc}\t{waypoint_rel_loc}')

print(f'Part 2: {abs(ship_loc[0]) + abs(ship_loc[1])}')
