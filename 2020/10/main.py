import argparse
from typing import Dict, List

parser = argparse.ArgumentParser(description='Run an Advent of Code program')
parser.add_argument(
    'input_file', type=str, help='the file containing input data'
)
args = parser.parse_args()

input_data: List = []
with open(args.input_file) as f:
    input_data = [0] + sorted([int(line) for line in f.read().splitlines()])

# Add a voltage three higher than the max
built_in_voltage = max(input_data) + 3
input_data.append(built_in_voltage)


def get_voltage_differences(input_data):
    voltage_differences: Dict[int, int] = {}
    previous_voltage = 0
    for voltage in input_data:
        delta = voltage - previous_voltage

        if delta in voltage_differences:
            voltage_differences[delta] += 1
        else:
            voltage_differences[delta] = 1

        previous_voltage = voltage

    return voltage_differences


voltage_differences = get_voltage_differences(input_data)
differences_product = voltage_differences[1] * voltage_differences[3]
print(f'Part 1: {differences_product}')


def get_adapter_tree(input_data):
    cursor = 0
    adapter_tree = {}
    for index, adapter in enumerate(input_data):
        compatible_adapters = []
        for next_adapter in input_data[index + 1 :]:
            if adapter + 3 < next_adapter:
                break
            compatible_adapters.append(next_adapter)
        adapter_tree[adapter] = compatible_adapters
    return adapter_tree


def get_path_count(node, tree):
    # print(f'{node} ', end='')
    # Are we on a leaf?
    if node in tree and not tree[node]:
        # print('')
        return 1

    return sum([get_path_count(child, tree) for child in tree[node]])


# https://stackoverflow.com/posts/35531270/revisions
def find_simple_paths(graph, start, end):
    visited = set()
    visited.add(start)

    nodestack = list()
    indexstack = list()
    current = start
    i = 0

    while True:
        # get a list of the neighbors of the current node
        neighbors = graph[current]

        # find the next unvisited neighbor of this node, if any
        while i < len(neighbors) and neighbors[i] in visited:
            i += 1

        if i >= len(neighbors):
            # we've reached the last neighbor of this node, backtrack
            visited.remove(current)
            if len(nodestack) < 1:
                break  # can't backtrack, stop!
            current = nodestack.pop()
            i = indexstack.pop()
        elif neighbors[i] == end:
            # yay, we found the target node! let the caller process the path
            yield nodestack + [current, end]
            i += 1
        else:
            # push current node and index onto stacks, switch to neighbor
            nodestack.append(current)
            indexstack.append(i + 1)
            visited.add(neighbors[i])
            current = neighbors[i]
            i = 0


adapter_tree = get_adapter_tree(input_data)
# print(adapter_tree)
path_count = len([path for path in find_simple_paths(adapter_tree, input_data[0], input_data[-1])])
print(f'Part 2: {path_count}')


# This works but it's terribly slow - O(n!)
# path_count = get_path_count(input_data[0], adapter_tree)
# print(f'Part 2: {path_count}')
