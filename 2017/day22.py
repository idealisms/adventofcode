import collections
import itertools
import math
import re

inp = open(re.match(r"day\d\d", __file__)[0] + 'input.txt').read().strip()
# inp = '''..#
# #..
# ...'''
lines = inp.splitlines()

infected = set()
for r, line in enumerate(lines):
  for c, value in enumerate(line):
    if value == '#':
      infected.add(complex(c, r))

pos = complex(len(lines) // 2, len(lines[0]) // 2)
# U, R, D, L = range(4)
cdir = 0

part1 = 0
for _ in range(10000):
  cdir += 1 if pos in infected else -1
  if pos in infected:
    infected.remove(pos)
  else:
    part1 += 1
    infected.add(pos)
  pos += {
    0: -1j,
    1: 1,
    2: 1j,
    3: -1,
  }[cdir % 4]

print('part1:', part1)

CLEAN, WEAKENED, INFECTED, FLAGGED = range(4)
state = collections.defaultdict(int)
for r, line in enumerate(lines):
  for c, value in enumerate(line):
    if value == '#':
      state[complex(c, r)] = INFECTED

pos = complex(len(lines) // 2, len(lines[0]) // 2)
# U, R, D, L = range(4)
cdir = 0

part2 = 0
# for _ in range(100):
for _ in range(10000000):
  node_state = state[pos]
  if node_state == CLEAN:
    cdir -= 1
  elif node_state == WEAKENED:
    part2 += 1
  elif node_state == INFECTED:
    cdir += 1
  else:
    cdir += 2

  state[pos] = (node_state + 1) % 4
  pos += {
    0: -1j,
    1: 1,
    2: 1j,
    3: -1,
  }[cdir % 4]
print('part2:', part2)
