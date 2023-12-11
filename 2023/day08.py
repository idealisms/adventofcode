import collections
import itertools
import math
import re

inp = open(re.search(r"day\d\d", __file__)[0] + 'input.txt').read().strip()
lines = inp.splitlines()
steps = lines[0]

# node -> (left, right)
tree = {}
for line in lines[2:]:
    node, left, right = re.findall(r'[A-Z]+', line)
    tree[node] = (left, right)

def count_steps(start_node, is_part_1):
    cur_node = start_node
    seen_at_step = collections.defaultdict(int)
    cycles = []
    for i in range(99999999):
        direction = steps[i % len(steps)]
        cur_node = tree[cur_node][0 if direction == 'L' else 1]
        if cur_node == 'ZZZ' and is_part_1:
            return i+1
        if not is_part_1 and cur_node[2] == 'Z':
            if cur_node not in seen_at_step:
                seen_at_step[cur_node] = i
            else:
                if seen_at_step[cur_node] != -1:
                    cycles.append((
                        cur_node, 
                        seen_at_step[cur_node] + 1,
                        i - seen_at_step[cur_node]))
                    seen_at_step[cur_node] = -1
                else:
                    if list(seen_at_step.values()).count(-1) == len(seen_at_step.values()):
                        return cycles

print(count_steps('AAA', is_part_1=True))

cycles = []
for node in tree.keys():
    if node[2] == 'A':
        node_cycles = count_steps(node, is_part_1=False)
        print(node, node_cycles)
        cycles.extend(node_cycles)

def gcd(x, y):
   while(y):
       x, y = y, x % y
   return x

def lcm(x, y):
   lcm = (x*y)//gcd(x,y)
   return lcm

part2 = lcm(cycles[0][2], cycles[1][2])
for cycle in cycles[2:]:
    part2 = lcm(part2, cycle[2])
print(part2)
