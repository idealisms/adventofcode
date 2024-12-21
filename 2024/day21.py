import collections
import functools
import heapq
import itertools
import math
import re

inp = open(re.search(r"day\d\d", __file__)[0] + 'input.txt').read().strip()
# inp = '''029A
# 980A
# 179A
# 456A
# 379A'''


DIRS = {
    (-1, 0): '^',
    (1, 0):  'v',
    (0, -1): '<',
    (0, 1):  '>',
}

NUMPAD = [
    '789',
    '456',
    '123',
    ' 0A',
]
R = len(NUMPAD)
C = len(NUMPAD[0])
NUMPAD2POS = {}
for r in range(R):
    for c in range(C):
        NUMPAD2POS[NUMPAD[r][c]] = (r, c)

@functools.cache
def numpad_paths(start, end):
    r, c = NUMPAD2POS[start]
    for (dr, dc), d in DIRS.items():
        if (0 <= r + dr < R and 0 <= c + dc < C and
            NUMPAD[r+dr][c+dc] == end):
            return [d]

    er, ec = NUMPAD2POS[end]

    paths = []
    for (dr, dc), d in DIRS.items():
        if dr < 0 and er >= r:
            continue
        if dr > 0 and er <= r:
            continue
        if dc < 0 and ec >= c:
            continue
        if dc > 0 and ec <= c:
            continue
        if (0 <= r + dr < R and 0 <= c + dc < C and
            NUMPAD[r+dr][c+dc] != ' '):
            # print(start, end, d, paths)
            paths.extend([
                d + path for path in numpad_paths(NUMPAD[r+dr][c+dc], end)])
    min_len = min(map(len, paths))
    # print(start, end, paths, min_len)
    paths = [path for path in paths if len(path) == min_len]
    return paths
            
def solve_numpad(code):
    cur = 'A'
    paths = ['']
    for c in code:
        new_paths = []
        for p1 in paths:
            for p2 in numpad_paths(cur, c):
                new_paths.append(p1+p2+'A')
        paths = new_paths
        cur = c
    min_len = min(map(len, paths))
    return [path for path in paths if len(path) == min_len]

DIRPAD_PATHS = {
    ('^', 'A'): ['>'],
    ('^', '<'): ['v<'],
    ('^', 'v'): ['v'],
    ('^', '>'): ['>v', 'v>'],

    ('A', '^'): ['<'],
    ('A', '<'): ['<v<', 'v<<'],
    ('A', 'v'): ['v<', '<v'],
    ('A', '>'): ['v'],

    ('<', '^'): ['>^'],
    ('<', 'A'): ['>>^', '>^>'],
    ('<', 'v'): ['>'],
    ('<', '>'): ['>>'],

    ('v', '^'): ['^'],
    ('v', 'A'): ['^>', '>^'],
    ('v', '<'): ['<'],
    ('v', '>'): ['>'],

    ('>', '^'): ['<^', '^<'],
    ('>', 'A'): ['^'],
    ('>', '<'): ['<<'],
    ('>', 'v'): ['<'],
}

def solve_dirpad(keys):
    cur = 'A'
    paths = ['']
    for c in keys:
        new_paths = []
        for p1 in paths:
            for p2 in DIRPAD_PATHS.get((cur, c), ['']):
                new_paths.append(p1+p2+'A')
        paths = new_paths
        cur = c
    min_len = min(map(len, paths))
    return [path for path in paths if len(path) == min_len]

@functools.cache
def solve_dirpad2(keys, depth):
    if depth == 1:
        return len(solve_dirpad(keys)[0])
    total = 0
    cur = 'A'
    for k in keys:
        steps = []
        for p in DIRPAD_PATHS.get((cur, k), ['']):
            steps.append(solve_dirpad2(p + 'A', depth - 1))
        total += min(steps)
        cur = k
    return total

part1 = part2 = 0
for code in inp.splitlines():
    keys = solve_numpad(code)

    lens = []
    for key in keys:
        lens.append(solve_dirpad2(key, 2))
    part1 += min(lens) * int(code[:-1])

    lens = []
    for key in keys:
        lens.append(solve_dirpad2(key, 25))
    part2 += min(lens) * int(code[:-1])

print(part1)
print(part2)