import collections
import heapq
import itertools
import math
import re

inp = open(re.search(r"day\d\d", __file__)[0] + 'input.txt').read().strip()
# inp = '''###############
# #.......#....E#
# #.#.###.#.###.#
# #.....#.#...#.#
# #.###.#####.#.#
# #.#.#.......#.#
# #.#.#####.###.#
# #...........#.#
# ###.#.#####.#.#
# #...#.....#.#.#
# #.#.#.###.#.#.#
# #.....#...#.#.#
# #.###.#.#.#.#.#
# #S..#.....#...#
# ###############'''

grid = inp.splitlines()
R = len(grid)
C = len(grid[0])
N, E, S, W = tuple(range(4))
graph = collections.defaultdict(dict)
start = target = None
for r in range(R):
    for c in range(C):
        if grid[r][c] == 'S':
            start = (r, c, E)
        elif grid[r][c] == 'E':
            target = (r, c)
        if grid[r][c] in '.SE':
            for d in range(4):
                graph[(r, c, d)][r, c, (d + 1) % 4] = 1000
                graph[(r, c, d)][r, c, (d - 1) % 4] = 1000

            if grid[r-1][c] in '.SE':
                graph[(r, c, N)][(r-1, c, N)] = 1
            if grid[r+1][c] in '.SE':
                graph[(r, c, S)][(r+1, c, S)] = 1
            if grid[r][c-1] in '.SE':
                graph[(r, c, W)][(r, c-1, W)] = 1
            if grid[r][c+1] in '.SE':
                graph[(r, c, E)][(r, c+1, E)] = 1

# https://bradfieldcs.com/algos/graphs/dijkstras-algorithm/
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
                prev[neighbor] = [current_vertex]
                heapq.heappush(pq, (distance, neighbor))
            elif distance == distances[neighbor]:
                prev[neighbor].append(current_vertex)

    return distances, prev

# print(graph)
distances, prev = calculate_distances(graph, start)
part1 = min(
    distances[(target[0], target[1], N)],
    distances[(target[0], target[1], E)],
    distances[(target[0], target[1], S)],
    distances[(target[0], target[1], W)],
    )
print(part1)

visited = set()
for d in range(4):
    if distances[(target[0], target[1], d)] == part1:
        path = [(target[0], target[1], d)]
        while len(path) > 0:
            cur = path.pop()
            visited.add((cur[0], cur[1]))
            for pt in prev[cur]:
                if pt != start:
                    path.append(pt)
        visited.add((start[0], start[1]))
print(len(visited))
