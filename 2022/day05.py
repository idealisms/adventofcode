import collections
import itertools
import math
import re

inp = open(re.search(r"day\d\d", __file__)[0] + 'input.txt').read().rstrip()
init, moves = inp.split('\n\n')
stacks_raw = list(reversed(init.splitlines()))[1:]
num_stacks = len(stacks_raw[0].split(' '))
stacks = [[] for _ in range(num_stacks)]
for stack_raw in stacks_raw:
    for i in range(num_stacks):
        value = stack_raw[4*i + 1]
        if value != ' ':
            stacks[i].append(value)

# for move_line in moves.splitlines():
#     n, f, t = map(int, re.findall('\d+', move_line))
#     for i in range(n):
#         stacks[t-1].append(stacks[f-1].pop(-1))
# part1 = ''
# for s in stacks:
#     part1 += s[-1]
# print(part1)

for move_line in moves.splitlines():
    n, f, t = map(int, re.findall('\d+', move_line))
    stacks[t-1].extend(stacks[f-1][-n:])
    stacks[f-1] = stacks[f-1][:-n]
part2= ''
for s in stacks:
    part2 += s[-1]
print(part2)