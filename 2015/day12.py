import collections
import itertools
import json
import math
import re

inp = open(re.match(r"day\d\d", __file__)[0] + 'input.txt').read().strip()
j = json.loads(inp)

def sum_nums(node):
  if type(node) == int:
    return node
  elif type(node) == list:
    return sum(sum_nums(n) for n in node)
  elif type(node) == str:
    return 0
  elif type(node) == dict:
    return sum(sum_nums(n) for n in node.values())
  else:
    raise Exception(f'unknown node {str(type(node))}')

print('part1:', sum_nums(j))

def sum_nums(node):
  if type(node) == int:
    return node
  elif type(node) == list:
    return sum(sum_nums(n) for n in node)
  elif type(node) == str:
    return 0
  elif type(node) == dict:
    if 'red' not in node.values():
      return sum(sum_nums(n) for n in node.values())
    return 0
  else:
    raise Exception(f'unknown node {str(type(node))}')

print('part2:', sum_nums(j))
