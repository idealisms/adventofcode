import collections
import itertools
import math
import re

inp = open(re.search(r"day\d\d", __file__)[0] + 'input.txt').read().strip()
times_str, dist_str = inp.splitlines()

times = list(map(int, re.findall(r'\d+', times_str)))
distances = list(map(int, re.findall(r'\d+', dist_str)))

better_times = []
for time, distance in zip(times, distances):
    better = 0
    for hold_time in range(1, time):
        if hold_time * (time - hold_time) > distance:
            better += 1
    better_times.append(better)
print(math.prod(better_times))

time = int(''.join(re.findall(r'\d+', times_str)))
distance = int(''.join(re.findall(r'\d+', dist_str)))
# print(time, distance)

def search(lo, hi, greater_than):
    hold_time = (lo + hi) // 2
    if lo == hi:
        return lo
    if greater_than:
        if hold_time * (time - hold_time) > distance:
            return search(lo, hold_time, greater_than)
        else:
            if hold_time == lo:
                return hi
            return search(hold_time, hi, greater_than)
    else:
        if hold_time * (time - hold_time) > distance:
            if hold_time == lo:
                return hi
            return search(hold_time, hi, greater_than)
        else:
            return search(lo, hold_time, greater_than)

lo = search(1, time // 2, greater_than=True)
hi = search(time // 2, time, greater_than=False)
# print(lo, hi)
print(hi-lo)
