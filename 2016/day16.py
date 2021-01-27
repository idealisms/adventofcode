import collections
import itertools
import math
import re

data = open(re.match(r"day\d\d", __file__)[0] + 'input.txt').read().strip()

def gen_random_data(a):
  b = reversed(a)
  return a + '0' + ''.join('0' if d == '1' else '1' for d in b)

def get_checksum(s):
  checksum = []
  for i in range(len(s) // 2):
    if s[i * 2] == s[i * 2 + 1]:
      checksum.append('1')
    else:
      checksum.append('0')
  return ''.join(checksum)

def solve(data, disk_length):
  while len(data) < disk_length:
    data = gen_random_data(data)

  checksum = data[:disk_length]
  while True:
    checksum = get_checksum(checksum)
    if len(checksum) % 2 == 1:
      return checksum

print('part1:', solve(data, 272))
print('part2:', solve(data, 35651584))
