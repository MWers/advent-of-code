import argparse
import re
from typing import Dict, List, Set

parser = argparse.ArgumentParser(description='Run an Advent of Code program')
parser.add_argument(
    'input_file', type=str, help='the file containing input data'
)
args = parser.parse_args()

input_data: List = []
with open(args.input_file) as f:
    input_data = [line for line in f.read().splitlines()]


def parse_bag(description):
    m = re.match(r"([0-9]+)? ?([a-z ]+) bags?\.?", description)
    count = int(m.group(1)) if m.group(1) else None
    color = m.group(2) if m.group(2) != 'no other' else None
    return (color, count)


def get_children(color, parents):
    children = set()
    if color in parents:
        for color in parents[color]:
            children.add(color)
            sub_children = get_children(color, parents)
            if sub_children:
                for child in sub_children:
                    children.add(child)
        return children


def get_bag_count(color, nodes):
    bag_counts = 0
    if color in nodes:
        children = nodes[color]
        for child in children:
            bag_counts += child[1]
            bag_counts += child[1] * get_bag_count(child[0], nodes)
    return bag_counts


parents: Dict[str, Set] = {}
for line in input_data:
    node_str, children_str = line.split(' contain ')
    node = parse_bag(node_str)

    children = [parse_bag(child_str) for child_str in children_str.split(', ')]
    for child in children:
        if child[0] not in parents:
            parents[child[0]] = set()
        parents[child[0]].add(node[0])


print(f'Part 1: {len(get_children("shiny gold", parents))}')

nodes = {}
for line in input_data:
    node_str, children_str = line.split(' contain ')
    node = parse_bag(node_str)

    children = [
        bag
        for bag in [
            parse_bag(child_str) for child_str in children_str.split(', ')
        ]
        if bag != (None, None)
    ]
    nodes[node[0]] = children


print(f'Part 2: {get_bag_count("shiny gold", nodes)}')
