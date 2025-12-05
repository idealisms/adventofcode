import collections
import heapq
import itertools
import math
import re

inp = open(re.search(r"day\d\d", __file__)[0] + 'input.txt').read().strip()
ranges_str, ids_str = inp.split('\n\n')
ranges = []
for range_str in ranges_str.splitlines():
    ranges.append(tuple(map(int, range_str.split('-'))))

part1 = 0
for id_str in ids_str.splitlines():
    id = int(id_str)
    for lo, hi in ranges:
        if lo <= id <= hi:
            part1 += 1
            break
print(part1)

pts = []
for lo, hi in ranges:
    pts.append((lo, -1))
    pts.append((hi, 1))
pts.sort()

part2 = score = 0
start = -1
for n, delta in pts:
    delta = -delta
    if score == 0 and delta == 1:
        start = n
    elif score == 1 and delta == -1:
        part2 += n - start + 1
    score += delta
print(part2)
