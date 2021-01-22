import collections
import itertools
import math
import re

inp = open(re.match(r"day\d\d", __file__)[0] + 'input.txt').read().strip()

def is_valid(enc_name, checksum):
  res = []
  for i in range(26):
    res.append((0, chr(ord('a') + i)))
  for c in enc_name:
    if c == '-':
      continue
    idx = ord(c) - ord('a')
    res[idx] = (res[idx][0] + 1, res[idx][1])
  res.sort(key=lambda x: (-x[0], x[1]))
  return checksum == ''.join(p[1] for p in res[:5])

def decrypt_name(enc_name, sector_id):
  res = ''
  for c in enc_name:
    if c == '-':
      res += ' '
    else:
      res += chr((((ord(c) - ord('a')) + sector_id) % 26) + ord('a'))
  return res

part1 = 0
part2 = None
for line in inp.splitlines():
  mo = re.match(r'([-a-z]+)(\d+)[\[]([a-z]+)', line)
  enc_name, sector_id, checksum = mo.group(1), int(mo.group(2)), mo.group(3)
  if is_valid(enc_name, checksum):
    part1 += sector_id
    if 'north' in decrypt_name(enc_name, sector_id):
      part2 = sector_id
print('part1:', part1)
print('part2:', part2)
