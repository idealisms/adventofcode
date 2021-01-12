import collections
import itertools
import math
import re

inp = open(re.match(r"day\d\d", __file__)[0] + 'input.txt').read().strip()

aunt_props = {}
for line in inp.splitlines():
  aunt_id = re.match(r'Sue (\d+)', line).group(1)
  d = {}
  for prop, count in re.findall(r'([a-z]+): (\d+)', line):
    d[prop] = int(count)
  aunt_props[aunt_id] = d

target_description = '''children: 3
cats: 7
samoyeds: 2
pomeranians: 3
akitas: 0
vizslas: 0
goldfish: 5
trees: 3
cars: 2
perfumes: 1'''.splitlines()

target_props = {}
for line in target_description:
  prop, count = line.split(': ')
  target_props[prop] = int(count)

for aunt_id, props in aunt_props.items():
  if all(target_props[prop] == props[prop] for prop in props.keys()):
    print('part1:', aunt_id)

for aunt_id, props in aunt_props.items():
  is_valid = True
  for prop in props.keys():
    if prop in ('cats', 'trees'):
      if target_props[prop] >= props[prop]:
        is_valid = False
    elif prop in ('pomeranians', 'goldfish'):
      if target_props[prop] <= props[prop]:
        is_valid = False
    else:
      if target_props[prop] != props[prop]:
        is_valid = False
  if is_valid:
    print('part2:', aunt_id)
