import collections
import itertools
import math
import re

inp = open(re.match(r"day\d\d", __file__)[0] + 'input.txt').read().strip()
lines = inp.splitlines()
# lines = """""
# "abc"
# "aaa\\"aaa"
# "\\x27"\
# """.splitlines()

total = 0
for line in lines:
  s = eval(line)
  total += len(line) - len(s)
print('part1:', total)

total = 0
for line in lines:
  total += (
      line.count('\\')
      + line.count('"')
      + 2  # For the opening and closing double quotes
      )
print('part2:', total)

