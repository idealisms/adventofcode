import collections
import itertools
import math
import re

inp = open(re.search(r"day\d\d", __file__)[0] + 'input.txt').read().strip()
# inp = '''O....#....
# O.OO#....#
# .....##...
# OO.#O....O
# .O.....O#.
# O.#..O.#.#
# ..O..#O..O
# .......O..
# #....###..
# #OO..#....'''

grid = []
for line in inp.splitlines():
    grid.append(list(c for c in line))

def tilt_north(grid):
    changed = True
    while changed:
        changed = False
        for r, row in enumerate(grid):
            if r == 0:
                continue
            for c, char in enumerate(row):
                if char == 'O':
                    if grid[r-1][c] == '.':
                        grid[r-1][c] = 'O'
                        grid[r][c] = '.'
                        changed = True
    return grid

def calc_load(grid):
    load = 0
    for r, row in enumerate(grid):
        load += row.count('O') * (len(grid) - r)
    return load
part1 = calc_load(tilt_north(grid))
print(part1)

def rotate_clockwise(grid):
    new_grid = []
    for c in range(len(grid[0])):
        new_row = []
        for r in range(len(grid)):
            new_row.append(grid[len(grid) - 1 - r][c])
        new_grid.append(new_row)
    return new_grid

def spin_cycle(grid):
    for _ in range(4):
        grid = tilt_north(grid)
        grid = rotate_clockwise(grid)
    return grid

# reset for part2
grid = []
for line in inp.splitlines():
    grid.append(list(c for c in line))

loads = []
for i in range(1000000000):
    grid = spin_cycle(grid)
    load = calc_load(grid)
    print(i, load)
    if loads.count(load) > 3:
        break
    loads.append(load)


# 146 89855
# 147 89878
# 148 89887
# 149 89896
# 150 89900
# 151 89880
# 152 89873
# 153 89849
# 154 89813
# 155 89800
# 156 89795
# 157 89799
# 158 89819
# 159 89845
# 160 89851
# 161 89873
# 162 89896
# 163 89892
# 164 89895
# 165 89889
# 166 89869
# 167 89844
# 168 89822
# 169 89796
# 170 89790
# 171 89808
# 172 89815
# 173 89840
# 174 89860
# 175 89869
# 176 89891
# 177 89901
# 178 89891
# 179 89884
# 180 89878
# 181 89840
# 182 89817
# 183 89805
# 184 89786
# 185 89803
# 186 89824
# 187 89836
# 188 89855
# 189 89878

# cycle length = 188 - 146 = 42
# (1000000000 - (146 + 1)) % 42 = 13
part2 = loads[146+13]
print(part2)