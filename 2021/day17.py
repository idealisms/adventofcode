import collections
import itertools
import math
import re

inp = open(re.search(r"day\d\d", __file__)[0] + 'input.txt').read().strip()

x1, x2, y1, y2 = list(map(int, re.findall('\d+', inp)))
y1 = -y1
y2 = -y2

part1 = 0
valid_y_steps = []
for dy in range(-200, 200):
    start_dy = dy
    cury = 0
    maxy = 0
    valid_velocity = False
    num_steps = []
    for step in range(1, 10000):
        cury += dy
        # print('  ', step, cury)
        dy -= 1
        maxy = max(cury, maxy)
        if cury < y1:
            break
        if y1 <= cury <= y2:
            valid_velocity = True
            num_steps.append(step)
    if valid_velocity:
        valid_y_steps.append((start_dy, num_steps))
        # print(start_dy, num_steps)
        part1 = max(part1, maxy)
print(part1)

valid_x_steps = []
for dx in range(1, 500):
    start_dx = dx
    curx = 0
    valid_velocity = False
    num_steps = []
    for step in range(1, 400):
        curx += dx
        # print('  ', step, cury)
        if dx:
            dx -= 1
        if curx > x2:
            break
        if x1 <= curx <= x2:
            valid_velocity = True
            num_steps.append(step)
    if valid_velocity:
        valid_x_steps.append((start_dx, num_steps))
        # print(start_dx, num_steps)

part2 = 0
for dy, dy_steps in valid_y_steps:
    for dx, dx_steps in valid_x_steps:
        if set(dy_steps).intersection(set(dx_steps)):
            part2 += 1
print(part2)
