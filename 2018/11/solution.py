from __future__ import print_function
import operator

SERIAL = 8199

def get_power(x, y, serial):
    rack_id = x + 10
    power = rack_id * y
    power = power + serial
    power = power * rack_id
    power = int(power/100) % 10
    power = power - 5
    return power

# print(get_power(3, 5, 8))
# print(get_power(122, 79, 57))
# print(get_power(217, 196, 39))
# print(get_power(101, 153, 71))

grid = {}
for y in range(1, 301):
    for x in range(1, 301):
        grid[x, y] = get_power(x, y, SERIAL)

squares = {}
for y in range(1, 299):
    for x in range(1, 299):
        squares[x, y] = (grid[x, y] + grid[x+1, y] + grid[x+2, y]
                         + grid[x, y+1] + grid[x+1, y+1] + grid[x+2, y+1]
                         + grid[x, y+2] + grid[x+1, y+2] + grid[x+2, y+2])

max_3x3 = max(squares.iteritems(), key=operator.itemgetter(1))[0]
print('part 1: {}'.format(max_3x3))

squares = {}
for s in range(1, 300):
    for y in range(1, (300 - s)):
        for x in range(1, (300 - s)):
            square_sum = 0
            for j in range(0, s):
                for i in range(0, s):
                    square_sum += grid[x+i, y+j]
            squares[x, y, s] = square_sum

max_any = max(squares.iteritems(), key=operator.itemgetter(1))[0]
print('part 2: {}'.format(max_any))
