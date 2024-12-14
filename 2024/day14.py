import collections
import itertools
import math
import re

inp = open(re.search(r"day\d\d", __file__)[0] + 'input.txt').read().strip()
X = 101
Y = 103

# X = 11
# Y = 7
# inp = '''p=0,4 v=3,-3
# p=6,3 v=-1,-3
# p=10,3 v=-1,2
# p=2,0 v=2,-1
# p=0,0 v=1,3
# p=3,0 v=-2,-2
# p=7,6 v=-1,-3
# p=3,0 v=-1,-2
# p=9,3 v=2,3
# p=7,3 v=-1,2
# p=2,4 v=2,-3
# p=9,5 v=-3,-3
# '''

q = [0, 0, 0, 0]
for line in inp.splitlines():
    x, y, dx, dy = map(int, re.findall(r'[-]?\d+', line))
    nx = (x + dx * 100) % X
    ny = (y + dy * 100) % Y
    print(x, y, dx, dy, nx, ny)
    if nx < X // 2 and ny < Y // 2:
        q[0] += 1
    elif nx > X // 2 and ny < Y // 2:
        q[1] += 1
    elif nx < X // 2 and ny > Y // 2:
        q[2] += 1
    elif nx > X // 2 and ny > Y // 2:
        q[3] += 1
print(math.prod(q))

pts = []
for line in inp.splitlines():
    pts.append(list(map(int, re.findall(r'[-]?\d+', line))))

# Algorithm:
# - Print every second until I see it.
# - After about 1000s, I haven't seen the tree. But I have seen points start
#   to cluster. They are clustering every 101s with an offset of 7s.
# - Restart and only print 7s + 101s * x.
# - Stop when I see the tree.
# I was thrown off for a bit because I was using the unicode christmas tree and
# a blank space. The tree is wider than a space so my tree looked a bit skewed.
s = 8086
while True:
    s += 1
    grid = [['⬛'] * 103 for _ in range(103)]
    for i, pt in enumerate(pts):
        x = (pt[0] + s * pt[2]) % X
        y = (pt[1] + s * pt[3]) % Y
        grid[y][x] = '🎄'

    for row in grid:
        print(''.join(row))
    print(s)
    _ = input()
