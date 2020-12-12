from __future__ import print_function
import re

input_file = 'input-full.txt'
# input_file = 'input-sample1.txt'
# input_file = 'input-sample2.txt'
input_re = re.compile('pos=<(?P<x>[- ]?[0-9]+),(?P<y>[- ]?[0-9]+),(?P<z>[- ]?[0-9]+)>, r=(?P<radius>[0-9]+)')
# pos=<0,0,0>, r=4
all_bots = []
max_radius = -1
with open(input_file, 'r') as f:
    raw_input = [i.rstrip() for i in f]

    # Parse inputs
    for line in raw_input:
        input_rs = input_re.match(line)
        x = int(input_rs.group('x'))
        y = int(input_rs.group('y'))
        z = int(input_rs.group('z'))
        radius = int(input_rs.group('radius'))
        all_bots.append((x, y, z, radius))
        if radius > max_radius:
            strongest_bot = (x, y, z, radius)
            max_radius = radius

    # print(all_bots)

print("max radius: {}".format(strongest_bot))


def get_taxicab_dist(p1, p2):
    return abs(p2[0] - p1[0]) + abs(p2[1] - p1[1]) + abs(p2[2] - p1[2])


def get_bots_in_range(bot, all_bots):
    inrange_count = 0
    for curr_bot in all_bots:
        if get_taxicab_dist(bot, curr_bot) <= bot[3]:
            inrange_count += 1
    return inrange_count


def bot_range_overlaps(bot1, bot2):
    # if dist between bots <= sum of their ranges, they overlap
    return get_taxicab_dist(bot1, bot2) <= (bot1[3] + bot2[3])


def get_overlapping_bots(bots):
    overlapping_bots = {}
    for i, bot1 in enumerate(bots):
        for j in range(i+1, len(bots)):
            bot2 = bots[j]
            if bot_range_overlaps(bot1, bot2):
                if bot1 not in overlapping_bots:
                    overlapping_bots[bot1] = set()
                if bot2 not in overlapping_bots:
                    overlapping_bots[bot2] = set()
                overlapping_bots[bot1].add(bot2)
                overlapping_bots[bot2].add(bot1)

    return overlapping_bots


print("part 1: {} within range".format(
    get_bots_in_range(strongest_bot, all_bots)))

overlapping_bots = get_overlapping_bots(all_bots)
most_overlaps = {}
most_overlaps['bots'] = []
most_overlaps['count'] = 0
for bot in overlapping_bots.keys():
    overlaps = len(overlapping_bots[bot])
    if overlaps > most_overlaps['count']:
        most_overlaps['bots'] = [bot]
        most_overlaps['count'] = overlaps
    elif overlaps == most_overlaps['count']:
        most_overlaps['bots'].append(bot)

print(most_overlaps)

# most_in_range = -1
# most_in_range_points = []
# for z in range(min_z, max_z + 1):
#     for y in range(min_y, max_y + 1):
#         for x in range(min_x, max_x + 1):
#             in_range = get_inrange_count_by_point((x, y, z, 0), all_bots)
#             if in_range >= most_in_range:
#                 most_in_range = in_range
#                 most_in_range_points.append((x, y, z))

# nearest = {}
# nearest['dist'] = 999999999
# nearest['point'] = None
# for point in most_in_range_points:
#     dist = get_taxicab_dist(point, (0, 0, 0))
#     if dist < nearest['dist']:
#         nearest['dist'] = dist
#         nearest['point'] = point
#
# print("part 2: {} {}".format(nearest['dist'], nearest['point']))


        # if get_taxicab_dist(bot, strongest_bot) <= strongest_bot[3]:
        #     within_range += 1

# def traverse_graph(graph):
#     for node in graph:
#         if node[0] in ['at', 'literal']:
#             print(node)
#         elif node[0] in ['subpattern']:
#             print(node[1][1][0])
#         elif node[0] in ['branch']:
#             print(node[1][0][0])
#
#
# graph = re.sre_parse.parse(data[0])
# traverse_graph(graph)
