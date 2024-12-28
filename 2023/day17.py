import collections
import heapq
import itertools
import math
import re

inp = open(re.search(r"day\d\d", __file__)[0] + 'input.txt').read().strip()
# inp = '''2413432311323
# 3215453535623
# 3255245654254
# 3446585845452
# 4546657867536
# 1438598798454
# 4457876987766
# 3637877979653
# 4654967986887
# 4564679986453
# 1224686865563
# 2546548887735
# 4322674655533'''


grid = inp.splitlines()
R = len(grid)
C = len(grid[0])
E, S, W, N = range(4)
deltas = [
    (0, 1),
    (1, 0),
    (0, -1),
    (-1, 0),
]
INF = 1000000000
# node id: (r, c, dir, cnt)
start = (0, 0, S, 0)
q = [(0, start)]
dists = collections.defaultdict(lambda: INF)
while len(q) > 0:
    cur_dist, cur_node = heapq.heappop(q)
    if cur_dist > dists[cur_node]:
        continue

    r, c, d, cnt = cur_node
    for dd in range(4):
        dr, dc = deltas[dd]
        if dd == d and cnt == 3:
            continue
        if dd == (d + 2) % 4:
            continue
        nr, nc = r+dr, c+dc
        if nr < 0 or nr >= R or nc < 0 or nc >= C:
            continue
        dist = cur_dist + int(grid[nr][nc])
        next_node = (nr, nc, dd, 1 if dd != d else cnt + 1)
        if dist < dists[next_node]:
            dists[next_node] = dist
            heapq.heappush(q, (dist, next_node))

part1 = INF
for d in range(4):
    for cnt in range(1, 4):
        part1 = min(part1, dists[(R-1, C-1, d, cnt)])
print(part1)

# Two possible start directions.
q = [(0, (0, 0, S, 0)), (0, (0, 0, E, 0))]
dists = collections.defaultdict(lambda: INF)
while len(q) > 0:
    cur_dist, cur_node = heapq.heappop(q)
    if cur_dist > dists[cur_node]:
        continue

    r, c, d, cnt = cur_node
    for dd in range(4):
        dr, dc = deltas[dd]
        if dd == d and cnt == 10:
            continue
        if dd == (d + 2) % 4:
            continue
        if dd in ((d + 1) % 4, (d + 3) % 4) and cnt < 4:
            continue
        nr, nc = r+dr, c+dc
        if nr < 0 or nr >= R or nc < 0 or nc >= C:
            continue
        dist = cur_dist + int(grid[nr][nc])
        next_node = (nr, nc, dd, 1 if dd != d else cnt + 1)
        if dist < dists[next_node]:
            dists[next_node] = dist
            heapq.heappush(q, (dist, next_node))

part2 = INF
for d in range(4):
    for cnt in range(4, 11):
        part2 = min(part2, dists[(R-1, C-1, d, cnt)])
print(part2)
