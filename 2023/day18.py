import collections
import heapq
import itertools
import math
import re

inp = open(re.search(r"day\d\d", __file__)[0] + 'input.txt').read().strip()
# inp = '''R 6 (#70c710)
# D 5 (#0dc571)
# L 2 (#5713f0)
# D 2 (#d2c081)
# R 2 (#59c680)
# D 2 (#411b91)
# L 5 (#8ceee2)
# U 2 (#caa173)
# L 1 (#1b58a2)
# U 2 (#caa171)
# R 2 (#7807d2)
# U 3 (#a77fa3)
# L 2 (#015232)
# U 2 (#7a21e3)'''


DIRS = {
    'R': 0+1j,
    'D': 1,
    'L': 0-1j,
    'U': -1,
}
DIRS2 = {
    '0': 0+1j,
    '1': 1,
    '2': 0-1j,
    '3': -1,
}

pts = [0j]
pts2 = [0j]
lava = set(pts)
maxr = minr = maxc = minc = 0
for line in inp.splitlines():
    d, m, color = line.split(' ')
    cur = pts[-1]
    for _ in range(int(m)):
        cur += DIRS[d]
        lava.add(cur)
    pts.append(pts[-1] + (DIRS[d] * int(m)))
    maxr = max(pts[-1].real, maxr)
    minr = min(pts[-1].real, minr)
    maxc = max(pts[-1].imag, maxc)
    minc = min(pts[-1].imag, minc)

    d2 = DIRS2[color[-2]]
    m2 = int(color[2:-2], 16)
    pts2.append(pts2[-1] + (d2 * m2))
maxr, minr, maxc, minc = map(int, (maxr, minr, maxc, minc))
# print(minr, maxr)
# print(minc, maxc)
# print(len(lava))

def flood(lava, start):
    q = [start]
    while len(q) > 0:
        pt = q.pop()
        if pt in lava:
            continue
        lava.add(pt)
        for d in DIRS.values():
            q.append(pt + d)

    return len(lava)

# start = complex((maxr + minr) // 2, (maxc + minc) // 2)
# Naive solution doing a flood fill of the grid.
start = complex(1, 1)
print(flood(lava, start))

# General solution for larger numbers. We transform the grid
# by collapsing large distances down to a single point.
# Here's an example of the test input:
#   0_1_2_4_6
# 0 #########
# _ #       #
# 2 #####   #
# _     #   #
# 5 ##### ###
# _ #     #
# 7 ###   ###
# _   #     #
# 9   #######
def solve(pts):
    rows = set()
    cols = set()
    for pt in pts:
        rows.add(pt.real)
        cols.add(pt.imag)
    rows = sorted(list(rows))
    cols = sorted(list(cols))
    row2idx = {}
    for i, row in enumerate(rows):
        row2idx[row] = i * 2
    col2idx = {}
    for i, col in enumerate(cols):
        col2idx[col] = i * 2

    trans_map = set()
    for i, pt in enumerate(pts):
        next_pt = pts[(i+1) % len(pts)]
        if pt.real == next_pt.real:
            r = row2idx[pt.real]
            c1 = col2idx[pt.imag]
            c2 = col2idx[next_pt.imag]
            for c in range(min(c1, c2), max(c1, c2) + 1):
                trans_map.add(complex(r, c))
        else:
            c = col2idx[pt.imag]
            r1 = row2idx[pt.real]
            r2 = row2idx[next_pt.real]
            for r in range(min(r1, r2), max(r1, r2) + 1):
                trans_map.add(complex(r, c))
    # print(trans_map)
    # for r in range(len(rows) * 2):
    #     row = ''
    #     for c in range(len(cols) * 2):
    #         if complex(r, c) in trans_map:
    #             row += '#'
    #         else:
    #             row += '.'
    #     print(row)
    # print(len(rows), len(cols))
    start = complex(row2idx[pts[0].real] + 1, col2idx[pts[0].imag] + 1)
    # print(start)
    flood(trans_map, start)

    rows = list(map(int, rows))
    cols = list(map(int, cols))
    area = 0
    for pt in trans_map:
        h = w = 1
        if int(pt.real) % 2 == 1:
            r1 = rows[int(pt.real) // 2]
            r2 = rows[int(pt.real) // 2 + 1]
            h = abs(r1 - r2) - 1
        if int(pt.imag) % 2 == 1:
            c1 = cols[int(pt.imag) // 2]
            c2 = cols[int(pt.imag) // 2 + 1]
            w = abs(c1 - c2) - 1
        # print(pt, h, w)
        area += h * w
    return area

print(solve(pts))
print(solve(pts2))
