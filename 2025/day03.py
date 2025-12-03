import collections
import heapq
import itertools
import math
import re

inp = open(re.search(r"day\d\d", __file__)[0] + 'input.txt').read().strip()
# inp = '''987654321111111
# 811111111111119
# 234234234234278
# 818181911112111'''

part1 = 0
for line in inp.splitlines():
    first = line.find(max(line[:-1]))
    best = line[first] + max(line[first+1:])
    # print(best)
    part1 += int(best)
print(part1)

part2 = 0
for line in inp.splitlines():
    best = ''
    start = 0
    for n in range(12):
        cur = line.find(max(line[start:len(line) + n - 11]), start)
        best += line[cur]
        start = cur + 1
    # print(best)
    part2 += int(best)
print(part2)
