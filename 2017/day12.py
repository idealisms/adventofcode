import collections
import itertools
import math
import re

inp = open(re.match(r"day\d\d", __file__)[0] + 'input.txt').read().strip()

edges = {}
for line in inp.splitlines():
  nums = [int(n) for n in re.findall(r'\d+', line)]
  edges[nums[0]] = set(nums[1:])

group0 = set()
queue = [0]
while len(queue):
  node = queue.pop(0)
  if node in group0:
    continue
  group0.add(node)
  queue.extend(list(edges[node]))
print('part1:', len(group0))

num_groups = 0
unallocated = set(edges.keys())
while len(unallocated):
  num_groups += 1
  seen = set()
  queue = [min(unallocated)]  # Pick any node to start.
  while len(queue):
    node = queue.pop(0)
    if node in seen:
      continue
    seen.add(node)
    queue.extend(list(edges[node]))
  unallocated = unallocated - seen

print('part2:', num_groups)
