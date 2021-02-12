import collections
import itertools
import math
import re

inp = open(re.match(r"day\d\d", __file__)[0] + 'input.txt').read().strip()

# Copied from day10.py.
def knot_hash(s):
  def hash(lengths, rounds=1):
    lst = list(range(256))
    offset = 0
    skip_size = 0
    for _ in range(rounds):
      for length in lengths:
        lst = lst[length:] + list(reversed(lst[:length]))
        lst = lst[skip_size:] + lst[:skip_size]
        offset = (offset + length + skip_size) % len(lst)
        skip_size = (skip_size + 1) % len(lst)
    return lst[-offset:] + lst[:-offset]

  import functools
  import operator
  # Fold right
  def xor(lst):
    return functools.reduce(operator.xor, lst[1:], lst[0])

  lengths = [ord(c) for c in s] + [17, 31, 73, 47, 23]
  lst = hash(lengths, 64)
  decimal = [xor(lst[i*16:(i+1)*16]) for i in range(16)]
  return ''.join(f'{n:02x}' for n in decimal)

hashes = []
for i in range(128):
  hashes.append(knot_hash(f'{inp}-{i}'))

# Format a number as binary.
print('part1:', sum(f'{int(h, 16):b}'.count('1') for h in hashes))

grid = []
for h in hashes:
  grid.append(list(f'{int(h, 16):0128b}'))

def remove(r, c):
  if grid[r][c] == '0':
    return
  grid[r][c] = '0'
  for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
    nr = r + dr
    nc = c + dc
    if 0 <= nr < 128 and 0 <= nc < 128:
      remove(nr, nc)

groups = 0
for r, row in enumerate(grid):
  for c, value in enumerate(row):
    if grid[r][c] == '1':
      groups += 1
      remove(r, c)
print('part2:', groups)
