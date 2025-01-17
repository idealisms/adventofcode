import collections
import functools
import heapq
import itertools
import math
import re

inp = open(re.search(r"day\d\d", __file__)[0] + 'input.txt').read().strip()
# inp = '''#.#####################
# #.......#########...###
# #######.#########.#.###
# ###.....#.>.>.###.#.###
# ###v#####.#v#.###.#.###
# ###.>...#.#.#.....#...#
# ###v###.#.#.#########.#
# ###...#.#.#.......#...#
# #####.#.#.#######.#.###
# #.....#.#.#.......#...#
# #.#####.#.#.#########v#
# #.#...#...#...###...>.#
# #.#.#v#######v###.###v#
# #...#.>.#...>.>.#.###.#
# #####v#.#.###v#.#.###.#
# #.....#...#...#.#.#...#
# #.#########.###.#.#.###
# #...###...#...#...#.###
# ###.###.#.###v#####v###
# #...#...#.#.>.>.#.>.###
# #.###.###.#.###.#.#v###
# #.....###...###...#...#
# #####################.#'''


grid = inp.splitlines()
R = len(grid)
C = len(grid[0])
start = None
for c in range(C):
    if grid[0][c] == '.':
        start = complex(0, c)
        break

DELTAS = {
    '>': complex(0, 1),
    '<': complex(0, -1),
    'v': complex(1, 0),
    '^': complex(-1, 0),
}

def count_steps(pos):
    steps = 0
    visited = set()
    while True:
        visited.add(pos)
        for d in DELTAS.values():
            np = pos + d
            r, c = int(np.real), int(np.imag)
            if grid[r][c] == '.' and np not in visited:
                steps += 1
                pos = np
                if r == R - 1:
                    return steps, pos
                break
            elif grid[r][c] in '><^v':
                np += DELTAS[grid[r][c]]
                if np == pos:
                    continue
                return steps + 2, np

steps, fork_pos = count_steps(start)
graph = collections.defaultdict(dict)
graph[start][fork_pos] = steps
q = [fork_pos]
seen = set()
while len(q) > 0:
    pos = q.pop(0)
    for d in DELTAS.values():
        np = pos + d
        r, c = int(np.real), int(np.imag)
        if grid[r][c] == '#':
            continue
        np += DELTAS[grid[r][c]]
        if np == pos:
            continue
        steps, fork_pos = count_steps(np)
        graph[pos][fork_pos] = steps + 2
        # print(pos, fork_pos, steps + 2)
        if int(fork_pos.real) != R - 1 and fork_pos not in seen:
            q.append(fork_pos)
            seen.add(fork_pos)

@functools.cache
def max_path(pos):
    steps = 0
    for next_pos, add_steps in graph[pos].items():
        steps = max(steps, add_steps + max_path(next_pos))
    return steps
print(max_path(start))

nodeId = {}
for i, node in enumerate(sorted(graph.keys(), key=lambda n: n.real)):
    nodeId[node] = i

graph2 = collections.defaultdict(dict)

for node, dests in graph.items():
    for dest in dests:
        graph2[nodeId[node]][nodeId[dest]] = graph[node][dest]
        if int(dest.real) != R - 1:
            graph2[nodeId[dest]][nodeId[node]] = graph[node][dest]

@functools.cache
def max_path2(pos, visited):
    steps = 0
    visited = tuple(sorted(visited + (pos,)))

    for next_pos, add_steps in graph2[pos].items():
        if next_pos in visited:
            continue
        steps = max(steps, add_steps + max_path2(next_pos, visited))
    return steps

# Even with pyp3, this takes 1m7s
print(max_path2(0, tuple()))
