import collections
import itertools
import math
import re

inp = open(re.match(r"day\d\d", __file__)[0] + 'input.txt').read().strip()
containers = [int(n) for n in inp.splitlines()]

TARGET = 150
# Test case
# TARGET = 25
# containers = [5, 5, 10, 15, 20]

ways = [0] * (TARGET + 1)
for container in containers:
  new_ways = [n for n in ways]
  new_ways[container] += 1
  for i in range((TARGET + 1) - container):
    if ways[i] > 0:
      new_ways[i + container] += ways[i]
  ways = new_ways
print('part1:', ways[TARGET])

# [num ways][num containers]
num_containers = len(containers)
ways = [[0] * num_containers for _ in range(TARGET + 1)]
for container in containers:
  new_ways = [[n for n in row] for row in ways]
  new_ways[container][1] += 1
  for i in range((TARGET + 1) - container):
    for j in range(num_containers):
      if ways[i][j] > 0:
        new_ways[i + container][j + 1] += ways[i][j]
  ways = new_ways
for j in range(num_containers):
  if ways[TARGET][j] > 0:
    print('min containers:', j)
    print('part2:', ways[TARGET][j])
    break
