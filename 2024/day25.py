import collections
import heapq
import itertools
import math
import re

inp = open(re.search(r"day\d\d", __file__)[0] + 'input.txt').read().strip()

C = 5
R = 7
tops = []
bottoms = []
for pattern in inp.split('\n\n'):
    lines = pattern.splitlines()
    row = []
    if lines[0] == '.....':
        for c in range(C):
            cnt = 5
            for r in range(1, 6):
                if lines[r][c] == '#':
                    break
                cnt -= 1
            row.append(cnt)
        bottoms.append(row)
    else:
        for c in range(C):
            cnt = 0
            for r in range(1, 6):
                if lines[r][c] == '.':
                    break
                cnt += 1
            row.append(cnt)
        tops.append(row)

part1 = 0
for top_row in tops:
    for bottom_row in bottoms:
        is_match = True
        for c in range(C):
            if top_row[c] + bottom_row[c] > 5:
                is_match = False
                break
        if is_match:
            part1 += 1
print(part1)
