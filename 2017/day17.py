import collections
import itertools
import math
import re

inp = open(re.match(r"day\d\d", __file__)[0] + 'input.txt').read().strip()
steps = int(inp)

q = collections.deque([0])
for n in range(1, 2018):
  q.rotate(-steps - 1)
  q.appendleft(n)

q.rotate(-q.index(2017) - 1)
print('part1:', q.popleft())

q = collections.deque([0])
for n in range(1, 50000000):
  q.rotate(-steps - 1)
  q.appendleft(n)

q.rotate(-q.index(0) - 1)
print('part2:', q.popleft())
