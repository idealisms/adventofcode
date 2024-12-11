import collections
import itertools
import math
import re

inp = open(re.search(r"day\d\d", __file__)[0] + 'input.txt').read().strip()
start = list(map(int, inp.split()))

stones = start[:]
for i in range(25):
    new_stones = []
    for n in stones:
        if n == 0:
            new_stones.append(1)
        elif len(str(n)) % 2 == 0:
            ss = str(n)
            new_stones.append(int(ss[:len(ss) // 2]))
            new_stones.append(int(ss[len(ss) // 2:]))
        else:
            new_stones.append(n * 2024)
    stones = new_stones
print(len(stones))

mem = {}
def count_stones(n, steps):
    # print(n, steps)
    if (n, steps) in mem:
        return mem[(n, steps)]

    if steps == 1:
        if n == 0:
            return 1
        elif len(str(n)) % 2 == 0:
            return 2
        else:
            return 1

    res = -1
    if n == 0:
        res = count_stones(1, steps - 1)
    elif len(str(n)) % 2 == 0:
        ss = str(n)
        res = (
            count_stones(int(ss[:len(ss) // 2]), steps - 1 ) +
            count_stones(int(ss[len(ss) // 2:]), steps - 1))
    else:
        res = count_stones(n * 2024, steps - 1)
    mem[(n, steps)] = res
    return res

part2 = 0
for n in start:
    part2 += count_stones(n, 75)
print(part2)
