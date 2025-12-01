import collections
import heapq
import itertools
import math
import re

inp = open(re.search(r"day\d\d", __file__)[0] + 'input.txt').read().strip()
cur = 50
part1 = part2 = 0
for line in inp.splitlines():
    d = int(line[1:])
    part2 += d // 100
    d %= 100
    prev = cur
    if line[0] == 'L':
        cur -= d
    else:
        cur += d
    if (prev != 0 and cur < 1) or cur > 99:
        part2 += 1
    cur %= 100
    if cur == 0:
        part1 += 1
print(part1)
print(part2)