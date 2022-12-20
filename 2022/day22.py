import collections
import itertools
import math
import re

inp = open(re.search(r"day\d\d", __file__)[0] + 'input.txt').read()
_inp = '''        ...#
        .#..
        #...
        ....
...#.......#
........#...
..#....#....
..........#.
        ...#....
        .....#..
        .#......
        ......#.

10R5L5R10L4R5L5'''

inp_grid, moves = inp.split('\n\n')
grid = inp_grid.splitlines()
grid = [' ' + line + ' ' for line in grid]
num_cols = max(len(line) for line in grid)
grid = [
    line if len(line) == num_cols
    else line + (' ' * (num_cols - len(line)))
    for line in grid
]
grid.insert(0, ' ' * len(grid[0]))
grid.append(' ' * len(grid[0]))
moves = re.findall('L|R|\d+', moves.strip())
moves = [int(m) if m not in 'LR' else m for m in moves]

DIRS = [
    (0, 1), # right
    (1, 0), # down
    (0, -1), # left
    (-1, 0), # up
]
RIGHT, DOWN, LEFT, UP = range(4)

def init():
    row = 1
    col = 0
    while grid[row][col] == ' ':
        col += 1
    return row, col, 0

row, col, f = init()

for move in moves:
    if move == 'L':
        f = (f - 1) % len(DIRS)
    elif move == 'R':
        f = (f + 1) % len(DIRS)
    else:
        for _ in range(move):
            dr, dc = DIRS[f]
            next_row = row + dr
            next_col = col + dc
            if grid[next_row][next_col] == ' ':
                dr, dc = DIRS[(f + 2) % len(DIRS)]
                while grid[next_row + dr][next_col + dc] != ' ':
                    next_row += dr
                    next_col += dc
            if grid[next_row][next_col] == '#':
                break
            elif grid[next_row][next_col] == '.':
                row = next_row
                col = next_col
            else:
                raise ValueError
print(1000*row + 4*col+f)

s = (len(grid) - 2) // 4
#              1 1 1
#            5 0 0 5
#            1 0 1 0
#            
#             0   6
# 1          EEE FFF
#          3 EEE FFF 5
# 50         EEE FFF
#                 4
# 51         DDD
#          2 DDD 4
# 100        DDD
#         2
# 101    BBB CCC
#      3 BBB CCC 5
# 150    BBB CCC
#             1
# 151    AAA
#      0 AAA 1
# 200    AAA
#         6
def wrap_edge(r, c, f):
    # print('w_e', r, c, DIR_NAME[f])
    if r == 0 and 51 <= c <= 100: # 0
        assert f == UP
        return c + 100, 1, RIGHT
    elif 151 <= r <= 200 and c == 0:
        assert f == LEFT
        return 1, r - 100, DOWN
    elif r == 151 and 51 <= c <= 100 and f == DOWN: # 1
        return 100 + c, 50, LEFT
    elif 151 <= r <= 200 and c == 51 and f == RIGHT:
        return 150, r - 100, UP
    elif 51 <= r <= 100 and c == 50 and f == LEFT: # 2
        return 101, r - 50, DOWN
    elif r == 100 and 1 <= c <= 50 and f == UP:
        return c + 50, 51, RIGHT
    elif 101 <= r <= 150 and c == 0: # 3
        assert f == LEFT
        return 151 - r, 51, RIGHT
    elif 1 <= r <= 50 and c == 50:
        assert f == LEFT
        return 151 - r, 1, RIGHT
    elif 51 <= r <= 100 and c == 101 and f == RIGHT: # 4
        return 50, 50 + r, UP
    elif r == 51 and 101 <= c <= 150 and f == DOWN:
        return c - 50, 100, LEFT
    elif 101 <= r <= 150 and c == 101: # 5
        assert f == RIGHT
        return 151 - r, 150, LEFT
    elif 1 <= r <= 50 and c == 151:
        assert f == RIGHT
        return 151 - r, 100, LEFT
    elif r == 0 and 101 <= c <= 150: # 6
        assert f == UP
        return 200, c - 100, UP
    elif r == 201:
        assert 1 <= c <= 50
        assert f == DOWN
        return 1, c + 100, DOWN
    print(r, c, DIR_NAME[f])
    raise ValueError

row, col, f = init()
DIR_NAME = [
    'right',
    'down',
    'left',
    'up',
]

for move in moves:
    if move == 'L':
        f = (f - 1) % len(DIRS)
        # print('L', DIR_NAME[f])
    elif move == 'R':
        f = (f + 1) % len(DIRS)
        # print('R', DIR_NAME[f])
    else:
        # print('move', DIR_NAME[f], move, f'{row},{col}')
        for _ in range(move):
            dr, dc = DIRS[f]
            next_row = row + dr
            next_col = col + dc
            next_f = f
            if grid[next_row][next_col] == ' ':
                # print(row, col, DIR_NAME[f])
                next_row, next_col, next_f = wrap_edge(next_row, next_col, f)
            if grid[next_row][next_col] == '#':
                break
            elif grid[next_row][next_col] == '.':
                row = next_row
                col = next_col
                f = next_f
            else:
                raise ValueError
        # print('end', f'{row},{col} {DIR_NAME[f]}')
print(1000*row + 4*col+f)
# 42553 too low