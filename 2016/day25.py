import collections
import itertools
import math
import re

inp = open(re.match(r"day\d\d", __file__)[0] + 'input.txt').read().strip()
instructions = inp.splitlines()

def run(regs):
  pc = 0
  seen = set()  # Used to detect infinite loops.
  out = []
  while True:
    if pc >= len(instructions):
      break
    key = (pc, tuple(regs[x] for x in 'abcd'))
    if key in seen:
      break
    seen.add(key)

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
    elif inst.startswith('out '):
      out.append(regs[inst[4]])
      pc += 1
  return out

for a in itertools.count(1):
  out = run(dict(a=a, b=0, c=0, d=0))
  print(a, out)
  if len(out) > 0 and len(out) % 2 == 0 and all((True if value == i % 2 else False for i, value in enumerate(out))):
    print('part1:', a)
    break
