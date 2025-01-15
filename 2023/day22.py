import collections
import copy
import heapq
import itertools
import math
import re

inp = open(re.search(r"day\d\d", __file__)[0] + 'input.txt').read().strip()
# inp = '''1,0,1~1,2,1
# 0,0,2~2,0,2
# 0,2,3~2,2,3
# 0,0,4~0,2,4
# 2,0,5~2,2,5
# 0,1,6~2,1,6
# 1,1,8~1,1,9'''

bricks = []
for line in inp.splitlines():
    bricks.append(list(map(int, re.findall(r'\d+', line))))
bricks.sort(key=lambda b: (b[2], b[0], b[1]))

max_x = sorted(bricks, key=lambda b: b[3], reverse=True)[0][3]
max_y = sorted(bricks, key=lambda b: b[4], reverse=True)[0][4]
# print(max_x, max_y)

heights = collections.defaultdict(int)
piece_on_top = collections.defaultdict(lambda: -1)

def print_heights():
    for y in range(max_y + 1):
        row = '  '
        for x in range(max_x + 1):
            row += '{:3d} '.format(heights[(x, y)])
        print(row)

cannot_be_disintegrated = set()
for i, brick in enumerate(bricks):
    print(i, brick)
    target_height = 1
    for x in range(brick[0], brick[3] + 1):
        for y in range(brick[1], brick[4] + 1):
            target_height = max(target_height, heights[(x, y)] + 1)
    dh = brick[2] - target_height
    if dh > 0:
        print('  dropping brick', dh)
        brick[2] -= dh
        brick[5] -= dh

    pieces_below = set()
    for x in range(brick[0], brick[3] + 1):
        for y in range(brick[1], brick[4] + 1):
            if (heights[(x, y)] == target_height - 1 and 
                piece_on_top[(x, y)] != -1):
                pieces_below.add(piece_on_top[(x, y)])
            piece_on_top[(x, y)] = i
    print('  resting on', list(sorted(pieces_below)))
    if len(pieces_below) == 1:
        cannot_be_disintegrated.add(pieces_below.pop())

    for x in range(brick[0], brick[3] + 1):
        for y in range(brick[1], brick[4] + 1):
            heights[(x, y)] = brick[5]

    # print_heights()

print('\npart1:', len(bricks) - len(cannot_be_disintegrated))

def count_falling_bricks(bricks):
    fallen_bricks = 0
    heights = collections.defaultdict(int)

    for brick in bricks:
        target_height = 1
        for x in range(brick[0], brick[3] + 1):
            for y in range(brick[1], brick[4] + 1):
                target_height = max(target_height, heights[(x, y)] + 1)
        dh = brick[2] - target_height
        if dh > 0:
            brick[2] -= dh
            brick[5] -= dh
            fallen_bricks += 1

        for x in range(brick[0], brick[3] + 1):
            for y in range(brick[1], brick[4] + 1):
                heights[(x, y)] = brick[5]

    return fallen_bricks

part2 = 0
for i in range(len(bricks)):
    if i not in cannot_be_disintegrated:
        continue
    bricks_copy = copy.deepcopy(bricks)
    bricks_copy.pop(i)

    part2 += count_falling_bricks(bricks_copy)
print('part2:', part2)
