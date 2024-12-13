import collections
import itertools
import math
import re

inp = open(re.search(r"day\d\d", __file__)[0] + 'input.txt').read().strip()
cases = inp.split('\n\n')

def solve(ax, ay, bx, by, tx, ty):
    best = 99999999
    for a in range(101):
        for b in range(101):
            if a*ax + b*bx == tx and a*ay + b*by == ty:
                if best != 99999999:
                    print('multiple answers')
                # print(1, a, b)
                best = min(best, a*3 + b)
    return 0 if best == 99999999 else best

def solve2(ax, ay, bx, by, tx, ty):
    b = (ty - (tx*ay)/ax) / (by - (bx*ay)/ax)
    a = (tx - b*bx) / ax
    # print(2, a, b)
    pa = int(round(a, 0))
    pb = int(round(b, 0))
    if pa*ax+pb*bx == tx and pa*ay+pb*by == ty:
        return 3*pa + pb
    return 0

part1 = part2 = 0
for case in cases:
    tokens = re.findall(r'\d+', case, re.M)
    ax, ay, bx, by, tx, ty = map(int, tokens)

    # print(solve(ax, ay, bx, by, tx, ty),
    #       solve2(ax, ay, bx, by, tx, ty))
    part1 += solve(ax, ay, bx, by, tx, ty)
    part2 += solve2(
        ax, ay, bx, by,
        tx+10000000000000, ty+10000000000000)
print(part1)
print(part2)
