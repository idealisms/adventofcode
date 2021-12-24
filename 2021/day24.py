import collections
import copy
import itertools
import math
import re

inp = open(re.search(r"day\d\d", __file__)[0] + 'input.txt').read().strip()

command_blocks = inp.split('\ninp w\n')
assert len(command_blocks) == 14

cmds = []
for lines in command_blocks:
    cmd_lines = []
    for line in lines.splitlines():
        cmd_lines.append(line.split(' '))
    cmds.append(cmd_lines)

def getValue(vars, st):
    if st in 'wxyz':
        return vars[st]
    return int(st)

def runCommands(vars, cmds):
    for cmd in cmds:
        if cmd[0] == 'inp':
            continue
        elif cmd[0] == 'add':
            vars[cmd[1]] += getValue(vars, cmd[2])
        elif cmd[0] == 'mul':
            vars[cmd[1]] *= getValue(vars, cmd[2])
        elif cmd[0] == 'div':
            b = getValue(vars, cmd[2])
            if b == 0:
                vars['z'] = -1
                break
            vars[cmd[1]] = math.trunc(vars[cmd[1]] / b)
        elif cmd[0] == 'mod':
            a = vars[cmd[1]]
            b = getValue(vars, cmd[2])
            if a < 0 or b <= 0:
                vars['z'] = -1
                break
            vars[cmd[1]] %= b
        elif cmd[0] == 'eql':
            vars[cmd[1]] = 1 if vars[cmd[1]] == getValue(vars, cmd[2]) else 0
        else:
            raise Exception
    return vars

def part1():
    bestZs = {0: 0}
    for i, cmdBlock in enumerate(cmds[:13]):
        newBestZs = collections.defaultdict(int)
        for startZ, n in bestZs.items():
            for w in range(1, 10):
                vars = collections.defaultdict(int)
                vars['w'] = w
                vars['z'] = startZ
                z = runCommands(vars, cmdBlock)['z']
                newBestZs[z] = max(newBestZs[z], n*10 + w)
        bestZs = newBestZs
        print(i, len(bestZs))

    possible = reversed(sorted([(n, z) for z, n in bestZs.items()]))

    for n, z in possible:
        for w in range(9, 0, -1):
            vars = collections.defaultdict(int)
            vars['w'] = w
            vars['z'] = z
            if 0 == runCommands(vars, cmds[-1])['z']:
                print(str(n) + str(w))
                return

def part2():
    bestZs = {0: 0}
    for i, cmdBlock in enumerate(cmds[:13]):
        newBestZs = {}
        for startZ, n in bestZs.items():
            for w in range(1, 10):
                vars = collections.defaultdict(int)
                vars['w'] = w
                vars['z'] = startZ
                z = runCommands(vars, cmdBlock)['z']
                newBestZs[z] = min(newBestZs.get(z, int(1e15)), n*10 + w)
        bestZs = newBestZs
        print(i, len(bestZs))

    possible = reversed(sorted([(n, z) for z, n in bestZs.items()]))

    possible = sorted(possible)
    for n, z in possible:
        for w in range(1, 10):
            vars = collections.defaultdict(int)
            vars['w'] = w
            vars['z'] = z
            if 0 == runCommands(vars, cmds[-1])['z']:
                print(str(n) + str(w))
                return

# part1() # 93997999296912
part2() # 81111379141811
