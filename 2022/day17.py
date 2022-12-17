import collections
import itertools
import math
import re

inp = open('day17input.txt').read().strip()
_inp = '>>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>'

gas = inp
gi = 0
# walls at c = 0, c = 8 and r = 0
top = 0
# Described as coordinates (r, c) from the lower left.
rocks = [
    # ####
    [(0, 0), (0, 1), (0, 2), (0, 3)],

    # .#.
    # ###
    # .#.
    [(0, 1), (1, 0), (1, 1), (1, 2), (2, 1)],

    # ..#
    # ..#
    # ###
    [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2)],

    # #
    # #
    # #
    # #
    [(0, 0), (1, 0), (2, 0), (3, 0)],

    # ##
    # ##
    [(0, 0), (0, 1), (1, 0), (1, 1)],
]
ri = 0
# each row is a list of '.' and '#'
pit = [['#'] * 9]

def printpit():
    for row in reversed(pit):
        print(''.join(row))
    print()

def move(rock, dr, dc, off_r, off_c):
    '''Returns has_moved (bool), new dr, new dc'''
    for r, c in rock:
        if pit[r + dr + off_r][c + dc + off_c] == '#':
            return False, dr, dc
    return True, dr + off_r, dc + off_c

seen = {}
cycled = False
for step in range(1000000000000):
    rock = rocks[ri]
    ri = (ri + 1) % len(rocks)

    dr = top + 4
    dc = 3

    max_r = max(dr + r for (r, _) in rock)
    while len(pit) <= max_r:
        pit.append(['#'] + ['.'] * 7 + ['#'])

    while True:
        _, dr, dc = move(
            rock, dr, dc, 0, 1 if gas[gi] == '>' else -1)
        gi = (gi + 1) % len(gas)

        has_moved, dr, dc = move(rock, dr, dc, -1, 0)
        if not has_moved:
            break
    for r, c in rock:
        pit[r + dr][c + dc] = '#'
        top = max(top, r + dr)
    # part1
    if step == 2021:
        print('part1', top)
    if step == 5000:
        break

    # part 2
    if ri == 1 and not cycled:
        fp = gi, dc
        if fp in seen:
            print('cycle', seen[fp], step, fp) # 25 1750
            # cycled = True
            # break # This happens before 2021
        else:
            seen[fp] = step
    # if step in (25, 1575 + 25, 1750):
    if step in (415, 2130, 415+1314):
        print('height at', step, top) # 45, 2789
    # if (step - 25) % 1725 == 0:
    #     print(step, top, ri, gi, dc)

    # printpit()

start_offset = 15
cycle_length = 50 - start_offset
cycle_height = 79 - 26
remaining = (1000000000000 - (start_offset + 1)) % cycle_length
# print('remaining', remaining) # 34
# height at (start_offset + remaining)
height_of_extra = 78
part2 = height_of_extra + ((1000000000000 - (start_offset + 1)) // cycle_length) * cycle_height
print('part2 (test)', part2)

start_offset = 415
cycle_length = 2130 - start_offset # 1715
cycle_height = 3376 - 665 # 2711
remaining = (1000000000000 - (start_offset + 1)) % cycle_length
print('remaining', remaining) # 1314
# height at (start_offset + remaining)
height_of_extra = 2751
part2 = height_of_extra + ((1000000000000 - (start_offset + 1)) // cycle_length) * cycle_height
print('part2', part2)
