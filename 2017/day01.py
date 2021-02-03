import collections
import itertools
import math
import re

inp = open(re.match(r"day\d\d", __file__)[0] + 'input.txt').read().strip()
print('part1:', sum(int(d) for i, d in enumerate(inp)
                    if inp[i] == inp[(i+1) % len(inp)]))
print('part2:', sum(int(d) for i, d in enumerate(inp)
                    if inp[i] == inp[(i+len(inp)//2) % len(inp)]))
