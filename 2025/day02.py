import bisect
import collections
import heapq
import itertools
import math
import re

inp = open(re.search(r"day\d\d", __file__)[0] + 'input.txt').read().strip()
inp = '''11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124'''

part1 = 0
for range_str in inp.split(','):
    lo, hi = range_str.split('-')
    if len(lo) % 2 == 1:
        start = 10**((len(lo) + 1) // 2 - 1)
    else:
        start = int(lo[:len(lo) // 2])
    while start * 10**(len(str(start))) + start <= int(hi):
        if start * 10**(len(str(start))) + start >= int(lo):
            part1 += start * 10**(len(str(start))) + start
        start += 1
print(part1)

max_value = 0
for range_str in inp.split(','):
    lo, hi = range_str.split('-')
    max_value = max(max_value, int(hi))
values = set()
for i in range(1, 100000):
    s = str(i)
    for j in range(2, 10):
        if int(s * j) <= max_value:
            values.add(int(s * j))

values = list(sorted(values))
part2 = 0
for range_str in inp.split(','):
    lo, hi = map(int, range_str.split('-'))
    part2 += sum(values[bisect.bisect_left(values, lo):bisect.bisect_right(values, hi)])
print(part2)
