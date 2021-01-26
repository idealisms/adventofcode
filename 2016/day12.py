import collections
import itertools
import math
import re

inp = open(re.match(r"day\d\d", __file__)[0] + 'input.txt').read().strip()

instructions = inp.splitlines()

def run(regs):
  pc = 0
  while True:
    if pc >= len(instructions):
      break
    inst = instructions[pc]
    if inst.startswith('inc '):
      regs[inst[4]] += 1
      pc += 1
    elif inst.startswith('dec '):
      regs[inst[4]] -= 1
      pc += 1
    elif inst.startswith('cpy '):
      _, source, dest = inst.split(' ')
      value = regs[source] if source in 'abcd' else int(source)
      regs[dest] = value
      pc += 1
    elif inst.startswith('jnz '):
      _, test, offset = inst.split(' ')
      offset = int(offset)
      value = regs[test] if test in 'abcd' else int(test)
      if value != 0:
        pc += offset
      else:
        pc += 1
  return regs['a']

print('part1:', run(dict(a=0, b=0, c=0, d=0)))
print('part2:', run(dict(a=0, b=0, c=1, d=0)))
