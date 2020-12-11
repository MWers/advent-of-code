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
            if (
                0 <= i < grid_width
                and 0 <= j < grid_height
                and (i, j) != (x, y)
            ):
                neighbors += grid[j][i]
    return neighbors


def update_grid_for_visible(grid):
    new_grid = copy.deepcopy(grid)
    for y, line in enumerate(grid):
        for x, char in enumerate(line):
            neighbor_count = get_visible_count(x, y, grid)

            if char == 'L' and neighbor_count == 0:
                new_grid[y][x] = '#'

            if char == '#' and neighbor_count >= 5:
                new_grid[y][x] = 'L'
    return new_grid


def get_visible_count(x, y, grid):
    neighbor_count = 0
    for dx, dy in (
        (-1, -1),
        (0, -1),
        (1, -1),
        (-1, 0),
        (1, 0),
        (-1, 1),
        (0, 1),
        (1, 1),
    ):
        neighbor_count += (
            1 if is_seat_occupied_in_direction(x, y, grid, dx, dy) else 0
        )

    return neighbor_count


def is_seat_occupied_in_direction(x, y, grid, dx, dy):
    i = x + dx
    j = y + dy

    grid_height = len(grid)
    grid_width = len(grid[0])

    while 0 <= i < grid_width and 0 <= j < grid_height:
        if grid[j][i] == '#':
            return True
        if grid[j][i] == 'L':
            return False
        i += dx
        j += dy

    return False


# Part 1
# Update grid until it hits equilibrium
grid = [list(line) for line in input_data]
new_grid: List[List[str]] = []
while True:
    new_grid = update_grid_for_neighbors(grid)
    if grid_to_str(new_grid) == grid_to_str(grid):
        break
    grid = new_grid
occupied_seat_count = grid_to_str(new_grid).count('#')
print(f'Part 1: {occupied_seat_count}')


# Part 2
# Update grid until it hits equilibrium
grid = [list(line) for line in input_data]

while True:
    new_grid = update_grid_for_visible(grid)
    if grid_to_str(new_grid) == grid_to_str(grid):
        break
    grid = new_grid
occupied_seat_count = grid_to_str(new_grid).count('#')
print(f'Part 2: {occupied_seat_count}')
