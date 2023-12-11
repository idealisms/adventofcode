import collections
import itertools
import math
import re
import pprint
import functools

inp = open(re.search(r"day\d\d", __file__)[0] + 'input.txt').read().strip()
inp_ = '''0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45'''

lines = inp.splitlines()
hists = []
for line in lines:
    nums = list(map(int, line.split()))
    hists.append(nums)

def get_next_num(nums):
    values = []
    values.append(nums[:])
    while True:
        cur_row = values[-1]
        new_row = []
        for i in range(len(cur_row) - 1):
            new_row.append(cur_row[i+1] - cur_row[i])
        values.append(new_row)
        if new_row.count(new_row[0]) == len(new_row):
            break
    # pprint.pp(values)
    part1 = sum(l[-1] for l in values)
    part2 = functools.reduce(
        lambda acc, l: l[0] - acc,
        reversed(values),
        0)
    return part1, part2

part1 = part2 = 0
for hist in hists:
    p1, p2 = get_next_num(hist)
    part1 += p1
    part2 += p2
print(part1)
print(part2)
