import argparse
import copy
from typing import List

parser = argparse.ArgumentParser(description='Run an Advent of Code program')
parser.add_argument(
    'input_file', type=str, help='the file containing input data'
)
args = parser.parse_args()

input_data: List = []
with open(args.input_file) as f:
    input_data = [line for line in f.read().splitlines()]


def grid_to_str(grid):
    return '\n'.join([''.join([char for char in line]) for line in grid])


def update_grid_for_neighbors(grid):
    new_grid = copy.deepcopy(grid)
    for y, line in enumerate(grid):
        for x, char in enumerate(line):
            if char == '.':
                new_grid[y][x] = '.'
            else:
                neighbors = get_neighbors(x, y, grid)
                if char == 'L' and '#' not in neighbors:
                    new_grid[y][x] = '#'

                if char == '#' and neighbors.count('#') >= 4:
                    new_grid[y][x] = 'L'
    return new_grid


def get_neighbors(x, y, grid):
    grid_height = len(grid)
    grid_width = len(grid[0])
    neighbors = []
    for i in range(x - 1, x + 2):
        for j in range(y - 1, y + 2):
            # print(i, j)
            if (
                0 <= i < grid_width
                and 0 <= j < grid_height
                and (i, j) != (x, y)
            ):
                neighbors += grid[j][i]
                # print(f'{i}, {j}: {grid[j][i]}')
    return neighbors


# TODO
def update_grid_for_visible(grid):
    new_grid = copy.deepcopy(grid)
    for y, line in enumerate(grid):
        for x, char in enumerate(line):
            if char == '.':
                new_grid[y][x] = '.'
            else:
                neighbors = get_neighbors(x, y, grid)
                if char == 'L' and '#' not in neighbors:
                    new_grid[y][x] = '#'

                if char == '#' and neighbors.count('#') >= 4:
                    new_grid[y][x] = 'L'
    return new_grid


# TODO
def get_visible(x, y, grid):
    grid_height = len(grid)
    grid_width = len(grid[0])
    neighbors = []
    for i in range(x - 1, x + 2):
        for j in range(y - 1, y + 2):
            # print(i, j)
            if (
                0 <= i < grid_width
                and 0 <= j < grid_height
                and (i, j) != (x, y)
            ):
                neighbors += grid[j][i]
                # print(f'{i}, {j}: {grid[j][i]}')
    return neighbors


# TODO
def get_visible_for_direction(x, y, grid, dx, dy):
    pass


# print(grid_to_str(grid))
# print()
# print(grid_to_str(update_grid_for_neighbors(grid)))

# Part 1
# Update grid until it hits equilibrium
grid = [list(line) for line in input_data]
new_grid = []
while(True):
    new_grid = update_grid_for_neighbors(grid)
    # print(grid_to_str(new_grid))
    # print()
    if grid_to_str(new_grid) == grid_to_str(grid):
        # print('The grids are the same')
        break
    grid = new_grid
occupied_seat_count = grid_to_str(new_grid).count('#')
print(f'Part 1: {occupied_seat_count}')


# Part 2
# Update grid until it hits equilibrium
grid = [list(line) for line in input_data]


# print(get_neighbors(0, 0, grid))
# print(get_neighbors(2, 2, grid))
# print(get_neighbors(9, 9, grid))
# get_neighbors(1, 0, grid)
# get_neighbors(2, 0, grid)
# get_neighbors(3, 0, grid)
# get_neighbors(0, 0, grid)
# get_neighbors(0, 1, grid)
# get_neighbors(0, 2, grid)
# get_neighbors(0, 3, grid)
# update_grid_for_neighbors(grid)
