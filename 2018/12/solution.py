from __future__ import print_function
import re

input_file = 'input-full.txt'

patterns = {}
pots = ''
with open(input_file, 'r') as f:
    raw_data = [i.rstrip() for i in f]

    for line in raw_data:
        if 'initial state:' in line:
            pots = ('.' * 10) + line[15:] + ('.' * 120)
        elif '=>' in line:
            pattern, action = line.split(' => ')
            if action == '#':
                patterns[pattern] = action

# do large number of iterations, look for patterns
print('{0:>2}: {1}'.format(0, pots))
for i in range(1, 120):
    actions = set()
    for pattern in patterns.keys():
        action = patterns[pattern]
        for m in re.finditer('(?={})'.format(re.escape(pattern)), pots):
            actions.add((m.start() + 2, action))
    pots = '.' * len(pots)
    pot_idx_sum = 0
    for pos, char in actions:
        pots = pots[:pos] + char + pots[pos+1:]
        pot_idx_sum += pos - 10
    print('{0:>2}: {1} {2}'.format(i, pots, pot_idx_sum))

# after 100 generations, a pattern emerges:
#
# gen sum
# --- ----
# 100 6175
# 101 6225
# 102 6275
# 103 6325
# 104 6375
# 105 6425
# 106 6475
# 107 6525
# 108 6575
# 109 6625
# 110 6675
#
# sum = gen_nbr * 50 + 1175
part2_sum = 50000000000 * 50 + 1175
print('part 2: {}'.format(part2_sum))
