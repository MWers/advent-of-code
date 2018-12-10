from __future__ import print_function
import copy
import re

# input_file = 'input-sample.txt'
input_file = 'input-full.txt'

input_re = re.compile('position=<(?P<x>[- ]*\d+), (?P<y>[- ]*\d+)> velocity=<(?P<vx>[- ]*\d+), (?P<vy>[- ]*\d+)>')

input = []
with open(input_file, 'r') as f:
    raw_input = [i.rstrip() for i in f]

    # Parse inputs
    for line in raw_input:
        input_rs = input_re.match(line)
        x = int(input_rs.group('x'))
        y = int(input_rs.group('y'))
        vx = int(input_rs.group('vx'))
        vy = int(input_rs.group('vy'))
        input.append({
            'x': x,
            'y': y,
            'vx': vx,
            'vy': vy
        })

points = []
for second in range(10700):
    # Calculate movement
    if second == 0:
        points = copy.deepcopy(input)
    else:
        for pos, point in enumerate(points):
            new_point = {
                'x': point['x'] + point['vx'],
                'y': point['y'] + point['vy'],
                'vx': point['vx'],
                'vy': point['vy']
            }
            points[pos] = new_point

    # Get bounds
    x_seq = [item['x'] for item in points]
    y_seq = [item['y'] for item in points]

    # Eliminate noise, only print if bounds < 100
    # This is an arbitrary amount
    if (max(y_seq) - min(y_seq) < 100
            and max(x_seq) - min(x_seq) < 100):

        # Set lookup dict
        positions = {}
        for item in points:
            key = '{}x{}'.format(item['x'], item['y'])
            positions[key] = '#'

        print('{} seconds'.format(second))
        for i in range(min(y_seq), max(y_seq) + 1):
            for j in range(min(x_seq), max(x_seq) + 1):
                key = '{}x{}'.format(j, i)
                if key in positions:
                    print('#', end='')
                else:
                    print('.', end='')
            print('')

        print('')
