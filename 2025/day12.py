import collections
import heapq
import itertools
import math
import re

inp = open(re.search(r"day\d\d", __file__)[0] + 'input.txt').read().strip()
blobs = inp.split('\n\n')
sizes = [s.count('#') for s in blobs[:-1]]
part1 = 0
for line in blobs[-1].splitlines():
    dims, pieces_str = line.split(': ')
    x, y = tuple(map(int, dims.split('x')))
    pieces = [int(s) for s in pieces_str.split(' ')]
    if x*y > sum(a * b for a, b in zip(pieces, sizes)):
        part1 += 1
print(part1)