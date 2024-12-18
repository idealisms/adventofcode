import collections
import itertools
import math
import re
import heapq

inp = open(re.search(r"day\d\d", __file__)[0] + 'input.txt').read().strip()
X = Y = 70
SIZE = 1024
INF = 999999999

pts = []
for line in inp.splitlines():
    x, y = map(int, re.findall(r'\d+', line))
    pts.append((x, y))

def calculate_distances(graph, starting_vertex):
    distances = {vertex: INF for vertex in graph}
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
                heapq.heappush(pq, (distance, neighbor))

    return distances

def solve(walls):
    graph = collections.defaultdict(dict)
    for x in range(X+1):
        for y in range(Y+1):
            if x > 0 and (x-1, y) not in walls:
                graph[(x, y)][(x-1, y)] = 1
            if x+1 <= X and (x+1, y) not in walls:
                graph[(x, y)][(x+1, y)] = 1
            if y > 0 and (x, y-1) not in walls:
                graph[(x, y)][(x, y-1)] = 1
            if y+1 <= Y and (x, y+1) not in walls:
                graph[(x, y)][(x, y+1)] = 1

    distances = calculate_distances(graph, (0, 0))
    if distances[(X, Y)] == INF:
        print('%d,%d' % pts[len(walls)-1])
        return -1
    # print(size, distances[(X, Y)])
    return distances[(X, Y)]

walls = set(pts[:SIZE])
part1 = solve(walls)
print(part1)

for s in range(SIZE, len(pts)):
    walls.add(pts[s])
    if solve(walls) == -1:
        break
