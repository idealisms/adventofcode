import collections
import itertools
import math
import re

inp = open(re.match(r"day\d\d", __file__)[0] + 'input.txt').read().strip()

# Coordinate as a complex number. x-axis is real part,
# y-axis is imaginary part.
pos = 0+0j
right_turn = -1j
left_turn = 1j
direction = 1j

seen = set()
twice = None
for instruction in inp.split(', '):
  direction *= right_turn if instruction[0] == 'R' else left_turn
  for _ in range(int(instruction[1:])):
    pos += direction
    if twice is None and pos in seen:
      twice = pos
    seen.add(pos)
print('part1:', int(abs(pos.real) + abs(pos.imag)))
print('part2:', int(abs(twice.real) + abs(twice.imag)))

# Original solution.
# N, E, S, W = range(4)
# offset = [
#   1j,
#   1,
#   -1j,
#   -1,
# ]
#
# direction = N
# pos = 0+0j
# seen = set()
# twice = None
# for instruction in inp.split(', '):
#   direction += 1 if instruction[0] == 'R' else -1
#   for _ in range(int(instruction[1:])):
#     pos += offset[direction % 4]
#     if twice is None and pos in seen:
#       twice = pos
#     seen.add(pos)

# print('part1:', int(abs(pos.real) + abs(pos.imag)))
# print('part2:', int(abs(twice.real) + abs(twice.imag)))
