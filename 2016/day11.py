import collections
import itertools
import math
import re

inp = open(re.match(r"day\d\d", __file__)[0] + 'input.txt').read().strip()
# inp = '''The first floor contains a hydrogen-compatible microchip and a lithium-compatible microchip.
# The second floor contains a hydrogen generator.
# The third floor contains a lithium generator.
# The fourth floor contains nothing relevant.'''

# inp = '''The first floor contains a polonium generator, a promethium generator.
# The second floor contains a polonium-compatible microchip and a promethium-compatible microchip.
# The third floor contains nothing relevant.
# The fourth floor contains nothing relevant.'''
# 11

# inp = '''The first floor contains a polonium generator, a thulium generator, a thulium-compatible microchip, a promethium generator.
# The second floor contains a polonium-compatible microchip and a promethium-compatible microchip.
# The third floor contains nothing relevant.
# The fourth floor contains nothing relevant.'''
# 23

# inp = '''The first floor contains a polonium generator, a thulium generator, a thulium-compatible microchip, a promethium generator, a ruthenium generator, a ruthenium-compatible microchip.
# The second floor contains a polonium-compatible microchip and a promethium-compatible microchip.
# The third floor contains nothing relevant.
# The fourth floor contains nothing relevant.'''
# 35

# part1: 47
# part2: part1 + 12 + 12

floors = []
for line in inp.splitlines():
  floors.append(set((g[0][:2], g[2][0]) for g in  re.findall('a (\w+)(-compatible)? (generator|microchip)', line)))
# print(floors)

def is_valid_floor(floor):
  has_generators = any(item[1] == 'g' for item in floor)
  for element, type_ in floor:
    if type_ == 'm' and has_generators and (element, 'g') not in floor:
      return False
  return True

# assert is_valid_floor(set())
# assert is_valid_floor(set([('h', 'm')]))
# assert is_valid_floor(set([('h', 'g')]))
# assert is_valid_floor([('h', 'm'), ('l', 'm')])
# assert is_valid_floor([('h', 'g'), ('l', 'g')])
# assert is_valid_floor([('h', 'm'), ('h', 'g')])
# assert is_valid_floor([('h', 'm'), ('h', 'g'), ('l', 'g')])
# assert not is_valid_floor([('h', 'm'), ('h', 'g'), ('l', 'm')])
# assert is_valid_floor([('h', 'm'), ('h', 'g'), ('l', 'g'), ('l', 'm')])

def gen_elevator_payloads(floor):
  for item in floor:
    yield (item,)
  for items in itertools.combinations(floor, 2):
    yield items

part1 = None
floors = tuple(tuple(sorted(floor)) for floor in floors)
key = (0, floors)
seen = set([key])

# BFS of all combinations. Keep track of what we've seen to avoid
# going in circles.
queue = [(key, 0)]
while True:
  key, steps = queue.pop(0)
  elevator_floor, floors = key
  if elevator_floor == 3 and len(floors[3]) == sum(len(floor) for floor in floors):
    part1 = steps
    break

  moves = []
  for items, elevator_delta in itertools.product(gen_elevator_payloads(floors[elevator_floor]), (-1, 1)):
    new_elevator_floor = elevator_floor + elevator_delta
    if new_elevator_floor < 0 or new_elevator_floor > 3:
      continue

    new_floor = tuple(sorted(set(floors[elevator_floor]).difference(items)))
    if is_valid_floor(new_floor):
      new_floors = list(floors)
      new_floors[elevator_floor] = new_floor
      new_floors[new_elevator_floor] = tuple(sorted(floors[new_elevator_floor] + items))
      new_key = (new_elevator_floor, tuple(new_floors))
      if is_valid_floor(new_floors[new_elevator_floor]) and new_key not in seen:
        moves.append(new_key)

  seen.update(moves)
  for move in moves:
    queue.append((move, steps + 1))

print('part1:', part1)
print('part2:', part1 + 12 + 12)
