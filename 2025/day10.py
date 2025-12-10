import collections
import heapq
import itertools
import math
import re
from z3 import *

inp = open(re.search(r"day\d\d", __file__)[0] + 'input.txt').read().strip()


def solve(target, buttons):
    steps = 0
    n = len(target)
    states = set()
    states.add((0,) * n)
    while True:
        steps += 1
        new_states = set()
        for state in states:
            for button in buttons:
                new_states.add(tuple(
                    (state[i] + (i in button)) % 2 for i in range(n)))
        if target in new_states:
            return steps
        states = new_states

def solvej(buttons, joltages):
    n = len(buttons)
    cmd = '''s = Optimize()\n'''
    for i in range(n):
        cmd += f'''p{i} = Int('p{i}')\n'''
    cmd += '''presses = Int('presses')\n'''
    for t in range(len(joltages)):
        cmd += 's.add(' + ' + '.join(f'p{i}' for i in range(n) if t in buttons[i]) + f' == {joltages[t]})\n'
    for i in range(n):
        cmd += f's.add(p{i} >= 0)\n'
    cmd += 's.add(presses == ' + ' + '.join(f'p{i}' for i in range(n)) + ')\n'
    cmd += 's.minimize(presses)\n'
    cmd += '''if s.check() == sat:
    m = s.model()
    ans = m[presses].as_long()'''
    # print(cmd)
    my_locals = {}
    ans = None
    exec(cmd, globals(), my_locals)
    return my_locals['ans']

part1 = part2 = 0
for line in inp.splitlines():
    target, rest = line[1:-1].split('] ')
    buttons_str, joltage_str = rest.split(' {')
    target = tuple(c == '#' for c in target)
    buttons = []
    for button_str in buttons_str.split(' '):
        buttons.append(set(map(int, button_str[1:-1].split(','))))
    part1 += solve(target, buttons)
    joltages = tuple(map(int, joltage_str.split(',')))
    # print(buttons, joltages)
    part2 += solvej(buttons, joltages)
print(part1)
print(part2)
