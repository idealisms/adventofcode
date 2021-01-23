import collections
import itertools
import math
import re

inp = open(re.match(r"day\d\d", __file__)[0] + 'input.txt').read().strip()

def has_abba(s):
  mo = re.search(r'(.)(.)\2\1', s)
  return mo and mo.group(0)[0] != mo.group(0)[1]

part1 = 0
for line in inp.splitlines():
  in_brackets = re.findall(r'\[[a-z]+\]', line)
  if any([has_abba(in_bracket) for in_bracket in in_brackets]):
    continue
  without_hypernet = re.sub(r'\[[a-z]+\]', '[]', line)
  if has_abba(without_hypernet):
    part1 += 1
print('part1:', part1)

# Didn't use a regex for this because it could be overlapping.
def find_abas(s):
  abas = set()
  for i in range(len(s) - 2):
    a, b, c = s[i:i+3]
    if a not in '[]' and a == c and b != a:
      abas.add(a+b+c)
  return abas

part2 = 0
for line in inp.splitlines():
  in_brackets = re.findall(r'\[[a-z]+\]', line)
  without_hypernet = re.sub(r'\[[a-z]+\]', '[]', line)
  abas = find_abas(without_hypernet)
  for aba in abas:
    bab = aba[1] + aba[0] + aba[1]
    if any([bab in in_bracket for in_bracket in in_brackets]):
      part2 += 1
      break
print('part2:', part2)
