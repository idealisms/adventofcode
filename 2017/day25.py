import collections
import itertools
import math
import re

inp = open(re.match(r"day\d\d", __file__)[0] + 'input.txt').read().strip()
sections = inp.split('\n\n')
states = {}
for section in sections[1:]:
  lines = section.splitlines()
  state = lines[0][-2]
  states[state] = [
    (int(lines[2][-2]), 1 if lines[3][-6:] == 'right.' else -1, lines[4][-2]),
    (int(lines[6][-2]), 1 if lines[7][-6:] == 'right.' else -1, lines[8][-2]),
  ]

# print(states)

lines = sections[0].splitlines()
state = lines[0][-2]
steps = [int(n) for n in re.findall(r'\d+', lines[1])][0]
pos = 0
tape = collections.defaultdict(int)
for _ in range(steps):
  rules = states[state][tape[pos]]
  tape[pos] = rules[0]
  pos += rules[1]
  state = rules[2]
print(sum(tape.values()))
