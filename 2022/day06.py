import collections
import itertools
import math
import re

inp = open(re.search(r"day\d\d", __file__)[0] + 'input.txt').read().strip()

part1 = part2 = 0
for i in range(len(inp)):
    if part1 == 0 and len(set(inp[i:i+4])) == 4:
        part1 = i + 4
    if len(set(inp[i:i+14])) == 14:
        part2 = i + 14
        break
print(part1)
print(part2)
