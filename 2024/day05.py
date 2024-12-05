import collections
import itertools
import math
import re

inp = open(re.search(r"day\d\d", __file__)[0] + 'input.txt').read().strip()
# inp = '''47|53
# 97|13
# 97|61
# 97|47
# 75|29
# 61|13
# 75|53
# 29|13
# 97|29
# 53|29
# 61|53
# 97|53
# 61|29
# 47|13
# 75|47
# 97|75
# 47|61
# 75|61
# 47|29
# 75|13
# 53|13

# 75,47,61,53,29
# 97,61,53,29,13
# 75,29,13
# 75,97,47,61,53
# 61,13,29
# 97,13,75,29,47'''

graph_lines, rules = inp.split('\n\n')
graph = {} # str -> set()
for line in graph_lines.splitlines():
    left, right = line.split('|')
    graph.setdefault(left, set()).add(right)
# print(graph)

def check_order(order):
    for i, before in enumerate(order):
        for after in order[i+1:]:
            if before in graph.get(after, set()):
                return False
    return True

def update(order):
    for i, before in enumerate(order):
        for j, after in enumerate(order[i+1:]):
            if before in graph.get(after, set()):
                updated = order[:]
                j += i+1
                updated[i] = order[j]
                updated[j] = order[i]
                # print(i, j)
                # print(order)
                # print(updated)
                # print('--')
                return updated
    raise "Shouldn't be here"

def fix_order(order):
    while not check_order(order):
        order = update(order)
    return order

part1 = part2 = 0
for rule_line in rules.splitlines():
    order = rule_line.split(',')
    if check_order(order):
        part1 += int(order[len(order)//2])
    else:
        fixed_order = fix_order(order)
        part2 += int(fixed_order[len(order)//2])
print(part1)
print(part2)
