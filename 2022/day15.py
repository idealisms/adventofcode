import collections
import itertools
import math
import re

# inp = open(re.search(r"day\d\d", __file__)[0] + 'input.txt').read().strip()
# Rewrite to work with pypy
inp = open('day15input.txt').read().strip()
_inp = '''Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3'''

def dist(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

pts = []
for line in inp.splitlines():
    sx, sy, bx, by = list(map(int, re.findall('[-]?\d+', line)))
    pts.append((sx, sy, bx, by))

def ranges_for_y(ty):
    ranges = []
    for sx, sy, bx, by in pts:
        d = dist(sx, sy, bx, by)
        # print(sx, sy, bx, by, d)
        dx = d - abs(ty - sy)
        if dx >= 0:
            # print(sx, sy, bx, by, d, sx - dx, sx + dx)
            ranges.append((sx - dx, sx + dx))
    ranges.sort()
    return ranges

def merge(ranges):
    s = ranges[0][0]
    e = ranges[0][1]
    for range in ranges[1:]:
        if range[0] > e:
            return -1, e + 1
        elif range[0] <= e:
            e = max(e, range[1])
    return s, e

# part 1
ty = 2000000
_ty = 10
ranges = ranges_for_y(ty)
s, e = merge(ranges)
part1 = e - s + 1 - 1 # there's a beacon on the row
print(part1)

for ty in range(4000001):
    if ty % 100000 == 0:
        print(ty)
    ranges = ranges_for_y(ty)
    s, e = merge(ranges)
    if s == -1:
        print(e * 4000000 + ty)
        break
