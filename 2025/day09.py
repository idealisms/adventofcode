import collections
import heapq
import itertools
import math
import re

inp = open(re.search(r"day\d\d", __file__)[0] + 'input.txt').read().strip()
# inp = '''7,1
# 11,1
# 11,7
# 9,7
# 9,5
# 2,5
# 2,3
# 7,3'''

pts = []
for line in inp.splitlines():
    pts.append(tuple(map(int, line.split(','))))

N = len(pts)
part1 = 0
for i, pt1 in enumerate(pts):
    for j in range(i + 1, N):
        pt2 = pts[j]
        part1 = max(part1, (abs(pt1[0] - pt2[0]) + 1) * (abs(pt1[1] - pt2[1]) + 1))
print(part1)

cols = list(sorted(set(c for c, _ in pts)))
rows = list(sorted(set(r for _, r in pts)))
C, R = len(cols), len(rows)
col_map = {}
for i, c in enumerate(cols):
    col_map[c] = i
row_map = {}
for i, r in enumerate(rows):
    row_map[r] = i
def compress_pt(pt):
    return (col_map[pt[0]], row_map[pt[1]])
grid = [[' '] * 250 for _ in range(250)]

pts.append(pts[0])
for pt1, pt2 in itertools.pairwise(pts):
    c1, r1 = compress_pt(pt1)
    c2, r2 = compress_pt(pt2)
    if c1 == c2:
        for r in range(min(r1, r2), max(r1, r2) + 1):
            grid[c1][r] = '#'
    else:
        for c in range(min(c1, c2), max(c1, c2) + 1):
            grid[c][r1] = '#'

q = [(0, 0), (249, 0)]
while len(q) > 0:
    c, r = q.pop()
    if c < 0 or r < 0 or c >= 250 or r >= 250:
        continue
    if grid[c][r] != ' ':
        continue
    grid[c][r] = 'X'
    q.append((c - 1, r))
    q.append((c + 1, r))
    q.append((c, r - 1))
    q.append((c, r + 1))

# for r in range(250):
#     print(''.join(grid[r]))

part2 = 0
for i, pt1 in enumerate(pts):
    for j in range(i + 1, N):
        pt2 = pts[j]
        c1, r1 = compress_pt(pt1)
        c2, r2 = compress_pt(pt2)
        is_ok = True
        for c in range(min(c1, c2), max(c1, c2) + 1):
            for r in range(min(r1, r2), max(r1, r2) + 1):
                if grid[c][r] == 'X':
                    is_ok = False
                    break
            if not is_ok:
                break
        if is_ok:
            part2 = max(part2, (abs(pt1[0] - pt2[0]) + 1) * (abs(pt1[1] - pt2[1]) + 1))
print(part2)
