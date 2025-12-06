import collections
import heapq
import itertools
import math
import re

inp = open(re.search(r"day\d\d", __file__)[0] + 'input.txt').read()
lines = []
for line in inp.splitlines():
    lines.append(line.split())
R = len(lines)
C = len(lines[0])
for i in range(R - 1):
    lines[i] = map(int, lines[i])

lines = list(zip(*lines))

part1 = 0
for c in range(C):
    if lines[c][-1] == '*':
        part1 += math.prod(lines[c][:-1])
    else:
        part1 += sum(lines[c][:-1])
print(part1)

lines = inp.splitlines()
R = len(lines)
C = len(lines[0])

def read_num(c):
    s = ''
    for r in range(R - 1):
        s += lines[r][c]
    s = s.rstrip()
    if s == '':
        return
    return int(s)

part2 = 0
c = 0
while c < C:
    op = lines[-1][c]
    values = []
    n = read_num(c)
    while n is not None:
        values.append(n)
        c += 1
        if c == C:
            break
        n = read_num(c)
    if op == '*':
        part2 += math.prod(values)
    else:
        part2 += sum(values)
    c += 1
print(part2)
