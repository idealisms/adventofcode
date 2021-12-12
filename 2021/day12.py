import collections
import itertools
import math
import re

inp = open(re.search(r"day\d\d", __file__)[0] + 'input.txt').read().strip()

graph = collections.defaultdict(set)
for line in inp.splitlines():
    a, b = line.split('-')
    graph[a].add(b)
    graph[b].add(a)

def solve(cur_node, seen_nodes):
    if cur_node == 'end':
        return 1
    if cur_node.lower() == cur_node:
        seen_nodes = seen_nodes.union([cur_node])
    count = 0
    for next_node in graph[cur_node]:
        if next_node not in seen_nodes:
            count += solve(next_node, seen_nodes)
    return count

seen = set()
part1 = solve('start', seen)
print(part1)

def can_visit(node_name, seen_nodes):
    if node_name in ['start']:
        return False
    if node_name not in seen_nodes:
        return True
    if len(set(seen_nodes)) == len(seen_nodes):
        return True
    return False

def solve2(cur_node, seen_nodes):
    if cur_node == 'end':
        return 1
    if cur_node.lower() == cur_node:
        seen_nodes = seen_nodes + [cur_node]
    count = 0
    for next_node in graph[cur_node]:
        if can_visit(next_node, seen_nodes):
            count += solve2(next_node, seen_nodes)
    return count

seen = []
part2 = solve2('start', seen)
print(part2)