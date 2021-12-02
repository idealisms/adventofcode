import collections
import itertools
import math
import re

inp = open(re.match(r"day\d\d", __file__)[0] + 'input.txt').read().strip()
d = 0
x = 0
for line in inp.splitlines():
    inst, n = line.split(' ')
    if inst == 'forward':
        x += int(n)
    elif inst == 'up':
        d -= int(n)
    else:
        d += int(n)
print(d*x)

d = 0
x = 0
aim = 0
for line in inp.splitlines():
    inst, n = line.split(' ')
    if inst == 'forward':
        x += int(n)
        d += aim * int(n)
    elif inst == 'up':
        aim -= int(n)
    else:
        aim += int(n)
print(d*x)

