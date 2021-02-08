import collections
import copy
import itertools
import math
import re

inp = open(re.match(r"day\d\d", __file__)[0] + 'input.txt').read().strip()

registers = collections.defaultdict(int)
part2 = 0
for command in inp.splitlines():
  reg, incdec, amount, cond = re.match(
      r'([a-z]+) (inc|dec) ([-]?\d+) if (.+)', command).group(1, 2, 3, 4)
  registers[cond.split()[0]] += 0
  # We need to make a copy of registers for eval, because eval adds
  # values to the global scope.
  if eval(cond, copy.copy(registers)):
    registers[reg] += int(amount) if incdec == 'inc' else -int(amount)
  part2 = max(part2, max(registers.values()))

print('part1:', max(registers.values()))
print('part2:', part2)
