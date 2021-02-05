import collections
import itertools
import math
import re

inp = open(re.match(r"day\d\d", __file__)[0] + 'input.txt').read().strip()

part1 = part2 = 0
for phrase in inp.splitlines():
  words = phrase.split()
  if len(words) == len(set(words)):
    part1 += 1
  sorted_words = [''.join(sorted(word)) for word in words]
  if len(sorted_words) == len(set(sorted_words)):
    part2 += 1
print('part1:', part1)
print('part2:', part2)
