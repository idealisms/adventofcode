import collections
import heapq
import itertools
import math
import re

inp = open(re.search(r"day\d\d", __file__)[0] + 'input.txt').read().strip()
grid = inp.splitlines()
R = len(grid)
C = len(grid[0])
stones = set()
SR = SC = -1
for r in range(R):
    for c in range(C):
        if grid[r][c] == 'S':
            SR = r
            SC = c
        if grid[r][c] == '#':
            stones.add(complex(r, c))

deltas = (
    0+1j,
    1,
    0-1j,
    -1,
)
def num_plots(steps):
    plots = set()
    plots.add(complex(SR, SC))
    for step in range(steps):
        new_plots = set()
        for pos in plots:
            for delta in deltas:
                new_pt = pos+delta
                if complex(int(new_pt.real) % R, int(new_pt.imag) % C) not in stones:
                    new_plots.add(new_pt)
        plots = new_plots
    return plots

# part1
print(len(num_plots(64)))

# 26501365 steps
# 65 to get out of the first garden.
# 131 to traverse another garden.
# 202300 gardens in each direction.
TOTAL_STEPS = 26501365
N = (TOTAL_STEPS - 65) // R

# This is far enough to generate each type of plot needed.
plots = num_plots(65 + R + R)
counter = collections.Counter()
for pt in plots:
    counter[(math.floor(pt.real / R), math.floor(pt.imag / R))] += 1
print(counter)

ODD_TILES = counter[(0, 1)]
EVEN_TILES = counter[(0, 0)]
part2 = EVEN_TILES # Center
part2 += N * (counter[(1, -2)] +
              counter[(1, 2)] +
              counter[(-1, -2)] +
              counter[(-1, 2)])
part2 += (N - 1) * (counter[(1, -1)] +
                    counter[(1, 1)] +
                    counter[(-1, -1)] +
                    counter[(-1, 1)])
part2 += (counter[(2, 0)] +
          counter[(-2, 0)] +
          counter[(0, 2)] +
          counter[(0, -2)])

odds = 0
evens = 0
for i in range(2, N+1):
    if i % 2 == 0:
        odds += i - 1
    else:
        evens += i - 1
print(evens, odds)
part2 += 4 * (EVEN_TILES * evens + ODD_TILES * odds)
print(part2)
