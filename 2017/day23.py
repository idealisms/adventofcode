import collections
import itertools
import math
import re

inp = open(re.match(r"day\d\d", __file__)[0] + 'input.txt').read().strip()

commands = []
for line in inp.splitlines():
  commands.append(line.split())

def run(registers):
  def get_value(s):
    try:
      return int(s)
    except:
      return registers[s]

  pc = 0
  num_muls = 0
  for count in itertools.count():
    if pc >= len(commands):
      break
    command = commands[pc]
    # print(pc, command, registers)
    if command[0] == 'set':
      registers[command[1]] = get_value(command[2])
      pc += 1
    elif command[0] == 'sub':
      registers[command[1]] -= get_value(command[2])
      pc += 1
    elif command[0] == 'mul':
      registers[command[1]] *= get_value(command[2])
      num_muls += 1
      pc += 1
    elif command[0] == 'jnz':
      if get_value(command[1]) != 0:
        pc += get_value(command[2])
      else:
        pc += 1
  return num_muls

registers = collections.defaultdict(int)
print('part1:', run(registers))

#                     a=1
#  0 set b 65         b=65
#  1 set c b          c=65
#  2 jnz a 2          goto: 4
#  3 jnz 1 5
#  4 mul b 100        b=6500
#  5 sub b -100000    b=106500
#  6 set c b          c=106500
#  7 sub c -17000     c=123500
#  8 set f 1          f=1
#  9 set d 2          d=2
# 10 set e 2          e=2
# 11 set g d
# 12 mul g e
# 13 sub g b
# 14 jnz g 2          if d * e == b:
# 15 set f 0            f = 0
# 16 sub e -1         e += 1
# 17 set g e
# 18 sub g b          if e - b != 0
# 19 jnz g -8           goto: 11
# 20 sub d -1         d += 1
# 21 set g d
# 22 sub g b          if d != b:
# 23 jnz g -13          goto: 10
# 24 jnz f 2          if f == 0:
# 25 sub h -1           h += 1
# 26 set g b
# 27 sub g c
# 28 jnz g 2          if b == c:
# 29 jnz 1 3            exit
# 30 sub b -17        b += 17
# 31 jnz 1 -23        goto: 8
#
# Becomes:
#
# for b in range(106500, c + 1, 17):
#   f = 1
#   for d in range(2, b + 1):
#     for e in range(2, b + 1):
#       if d * e == b:
#         f = 0
#   if f == 0:
#     h += 1
#
# Becomes:

b = 106500
c = 123500
h = 0
def is_prime(n):
  for f in range(2, int(math.sqrt(n)) + 1):
    if n % f == 0:
      return False
  return True

for b in range(106500, c + 1, 17):
  if not is_prime(b):
    h += 1
print('part2:', h)
