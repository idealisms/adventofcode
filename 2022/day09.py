import collections
import itertools
import math
import re

inp = open(re.search(r"day\d\d", __file__)[0] + 'input.txt').read().strip()
inpx = '''R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2'''

pos = [(0, 0) for _ in range(10)]
part1 = {pos[1]}
part2 = {pos[-1]}
dx = {
    'U': 0,
    'D': 0,
    'L': -1,
    'R': 1,
}
dy = {
    'U': 1,
    'D': -1,
    'L': 0,
    'R': 0,
}

def move_knot(h, t):
    ht_dx = abs(h[0] - t[0])
    ht_dy = abs(h[1] - t[1])
    if ht_dx <= 1 and ht_dy <= 1:
        return t
    if ht_dx == 2 and ht_dy == 2:
        return ((t[0] + h[0]) // 2, (t[1] + h[1]) // 2)
    if ht_dx == 2:
        return ((t[0] + h[0]) // 2, h[1])
    return (h[0], (t[1] + h[1]) // 2)
    
for move in inp.splitlines():
    d, n = move.split()
    for _ in range(int(n)):
        pos[0] = (pos[0][0] + dx[d], pos[0][1] + dy[d])
        for i in range(9):
            pos[i+1] = move_knot(pos[i], pos[i+1])
        part1.add(pos[1])
        part2.add(pos[-1])
print(len(part1))
print(pos)
print(len(part2))