import collections
import heapq
import itertools
import math
import re

inp = open(re.search(r"day\d\d", __file__)[0] + 'input.txt').read().strip()
MI, MA = 200000000000000, 400000000000000
# inp = '''19, 13, 30 @ -2,  1, -2
# 18, 19, 22 @ -1, -1, -2
# 20, 25, 34 @ -2, -2, -4
# 12, 31, 28 @ -1, -2, -1
# 20, 19, 15 @  1, -5, -3'''
# MI, MA = 7, 27


stones = []
for line in inp.splitlines():
    nums = re.findall('[-]?\d+', line)
    if len(nums) != 6:
        raise ValueError
    stones.append(tuple(map(int, nums)))

def det(v1, v2):
    return (v1[0] * v2[1]) - (v1[1] * v2[0])

# (xi1, yi1) + t1 * (dx1, dy1) = (xi2, yi2) + t2 * (dx2, dy2)
#
# xi1 + t1 * dx1 = xi2 + t2 * dx2
# yi1 + t1 * dy1 = yi2 + t2 * dy2
#
# t1 * dx1 - t2 * dx2 = xi2 - xi1
# t1 * dy1 - t2 * dy2 = yi2 - yi1
part1 = 0
for a, a_nums in enumerate(stones):
    for b_nums in stones[a+1:]:
        xi1, yi1, zi1, dx1, dy1, dz1 = a_nums
        xi2, yi2, zi2, dx2, dy2, dz2 = b_nums
        # print(a_nums)
        # print(b_nums)

        # Using Cramer's Rule
        vt1 = (dx1, dy1)
        vt2 = (-dx2, -dy2)
        vc = (xi2 - xi1, yi2 - yi1)
        D = det(vt1, vt2)
        if D == 0:
            # print('  parallel')
            continue
        t1 = det(vc, vt2) / D
        t2 = det(vt1, vc) / D
        if t1 < 0 or t2 < 0:
            # print('  past')
            continue

        # print('  ', xi1 + t1 * dx1, ' ', yi1 + t1 * dy1)

        if (MI <= xi1 + t1 * dx1 <= MA and
            MI <= yi1 + t1 * dy1 <= MA):
            part1 += 1
print(part1)

# Eh, kind of cheating for part 2.
import z3
x0 = z3.Int('x0')
y0 = z3.Int('y0')
z0 = z3.Int('z0')
dx = z3.Int('dx')
dy = z3.Int('dy')
dz = z3.Int('dz')
t1 = z3.Int('t1')
t2 = z3.Int('t2')
t3 = z3.Int('t3')

s = z3.Solver()
s.add(t1 > 0, t2 > 0, t3 > 0)
s.add(x0 + dx * t1 == stones[0][0] + stones[0][3] * t1)
s.add(y0 + dy * t1 == stones[0][1] + stones[0][4] * t1)
s.add(z0 + dz * t1 == stones[0][2] + stones[0][5] * t1)
s.add(x0 + dx * t2 == stones[1][0] + stones[1][3] * t2)
s.add(y0 + dy * t2 == stones[1][1] + stones[1][4] * t2)
s.add(z0 + dz * t2 == stones[1][2] + stones[1][5] * t2)
s.add(x0 + dx * t3 == stones[2][0] + stones[2][3] * t3)
s.add(y0 + dy * t3 == stones[2][1] + stones[2][4] * t3)
s.add(z0 + dz * t3 == stones[2][2] + stones[2][5] * t3)
#print(s)
print(s.check())
m = s.model()
print(m.evaluate(x0 + y0 + z0))
