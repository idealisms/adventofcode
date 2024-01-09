import collections
import itertools
import math
import re

# fill() tends to recurse pretty deep, so we increase our stack.
import resource, sys
resource.setrlimit(resource.RLIMIT_STACK, (2**29,-1))
sys.setrecursionlimit(10**6)

inp = open(re.search(r"day\d\d", __file__)[0] + 'input.txt').read().strip()
# inp = '''.S------7.
# .|F----7|.
# .||OOOO||.
# .||OOOO||.
# .|L-7F-J|.
# .|II||II|.
# .L--JL--J.
# ..........'''

grid = inp.splitlines()
pos = -1 - 1j
for r, row in enumerate(grid):
    c = row.find('S')
    pos = complex(r, c)
    if c != -1:
        break
START = pos
grid2x = [[' '] * (2 * len(grid[0])) for _ in range(2 * len(grid))]
grid2x[int(pos.real) * 2][int(pos.imag) * 2] = 'X'

UP, RIGHT, DOWN, LEFT = range(4)
STEP = [
    -1,
    1j,
    1,
    -1j,
]

# manually do first step
steps = 1
d = DOWN
grid2x[int(pos.real) * 2][int(pos.imag) * 2] = 'X'
grid2x[int(pos.real) * 2 + 1][int(pos.imag) * 2] = 'X'
pos += STEP[d]
while pos != START:
    cur_pipe = grid[int(pos.real)][int(pos.imag)]
    grid2x[int(pos.real) * 2][int(pos.imag) * 2] = 'X'
    if d == UP:
        if cur_pipe == '|':
            new_dir = UP
        elif cur_pipe == '7':
            new_dir = LEFT
        elif cur_pipe == 'F':
            new_dir = RIGHT
        else:
            raise 'up?'
    elif d == RIGHT:
        if cur_pipe == '7':
            new_dir = DOWN
        elif cur_pipe == '-':
            new_dir = RIGHT
        elif cur_pipe == 'J':
            new_dir = UP
        else:
            raise 'right?'
    elif d == DOWN:
        if cur_pipe == 'J':
            new_dir = LEFT
        elif cur_pipe == '|':
            new_dir = DOWN
        elif cur_pipe == 'L':
            new_dir = RIGHT
        else:
            raise 'down?'
    elif d == LEFT:
        if cur_pipe == 'L':
            new_dir = UP
        elif cur_pipe == '-':
            new_dir = LEFT
        elif cur_pipe == 'F':
            new_dir = DOWN
        else:
            raise 'left?'
    steps += 1
    pos += STEP[new_dir]
    d = new_dir
    if d == UP:
        grid2x[int(pos.real) * 2 + 1][int(pos.imag) * 2] = 'X'
    elif d == RIGHT:
        grid2x[int(pos.real) * 2][int(pos.imag) * 2 - 1] = 'X'
    elif d == DOWN:
        grid2x[int(pos.real) * 2 - 1][int(pos.imag) * 2] = 'X'
    elif d == LEFT:
        grid2x[int(pos.real) * 2][int(pos.imag) * 2 + 1] = 'X'
print(steps // 2)
# for row in grid2x:
#     print(''.join(row))

def fill(r, c):
    if r < 0 or r >= len(grid2x):
        return
    row = grid2x[r]
    if c < 0 or c >= len(row):
        return
    if row[c] == ' ':
        row[c] = 'O'
        fill(r+1, c)
        fill(r-1, c)
        fill(r, c+1)
        fill(r, c-1)

for r, row in enumerate(grid2x):
    if r == 0 or r == len(grid2x) - 1:
        for c, value in enumerate(row):
            if value == ' ':
                fill(r, c)
    else:
        if row[0] == ' ':
            fill(r, 0)
        elif row[len(row) - 1] == ' ':
            fill(r, len(row) - 1)

# print()
# for row in grid2x:
#     print(''.join(row))

part2 = 0
for r, row in enumerate(grid2x):
    for c, value in enumerate(row):
        if value == ' ' and r % 2 == 0 and c % 2 == 0:
            part2 += 1
print(part2)