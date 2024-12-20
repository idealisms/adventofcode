import collections
import heapq
import itertools
import math
import re

inp = open(re.search(r"day\d\d", __file__)[0] + 'input.txt').read().strip()
grid = []
for row in inp.splitlines():
    grid.append(list(row))
R = len(grid)
C = len(grid[0])
for r in range(R):
    for c in range(C):
        if grid[r][c] == 'S':
            sr, sc = r, c
            grid[r][c] = '.'
        if grid[r][c] == 'E':
            er, ec = r, c
            grid[r][c] = '.'
graph = collections.defaultdict(dict)
for r in range(R):
    for c in range(C):
        if grid[r][c] == '.':
            if grid[r-1][c] == '.':
                graph[(r, c)][(r-1, c)] = 1
            if grid[r+1][c] == '.':
                graph[(r, c)][(r+1, c)] = 1
            if grid[r][c-1] == '.':
                graph[(r, c)][(r, c-1)] = 1
            if grid[r][c+1] == '.':
                graph[(r, c)][(r, c+1)] = 1

#nums = list(map(int, inp.splitlines()))

def calculate_distances(graph, starting_vertex):
    distances = {vertex: 999999999 for vertex in graph}
    prev = {vertex: None for vertex in graph}
    distances[starting_vertex] = 0

    pq = [(0, starting_vertex)]
    while len(pq) > 0:
        current_distance, current_vertex = heapq.heappop(pq)

        # Nodes can get added to the priority queue multiple times. We only
        # process a vertex the first time we remove it from the priority queue.
        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            # Only consider this new path if it's better than any path we've
            # already found.
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                prev[neighbor] = current_vertex
                heapq.heappush(pq, (distance, neighbor))

    return distances, prev

distances, prev = calculate_distances(graph, (sr, sc))
# print(distances[(er, ec)])

steps = {}
d = distances[(er, ec)]
r, c = er, ec
while (r, c) != (sr, sc):
    # print(d, r, c)
    steps[(r, c)] = d
    d -= 1
    r, c = prev[(r, c)]
steps[(sr, sc)] = 0

r, c = er, ec
part1 = 0
while prev[(r, c)] is not None:
    r, c = prev[(r, c)]
    if grid[r+1][c] == '#' and steps.get((r+2, c), 0) - steps[(r, c)] >= 102:
        part1 += 1
    if grid[r-1][c] == '#' and steps.get((r-2, c), 0) - steps[(r, c)] >= 102:
        part1 += 1
    if grid[r][c+1] == '#' and steps.get((r, c+2), 0) - steps[(r, c)] >= 102:
        part1 += 1
    if grid[r][c-1] == '#' and steps.get((r, c-2), 0) - steps[(r, c)] >= 102:
        part1 += 1
print(part1)

r, c = er, ec
part2 = 0
while prev[(r, c)] is not None:
    r, c = prev[(r, c)]
    for dr in range(-20, 21):
        for dc in range(-20, 21):
            md = abs(dr) + abs(dc)
            if md > 20:
                continue
            if (r+dr, c+dc) in steps and steps[(r+dr, c+dc)] - steps[(r, c)] >= 100 + md:
                part2 += 1
print(part2)
