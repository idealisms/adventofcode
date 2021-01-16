import collections
import itertools
import math
import re

inp = open(re.match(r"day\d\d", __file__)[0] + 'input.txt').read().strip()
enemy_hp, enemy_damage, enemy_armor = [int(n) for n in re.findall(r'\d+', inp, re.M)]

player_hp = 100

# Weapons:    Cost  Damage  Armor
WEAPONS = '''Dagger        8     4       0
Shortsword   10     5       0
Warhammer    25     6       0
Longsword    40     7       0
Greataxe     74     8       0'''
weapons = []
for line in WEAPONS.splitlines():
  weapons.append([int(n) for n in re.findall(r'\d+', line)])

# Armor:      Cost  Damage  Armor
ARMORS = '''Leather      13     0       1
Chainmail    31     0       2
Splintmail   53     0       3
Bandedmail   75     0       4
Platemail   102     0       5'''
armors = []
for line in ARMORS.splitlines():
  armors.append([int(n) for n in re.findall(r'\d+', line)])
armors.append([0, 0, 0]) # Armor is optional

# Rings:      Cost  Damage  Armor
RINGS = '''Damage +1    25     1       0
Damage +2    50     2       0
Damage +3   100     3       0
Defense +1   20     0       1
Defense +2   40     0       2
Defense +3   80     0       3'''
rings = []
for line in RINGS.splitlines():
  rings.append([int(n) for n in re.findall(r' \d+', line)])
rings.append([0, 0, 0]) # Can have 0-2 rings.
rings.append([0, 0, 0])

def player_wins_combat(
    player_damage, player_armor, player_hp,
    enemy_damage, enemy_armor, enemy_hp):
  while True:
    enemy_hp -= max(1, player_damage - enemy_armor)
    if enemy_hp <= 0:
      return True
    player_hp -= max(1, enemy_damage - player_armor)
    if player_hp <= 0:
      return False

best = 100000
for items in itertools.product(weapons, armors, itertools.combinations(rings, 2)):
  items = items[:2] + items[2]
  player_damage = sum(list(zip(*items))[1])
  player_armor = sum(list(zip(*items))[2])

  if player_wins_combat(
      player_damage, player_armor, player_hp,
      enemy_damage, enemy_armor, enemy_hp):
    cost = sum(list(zip(*items))[0])
    best = min(cost, best)

print('part1:', best)

best = 0
for items in itertools.product(weapons, armors, itertools.combinations(rings, 2)):
  items = items[:2] + items[2]
  player_damage = sum(list(zip(*items))[1])
  player_armor = sum(list(zip(*items))[2])

  if not player_wins_combat(
      player_damage, player_armor, player_hp,
      enemy_damage, enemy_armor, enemy_hp):
    cost = sum(list(zip(*items))[0])
    best = max(cost, best)

print('part2:', best)