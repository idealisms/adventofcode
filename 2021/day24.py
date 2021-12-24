import collections
import copy
import itertools
import math
import re

inp = open(re.search(r"day\d\d", __file__)[0] + 'input.txt').read().strip()

command_blocks = inp.split('\ninp w\n')
assert len(command_blocks) == 14

INP, ADD, MUL, DIV, MOD, EQL = list(range(6))
CMD_NAMES = {
    'inp': INP,
    'add': ADD,
    'mul': MUL,
    'div': DIV,
    'mod': MOD,
    'eql': EQL,
}

cmds = []
for lines in command_blocks:
    cmd_lines = []
    for line in lines.splitlines():
        cmd = line.split(' ')
        cmd[0] = CMD_NAMES[cmd[0]]
        if len(cmd) == 3:
            cmd[2] = cmd[2] if cmd[2] in 'wxyz' else int(cmd[2])
        cmd_lines.append(cmd)
    cmds.append(cmd_lines)

def get_value(vars, st):
    return vars.get(st, st)

def run_commands(vars, cmds):
    for cmd in cmds:
        if cmd[0] == INP:
            continue
        elif cmd[0] == ADD:
            vars[cmd[1]] += get_value(vars, cmd[2])
        elif cmd[0] == MUL:
            vars[cmd[1]] *= get_value(vars, cmd[2])
        elif cmd[0] == DIV:
            b = get_value(vars, cmd[2])
            if b == 0:
                vars['z'] = -1
                break
            vars[cmd[1]] = math.trunc(vars[cmd[1]] / b)
        elif cmd[0] == MOD:
            a = vars[cmd[1]]
            b = get_value(vars, cmd[2])
            if a < 0 or b <= 0:
                vars['z'] = -1
                break
            vars[cmd[1]] %= b
        elif cmd[0] == EQL:
            vars[cmd[1]] = 1 if vars[cmd[1]] == get_value(vars, cmd[2]) else 0
        else:
            raise Exception
    return vars

BIG_INT = int(1e15)
max_zs = {0: 0}
min_zs = {0: 0}
for i, cmd_block in enumerate(cmds[:13]):
    new_max_zs = collections.defaultdict(int)
    new_min_zs = collections.defaultdict(int)
    for startZ, max_n in max_zs.items():
        min_n = min_zs[startZ]
        for w in range(1, 10):
            vars = collections.defaultdict(int)
            vars['w'] = w
            vars['z'] = startZ
            z = run_commands(vars, cmd_block)['z']
            new_max_zs[z] = max(new_max_zs[z], max_n*10 + w)
            new_min_zs[z] = min(new_min_zs.get(z, BIG_INT), min_n*10 + w)
    max_zs = new_max_zs
    min_zs = new_min_zs
    print(i, len(max_zs))

def part1(max_zs):
    possible = reversed(sorted([(n, z) for z, n in max_zs.items()]))
    for n, z in possible:
        for w in range(9, 0, -1):
            vars = collections.defaultdict(int)
            vars['w'] = w
            vars['z'] = z
            if 0 == run_commands(vars, cmds[-1])['z']:
                print(str(n) + str(w))
                return

def part2(min_zs):
    possible = sorted([(n, z) for z, n in min_zs.items()])
    for n, z in possible:
        for w in range(1, 10):
            vars = collections.defaultdict(int)
            vars['w'] = w
            vars['z'] = z
            if 0 == run_commands(vars, cmds[-1])['z']:
                print(str(n) + str(w))
                return

part1(max_zs) # 93997999296912
part2(min_zs) # 81111379141811
