import collections
import itertools
import math
import re
import pprint

inp = open('day21input.txt').read().strip()

cmds = {}
for line in inp.splitlines():
    name, v = line.split(': ')
    tokens = v.split(' ')
    cmds[name] = int(tokens[0]) if len(tokens) == 1 else tokens

def solve(name):
    # if name == 'humn':
    #     print('humn')
    cmd = cmds[name]
    if type(cmd) == int:
        return cmd

    lhs = solve(cmd[0])
    rhs = solve(cmd[2])
    ans = None
    if cmd[1] == '+':
        ans = lhs + rhs
    elif cmd[1] == '-':
        ans = lhs - rhs
    elif cmd[1] == '*':
        ans = lhs * rhs
    elif cmd[1] == '/':
        ans = lhs / rhs
    return ans

print(solve('root'))

# print('l', solve(cmds['root'][0])) # has humn
# print('r', solve(cmds['root'][2])) # doesn't have humn
target = solve(cmds['root'][2])
print('target', target)
pow = 2
while True:
    n = int(math.pow(10, pow))
    cmds['humn'] = n

    if solve(cmds['root'][0]) < target:
        break
    pow += 1
lo = 0
hi = int(math.pow(10, pow))
while True:
    guess = (lo + hi) // 2
    cmds['humn'] = guess
    test = solve(cmds['root'][0])
    if test == target:
        print(guess)
        break
    if test < target:
        hi = guess
    else:
        lo = guess
