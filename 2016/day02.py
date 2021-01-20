import collections
import itertools
import math
import re

inp = open(re.match(r"day\d\d", __file__)[0] + 'input.txt').read().strip()

def step(pos, steps):
  for s in steps:
    if s == 'U':
      pos = (max(0, pos[0] - 1), pos[1])
    elif s == 'D':
      pos = (min(2, pos[0] + 1), pos[1])
    elif s == 'L':
      pos = (pos[0], max(0, pos[1] - 1))
    elif s == 'R':
      pos = (pos[0], min(2, pos[1] + 1))
  return pos

# r, c
pos = (1, 1)
digits = []
for steps in inp.splitlines():
  pos = step(pos, steps)
  digits.append(str(pos[0] * 3 + pos[1] + 1))
print('part1:', ''.join(digits))

keypad_str = '''\
    1    \n\
  2 3 4  \n\
5 6 7 8 9
  A B C  \n\
    D    '''
keypad = [[c for i, c in enumerate(row) if i % 2 == 0] for row in keypad_str.splitlines()]
for row in keypad:
  row.insert(0, ' ')
  row.append(' ')
keypad.insert(0, [' '] * len(keypad[0]))
keypad.append([' '] * len(keypad[0]))

def step2(pos, steps):
  for s in steps:
    if s == 'U':
      if keypad[pos[0] - 1][pos[1]] != ' ':
        pos = (pos[0] - 1, pos[1])
    elif s == 'D':
      if keypad[pos[0] + 1][pos[1]] != ' ':
        pos = (pos[0] + 1, pos[1])
    elif s == 'L':
      if keypad[pos[0]][pos[1] - 1] != ' ':
        pos = (pos[0], pos[1] - 1)
    elif s == 'R':
      if keypad[pos[0]][pos[1] + 1] != ' ':
        pos = (pos[0], pos[1] + 1)
  return pos

pos = (3, 1)
digits = []
for steps in inp.splitlines():
  pos = step2(pos, steps)
  digits.append(keypad[pos[0]][pos[1]])
print('part2:', ''.join(digits))
