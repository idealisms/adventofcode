import collections
import itertools
import math
import re

inp = open(re.search(r"day\d\d", __file__)[0] + 'input.txt').read().strip()
_inp = '''addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop'''

X = 1
cycle = 0
ncycle = 20
cycle_step = 40
part1 = 0
part2 = ''
for line in inp.splitlines():
    if line == 'noop':
        row_x = len(part2) % 40
        if row_x in (X - 1, X, X + 1):
            part2 += '#'
        else:
            part2 += '.'
        cycle += 1
        if cycle == ncycle:
            part1 += ncycle * X
            ncycle += cycle_step
    else:
        row_x = len(part2) % 40
        if row_x in (X - 1, X, X + 1):
            part2 += '#'
        else:
            part2 += '.'
        cycle += 1
        row_x = len(part2) % 40
        if row_x in (X - 1, X, X + 1):
            part2 += '#'
        else:
            part2 += '.'
        cycle += 1
        if cycle in (ncycle, ncycle + 1):
            part1 += ncycle * X
            ncycle += cycle_step
        X += int(line.split()[1])
print(part1)
for x_offset in range(6):
    print(''.join(part2[x_offset * 40:(x_offset + 1) * 40]))
