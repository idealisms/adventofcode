import collections
import itertools
import math
import re

inp = open(re.match(r"day\d\d", __file__)[0] + 'input.txt').read().strip()
commands = []
for cmd in inp.split(','):
  if cmd[0] == 's':
    commands.append(('s', int(cmd[1:])))
  elif cmd[0] == 'x':
    a, b = [int(n) for n in re.findall(r'\d+', cmd)]
    commands.append(('x', a, b))
  else:
    commands.append(('p', cmd[1], cmd[3]))

def dance(order):
  for cmd in commands:
    if cmd[0] == 's':
      amount = cmd[1]
      order = order[-amount:] + order[:-amount]
    elif cmd[0] == 'x':
      a, b = cmd[1], cmd[2]
      order[a], order[b] = order[b], order[a]
    else:
      a, b = order.index(cmd[1]), order.index(cmd[2])
      order[a], order[b] = order[b], order[a]
  return order

order = [chr(ord('a') + i) for i in range(16)]
print('part1:', ''.join(dance(order)))

# It seems impossible to merge commands because
# exchange and partner depend on the current state.
# Instead, hope that the dances hit a cycle. I don't
# think it has to cycle since there are 16!
# permutations, but otherwise, I'm not sure how this
# is solveable.
order = [chr(ord('a') + i) for i in range(16)]
seen = {}
for i in itertools.count(1):
  order = dance(order)
  key = ''.join(order)
  if key in seen:
    cycle_length = i - seen[key]
    remaining_dances = (1000 * 1000 * 1000 - i) % cycle_length
    for _ in range(remaining_dances):
      order = dance(order)
    break
  seen[key] = i
print('part2:', ''.join(order))
