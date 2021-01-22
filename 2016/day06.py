import collections
import itertools
import math
import re

inp = open(re.match(r"day\d\d", __file__)[0] + 'input.txt').read().strip()

lines = inp.splitlines()

def most_freq_letter(pos, lines):
  freq = collections.defaultdict(int)
  for line in lines:
    freq[line[pos]] += 1
  max_freq = max(list(freq.values()))
  for c, f in freq.items():
    if f == max_freq:
      return c

def least_freq_letter(pos, lines):
  freq = collections.defaultdict(int)
  for line in lines:
    freq[line[pos]] += 1
  min_freq = min(list(freq.values()))
  for c, f in freq.items():
    if f == min_freq:
      return c

part1 = ''
part2 = ''
for i in range(len(lines[0])):
  part1 += most_freq_letter(i, lines)
  part2 += least_freq_letter(i, lines)
print('part1:', part1)
print('part2:', part2)
