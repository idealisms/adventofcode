import collections
import itertools
import math
import re

inp = open(re.match(r"day\d\d", __file__)[0] + 'input.txt').read().strip()
instructions = inp.splitlines()
# instructions = '''cpy 2 a
# tgl a
# tgl a
# tgl a
# cpy 1 a
# dec a
# dec a'''.splitlines()
# instructions = '''cpy b c
# inc a
# dec c
# jnz c -2
# dec d
# jnz d -5'''.splitlines()


def run(regs):
  pc = 0
  while True:
    if pc >= len(instructions):
      break
    # print(pc, instructions[pc])
    inst = instructions[pc]
    if inst.startswith('inc '):
      regs[inst[4]] += 1
      pc += 1
    elif inst.startswith('dec '):
      regs[inst[4]] -= 1
      pc += 1
    elif inst.startswith('cpy '):
      # Second optimization found by printing commands as they were run.
      # This makes the first optimization unnecessary.
      # This set of commands is a += b * d
      if (inst == 'cpy b c' and instructions[pc+1:pc+6] == [
          'inc a', 'dec c', 'jnz c -2', 'dec d', 'jnz d -5']):
        regs['a'] += regs['b'] * regs['d']
        regs['c'] = regs['d'] = 0
        pc += 6
        continue

      _, source, dest = inst.split(' ')
      value = regs[source] if source in 'abcd' else int(source)
      if dest in 'abcd':
        regs[dest] = value
      pc += 1
    elif inst.startswith('jnz '):
      _, test, offset = inst.split(' ')
      offset = regs[offset] if offset in 'abcd' else int(offset)
      value = regs[test] if test in 'abcd' else int(test)
      # First optimization found by printing commands as they were run.
      # if offset == -2 and instructions[pc - 1] == 'dec c' and instructions[pc - 2] == 'inc a':
      #   regs['a'] += value
      #   regs['c'] = value = 0
      if value != 0:
        pc += offset
      else:
        pc += 1
    elif inst.startswith('tgl '):
      _, offset = inst.split(' ')
      instruction_location = pc + regs[offset]
      if 0 <= instruction_location < len(instructions):
        inst_to_change = instructions[instruction_location]
        if inst_to_change[:3] == 'inc':
          instructions[instruction_location] = 'dec' + inst_to_change[3:]
        elif inst_to_change[:3] in ('dec', 'tgl'):
          instructions[instruction_location] = 'inc' + inst_to_change[3:]
        elif inst_to_change[:3] == 'jnz':
          instructions[instruction_location] = 'cpy' + inst_to_change[3:]
        else:
          instructions[instruction_location] = 'jnz' + inst_to_change[3:]
      pc += 1

  return regs['a']

print('part1:', run(dict(a=7, b=0, c=0, d=0)))
instructions = inp.splitlines()
print('part2:', run(dict(a=12, b=0, c=0, d=0)))
