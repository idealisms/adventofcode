import collections
import itertools
import math
import re

inp = open(re.match(r"day\d\d", __file__)[0] + 'input.txt').read().strip()

def hash(lengths, rounds=1):
  lst = list(range(256))
  # lst = list(range(5))
  # inp = '3,4,1,5'

  offset = 0
  skip_size = 0
  for _ in range(rounds):
    for length in lengths:
      lst = lst[length:] + list(reversed(lst[:length]))
      lst = lst[skip_size:] + lst[:skip_size]
      offset = (offset + length + skip_size) % len(lst)
      skip_size = (skip_size + 1) % len(lst)
  return lst[-offset:] + lst[:-offset]

part1 = hash([int(n) for n in inp.split(',')])
print('part1:', part1[0] * part1[1])

import functools
import operator
def xor(lst):
  return functools.reduce(operator.xor, lst[1:], lst[0])

def knot_hash(s):
  lengths = [ord(c) for c in s] + [17, 31, 73, 47, 23]
  lst = hash(lengths, 64)
  decimal = [xor(lst[i*16:(i+1)*16]) for i in range(16)]
  return ''.join(f'{n:02x}' for n in decimal)

# print(knot_hash(''))
# print(knot_hash('AoC 2017'))
print('part2:', knot_hash(inp))
