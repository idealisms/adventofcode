import collections
import itertools
import math
import re

inp = open(re.match(r"day\d\d", __file__)[0] + 'input.txt').read().strip()
components = set()
index = collections.defaultdict(set)
for line in inp.splitlines():
  a, b = [int(n) for n in re.findall(r'\d+', line)]
  component = (min(a, b), max(a, b))
  components.add(component)
  index[a].add(component)
  index[b].add(component)

mem = {}
def solve(port, used):
  key = (port, tuple(used))
  if key in mem:
    return mem[key]

  best = sum(a + b for a, b in used)
  for component in index[port]:
    if component in used:
      continue
    new_port = component[0] if port == component[1] else component[1]
    best = max(best, solve(new_port, used.union([component])))
  mem[key] = best
  return best

print('part1:', solve(0, set()))

mem = {}
def solve2(port, used):
  key = (port, tuple(used))
  if key in mem:
    return mem[key]

  length, strength = len(used), sum(a + b for a, b in used)
  for component in index[port]:
    if component in used:
      continue
    new_port = component[0] if port == component[1] else component[1]
    other_length, other_strength = solve2(new_port, used.union([component]))
    if other_length > length or (other_length == length and other_strength > strength):
      length, strength = other_length, other_strength
  mem[key] = length, strength
  return length, strength

print('part2:', solve2(0, set())[1])
