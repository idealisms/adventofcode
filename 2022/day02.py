import collections
import itertools
import math
import re

inp = open(re.search(r"day\d\d", __file__)[0] + 'input.txt').read().strip()
# inp = """A Y
# B X
# C Z"""
#nums = list(map(int, inp.splitlines()))
part1 = 0
part2 = 0
for line in inp.splitlines():
    opp = {'A': 0, 'B': 1, 'C': 2}[line[0]]
    me = {'X': 0, 'Y': 1, 'Z': 2}[line[2]]
    part1 += me + 1
    if opp == me: # draw
        part1 += 3
    elif opp == (me + 1) % 3: # lose
        part1 += 0
    elif opp == (me + 2) % 3: # win
        part1 += 6
    if me == 0: # lose
        part2 += (opp + 2) % 3 + 1
    elif me == 1: # draw
        part2 += (opp % 3) + 1 + 3
    elif me == 2: # win
        part2 += (opp + 1) % 3 + 1 + 6

print(part1)
print(part2)
