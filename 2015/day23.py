import collections
import itertools
import math
import re

inp = open(re.match(r"day\d\d", __file__)[0] + 'input.txt').read().strip()
lines = inp.splitlines()
a, b = 0, 0

def run(a, b):
  pc = 0
  while True:
    if pc >= len(lines):
      break

    line = lines[pc]
    cmd = line[:3]
    args = line[4:].split(', ')

    if cmd == 'hlf':
      if args[0] == 'a':
        a //= 2
      else:
        b //= 2
      pc += 1
    elif cmd == 'tpl':
      if args[0] == 'a':
        a *= 3
      else:
        b *= 3
      pc += 1
    elif cmd == 'inc':
      if args[0] == 'a':
        a += 1
      else:
        b += 1
      pc += 1
    elif cmd == 'jmp':
      pc += int(args[0])
    elif cmd == 'jie':
      if ((args[0] == 'a' and a % 2 == 0) or
          (args[0] == 'b' and b % 2 == 0)):
        pc += int(args[1])
      else:
        pc += 1
    elif cmd == 'jio':
      if ((args[0] == 'a' and a == 1) or
          (args[0] == 'b' and b == 1)):
        pc += int(args[1])
      else:
        pc += 1
  return a, b

print('part1:', run(0, 0)[1])
print('part2:', run(1, 0)[1])
