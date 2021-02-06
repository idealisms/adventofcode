import collections
import itertools
import math
import re

inp = open(re.match(r"day\d\d", __file__)[0] + 'input.txt').read().strip()

instructions = [int(n) for n in inp.splitlines()]
pc = 0
part1 = None
for steps in itertools.count():
  if pc < 0 or pc >= len(instructions):
    part1 = steps
    break
  instructions[pc] += 1
  pc += instructions[pc] - 1
print('part1:', part1)

instructions = [int(n) for n in inp.splitlines()]
pc = 0
part2 = None
for steps in itertools.count():
  if pc < 0 or pc >= len(instructions):
    part2 = steps
    break
  offset = instructions[pc]
  instructions[pc] += -1 if offset >= 3 else 1
  pc += offset
print('part2:', part2)
