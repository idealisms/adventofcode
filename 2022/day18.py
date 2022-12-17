import collections
import itertools
import math
import re

inp = open(re.search(r"day\d\d", __file__)[0] + 'input.txt').read().strip()
_inp = '''2,2,2
1,2,2
3,2,2
2,1,2
2,3,2
2,2,1
2,2,3
2,2,4
2,2,6
1,2,5
3,2,5
2,1,5
2,3,5'''

pts = set()
for line in inp.splitlines():
    pts.add(tuple(map(int, re.findall('\d+', line))))

part1 = 0
offsets = [
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1),
]
min_n = max_n = 0
for pt in pts:
    min_n = min(min_n, *pt)
    max_n = max(max_n, *pt)
    for offset in offsets:
        if (pt[0] + offset[0],
            pt[1] + offset[1],
            pt[2] + offset[2]) not in pts:
            part1 += 1
print(part1)
# print(min_n, max_n) # [0 - 19]

outside = set()
q = [(-1, -1, -1)]
part2 = 0
while len(q):
    pt = q.pop(0)
    if pt in outside:
        continue
    if pt in pts:
        part2 += 1
        continue
    outside.add(pt)
    for offset in offsets:
        new_pt = (
            pt[0] + offset[0],
            pt[1] + offset[1],
            pt[2] + offset[2])
        if (-1 <= new_pt[0] <= 20 and
            -1 <= new_pt[1] <= 20 and
            -1 <= new_pt[2] <= 20):
            q.append(new_pt)
print(part2)
