from __future__ import print_function

"""
Advent of Code 2018 - Day 17

sample data:

x=495, y=2..7
y=7, x=495..501
x=501, y=3..7
x=498, y=2..4
x=506, y=1..2
x=498, y=10..13
x=504, y=10..13
y=13, x=498..504
"""

import re

input_file = 'input-sample.txt'
# input_file = 'input-full.txt'


def load_data(input_file):
    input_re = re.compile('(?P<axis1>[x|y])=(?P<num1>\d+), (?P<axis2>[x|y])=(?P<num2from>\d+)\.\.(?P<num2to>\d+)')

    min, max = {}, {}
    min['x'] = 999999999
    max['x'] = -999999999
    min['y'] = 999999999
    max['y'] = -999999999
    data = {}
    with open(input_file, 'r') as f:
        raw_data = [i.rstrip() for i in f]

        for line in raw_data:
            input_rs = input_re.match(line)
            axis1 = input_rs.group('axis1')
            num1 = int(input_rs.group('num1'))
            axis2 = input_rs.group('axis2')
            num2from = int(input_rs.group('num2from'))
            num2to = int(input_rs.group('num2to'))

            # write to data
            for idx in range(num2from, num2to + 1):
                if axis1 == 'x':
                    data_idx = (num1, idx)
                else:
                    data_idx = (idx, num1)
                data[data_idx] = '#'

            if num1 < min[axis1]:
                min[axis1] = num1
            if num1 > max[axis1]:
                max[axis1] = num1
            if num2from < min[axis2]:
                min[axis2] = num2from
            if num2to > max[axis2]:
                max[axis2] = num2to

    # x values can exceed min/max by 1
    min['x'] -= 1
    max['x'] += 1

    # set water source
    data[(500, 0)] = '+'

    return data, min, max


def print_data(data, min, max):
    for y in range(0, max['y'] + 2):
        for x in range(min['x'], max['x'] + 1):
            print(data.get((x, y), '.'), end='')

        print()


data, min, max = load_data(input_file)
print_data(data, min, max)

# TODO:
# set cursor at water source
# loop
#   for each step, update points next to cursors, creating new cursors
#   if a cursor cannot update any nearby points, remove it as a cursor
#   end when all active cursors are beyond max['y']
#   maintain count of all points changed to water
