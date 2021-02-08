import collections
import itertools
import math
import re

inp = open(re.match(r"day\d\d", __file__)[0] + 'input.txt').read().strip()

weights = {}
parent_edges = {}
children_edges = {}  # string -> set()
for line in inp.splitlines():
  parts = line.split(' -> ')
  name, weight = re.match(r'([a-z]+) [(](\d+)[)]', parts[0]).group(1, 2)
  weights[name] = int(weight)
  if len(parts) > 1:
    children = set(parts[1].split(', '))
    children_edges[name] = children
    for child in children:
      parent_edges[child] = name

part1 = list(weights.keys())[0]
while part1 in parent_edges:
  part1 = parent_edges[part1]
print('part1:', part1)

mem = {}
def compute_weight(node):
  if node in mem:
    return mem[node]

  weight = weights[node]
  for child in children_edges.get(node, []):
    weight += compute_weight(child)
  mem[node] = weight
  return weight

def find_unbalanced(node):
  if node not in children_edges:
    return []
  children = children_edges[node]
  unbalanced = []
  child_weights = [compute_weight(child) for child in children]
  if not all(weight == child_weights[0] for weight in child_weights):
    unbalanced.append(node)
  for child in children:
    unbalanced = unbalanced + find_unbalanced(child)
  return unbalanced

root = part1
# Find all nodes that are unbalanced.
unbalanced = find_unbalanced(root)
# The last unbalanced node (leaf node) is the one we want to fix.
unbalanced_weights = [(compute_weight(child), child) for child in children_edges[unbalanced[-1]]]

# Figure out which weight is the incorrect weight.
freq = collections.defaultdict(int)
for weight, _ in unbalanced_weights:
  freq[weight] += 1

for weight, f in freq.items():
  if f != 1:
    target_weight = weight
  else:
    node_to_fix_weight = weight

# Determine how much the weight is off by.
offset = target_weight - node_to_fix_weight
# Apply the offset to the node that has the wrong weight.
for weight, node in unbalanced_weights:
  if node_to_fix_weight == weight:
    print('part2:', weights[node] + offset)
