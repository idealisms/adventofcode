import collections
import itertools
import math
import re

inp = open(re.search(r"day\d\d", __file__)[0] + 'input.txt').read().strip()
# inp = '''########
# #..O.O.#
# ##@.O..#
# #...O..#
# #.#.O..#
# #...O..#
# #......#
# ########

# <^^>>>vv<v>>v<<'''

# inp = '''##########
# #..O..O.O#
# #......O.#
# #.OO..O.O#
# #..O@..O.#
# #O#..O...#
# #O..O..O.#
# #.OO.O.OO#
# #....O...#
# ##########

# <vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
# vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
# ><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
# <<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
# ^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
# ^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
# >^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
# <><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
# ^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
# v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^'''

# inp = '''#######
# #...#.#
# #.....#
# #..OO@#
# #..O..#
# #.....#
# #######

# <vv<<^^<<^^'''

map_inp, moves = inp.split('\n\n')
grid = map_inp.splitlines()
R = len(grid)
C = len(grid[0])
for r in range(R):
    grid[r] = list(grid[r])

rr = rc = 0
for r in range(R):
    for c in range(C):
        if grid[r][c] == '@':
            rr, rc = r, c
            grid[r][c] = '.'
            break
    if rr != 0:
        break

grid2 = []
for r in range(R):
    row = []
    for c in range(C):
        if grid[r][c] == '.':
            row.append('.')
            row.append('.')
        elif grid[r][c] == '#':
            row.append('#')
            row.append('#')
        elif grid[r][c] == 'O':
            row.append('[')
            row.append(']')
    grid2.append(row)
grid = grid2
rc *= 2
print(rr, rc)

def move(r, c, dr, dc):
    print('move', r, c, dr, dc)
    if grid[r+dr][c+dc] == '#':
        print('  wall')
        return r, c
    if grid[r+dr][c+dc] == '.':
        grid[r+dr][c+dc] = grid[r][c]
        grid[r][c] = '.'
        print('  open')
        return r+dr, c+dc
    if grid[r+dr][c+dc] in ('O', '[', ']'):
        print('  barrel')
        nr, nc = move(r+dr, c+dc, dr, dc)
        if nr == r+dr and nc == c+dc:
            # didn't move
            return r, c
        elif nr == r+dr+dr and nc == c+dc+dc:
            grid[r+dr][c+dc] = grid[r][c]
            grid[r][c] = '.'
            return r+dr, c+dc
        raise 'Should not be here O'
    raise 'Should not be here space'

def pr():
    print(rr, rc)
    if grid[rr][rc] != '.':
        raise 'robot overlapping'
    grid[rr][rc] = '@'
    for row in grid:
        print(''.join(row))
    grid[rr][rc] = '.'
    print()

# part 1
# for line in moves.splitlines():
#     for c in line:
#         # pr()
#         if c == '<':
#             rr, rc = move(rr, rc, 0, -1)
#         elif c == '>':
#             rr, rc = move(rr, rc, 0, 1)
#         elif c == '^':
#             rr, rc = move(rr, rc, -1, 0)
#         elif c == 'v':
#             rr, rc = move(rr, rc, 1, 0)
# # pr()
# part1 = 0
# for r in range(R):
#     for c in range(C):
#         if grid[r][c] == 'O':
#             part1 += r * 100 + c
# print(part1)

def move2(pts, d):
    barrels = set()
    for pt in pts:
        r, c = pt
        if grid[r+d][c] == '#':
            return False
        elif grid[r+d][c] == '[':
            barrels.add((r+d, c))
            barrels.add((r+d, c+1))
        elif grid[r+d][c] == ']':
            barrels.add((r+d, c))
            barrels.add((r+d, c-1))
    if len(barrels) == 0:
        for pt in pts:
            r, c = pt
            grid[r+d][c] = grid[r][c]
            grid[r][c] = '.'
        return True
    else:
        if move2(barrels, d):
            for pt in pts:
                r, c = pt
                grid[r+d][c] = grid[r][c]
                grid[r][c] = '.'
            return True
        return False

for line in moves.splitlines():
    for c in line:
        # pr()
        if c == '<':
            rr, rc = move(rr, rc, 0, -1)
        elif c == '>':
            rr, rc = move(rr, rc, 0, 1)
        elif c == '^':
            if move2([(rr, rc)], -1):
                rr -= 1
        elif c == 'v':
            if move2([(rr, rc)], 1):
                rr += 1
pr()

part2 = 0
for r in range(R):
    for c in range(C*2):
        if grid[r][c] == '[':
            part2 += r * 100 + c
print(part2)
