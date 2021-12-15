import collections
import itertools
import math
import re
import functools
import heapq

inp = open(re.search(r"day\d\d", __file__)[0] + 'input.txt').read().strip()

# inp='''1163751742
# 1381373672
# 2136511328
# 3694931569
# 7463417111
# 1319128137
# 1359912421
# 3125421639
# 1293138521
# 2311944581'''

grid = inp.splitlines()

source = (0, 0)
rows = len(grid)
cols = len(grid[0])
target = (rows - 1, cols - 1)

def dijkstras(grid):
    rows = len(grid)
    cols = len(grid[0])

    q = []
    seen = set()
    dist = collections.defaultdict(int)
    prev = collections.defaultdict(int)

    for r in range(rows):
        for c in range(cols):
            v = (r, c)
            dist[v] = 0 if v == source else 999999
            prev[v] = None
    heapq.heappush(q, (dist[source], source))

    while q:
        _, u = heapq.heappop(q)
        seen.add(u)

        for v in [(u[0] - 1, u[1]),
                (u[0] + 1, u[1]),
                (u[0], u[1] - 1),
                (u[0], u[1] + 1)]:
            if 0 <= v[0] < rows and 0 <= v[1] < cols:
                alt = dist[u] + int(grid[v[0]][v[1]])
                if alt < dist[v]:
                    dist[v] = alt
                    prev[v] = u
                    if v not in seen:
                        heapq.heappush(q, (alt, v))

    print(dist[(rows-1, cols-1)])
    # node = (rows-1, cols-1)
    # while node != (0, 0):
    #     print(node)
    #     node = prev[node]

dijkstras(grid)


grid2 = []
for step in range(5):
    for row in grid:
        row2 = ''
        for c in row:
            n = int(c) + step
            n = n if n <= 9 else n - 9
            row2 += str(n)
        grid2.append(row2)

for r, row in enumerate(grid2):
    new_row = ''
    for step in range(5):
        for c in row:
            n = int(c) + step
            n = n if n <= 9 else n - 9
            new_row += str(n)
    grid2[r] = new_row

dijkstras(grid2)
