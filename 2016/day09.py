import collections
import itertools
import math
import re

inp = open(re.match(r"day\d\d", __file__)[0] + 'input.txt').read().strip()

pos = 0
output = []
while pos < len(inp):
  if inp[pos] != '(':
    output.append(inp[pos])
    pos += 1
  else:
    close_pos = inp.find(')', pos)
    size, reps = [int(n) for n in re.findall(r'\d+', inp[pos:close_pos])]
    output.append(inp[close_pos + 1:close_pos + 1 + size] * reps)
    pos = close_pos + 1 + size
print('part1:', sum(len(s) for s in output))

def get_len(s):
  open_pos = s.find('(')
  if open_pos == -1:
    return len(s)
  close_pos = s.find(')', open_pos)
  size, reps = [int(n) for n in re.findall(r'\d+', s[open_pos:close_pos])]
  return (open_pos
    + get_len(s[close_pos + 1:close_pos + 1 + size]) * reps
    + get_len(s[close_pos+1+size:])
  )

print('part2:', get_len(inp))
