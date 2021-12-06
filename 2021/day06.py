import collections
import itertools
import math
import re

inp = open(re.match(r"day\d\d", __file__)[0] + 'input.txt').read().strip()

fish = list(map(int, inp.split(',')))
fmap = collections.defaultdict(int)
for n in range(9):
    fmap[n] = fish.count(n)

for day in range(256):
    if day == 80:
        print(sum(fmap.values()))
    new_fmap = collections.defaultdict(int)
    for n in range(9):
        if n == 0:
            new_fmap[6] += fmap[n]
            new_fmap[8] += fmap[n]
        else:
            new_fmap[n-1] += fmap[n]
    fmap = new_fmap
print(sum(fmap.values()))
