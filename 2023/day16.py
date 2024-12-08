import collections
import itertools
import math
import re

inp = open(re.search(r"day\d\d", __file__)[0] + 'input.txt').read().strip()
# inp = '''.|...\\....
# |.-.\\.....
# .....|-...
# ........|.
# ..........
# .........\\
# ..../.\\\\..
# .-.-/..|..
# .|....-|.\\
# ..//.|....'''

grid = {}
rows = inp.splitlines()
R = len(rows)
C = len(rows[0])
for r, line in enumerate(rows):
    for c, char in enumerate(line):
        if char != '.':
            grid[(r, c)] = char

UP, RIGHT, DOWN, LEFT = list(range(4))
DELTA = (
    (-1, 0),
    (0, 1),
    (1, 0),
    (0, -1),
)

def add(beams, r, c, d):
    beams.append((r + DELTA[d][0], c + DELTA[d][1], d))

def energized(beams):
    visited = set()
    while len(beams) > 0:
        r, c, d = beams.pop()
        if not (0 <= r < R and 0 <= c < C):
            continue
        if (r, c, d) in visited:
            continue
        visited.add((r, c, d))
        cur = grid.get((r, c), '.')
        if cur == '.':
            add(beams, r, c, d)
        elif cur == '|':
            if d in (UP, DOWN):
                add(beams, r, c, d)
            else:
                add(beams, r, c, UP)
                add(beams, r, c, DOWN)
        elif cur == '-':
            if d in (LEFT, RIGHT):
                add(beams, r, c, d)
            else:
                add(beams, r, c, LEFT)
                add(beams, r, c, RIGHT)
        elif cur == '/':
            if d == UP:
                add(beams, r, c, RIGHT)
            elif d == RIGHT:
                add(beams, r, c, UP)
            elif d == DOWN:
                add(beams, r, c, LEFT)
            elif d == LEFT:
                add(beams, r, c, DOWN)
        elif cur == '\\':
            if d == UP:
                add(beams, r, c, LEFT)
            elif d == RIGHT:
                add(beams, r, c, DOWN)
            elif d == DOWN:
                add(beams, r, c, RIGHT)
            elif d == LEFT:
                add(beams, r, c, UP)
    spaces = set()
    for r, c, d in visited:
        spaces.add((r, c))
    return len(spaces)

beams = [(0, 0, RIGHT)]
print(energized(beams)) # part1

part2 = 0
for r in range(R):
    beams = [(r, 0, RIGHT)]
    part2 = max(part2, energized(beams))
    beams = [(r, C - 1, LEFT)]
    part2 = max(part2, energized(beams))
for c in range(C):
    beams = [(0, c, DOWN)]
    part2 = max(part2, energized(beams))
    beams = [(R - 1, c, UP)]
    part2 = max(part2, energized(beams))
print(part2)