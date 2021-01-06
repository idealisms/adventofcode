import collections
import itertools
import math
import re

inp = open(re.match(r"day\d\d", __file__)[0] + 'input.txt').read().strip()
commands = {}
for line in inp.splitlines():
  lhs, out = line.split(' -> ')
  commands[out] = lhs.split(' ')

mem = {}
def solve(x):
  if x in mem:
    return mem[x]
  if re.match(r'\d+', x):
    return int(x)

  tokens = commands[x]
  ret = None
  if len(tokens) == 1:
    ret = solve(tokens[0])
  elif len(tokens) == 2:
    assert tokens[0] == 'NOT'
    ret = ~solve(tokens[1])
  elif len(tokens) == 3:
    if tokens[1] == 'AND':
      ret = solve(tokens[0]) & solve(tokens[2])
    elif tokens[1] == 'OR':
      ret = solve(tokens[0]) | solve(tokens[2])
    elif tokens[1] == 'LSHIFT':
      ret = solve(tokens[0]) << solve(tokens[2])
    elif tokens[1] == 'RSHIFT':
      ret = solve(tokens[0]) >> solve(tokens[2])
  assert ret != None
  mem[x] = ret
  return ret

part1 = solve('a')
print('part1:', part1)

commands['b'] = [str(part1)]
mem = {}
print('part2:', solve('a'))
