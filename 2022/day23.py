import collections
import itertools
import math
import re

inp = open(re.search(r"day\d\d", __file__)[0] + 'input.txt').read().strip()
_inp = '''..............
..............
.......#......
.....###.#....
...#...#.#....
....#...##....
...#.###......
...##.#.##....
....#..#......
..............
..............
..............'''

elves = set()
for r, line in enumerate(inp.splitlines()):
    for c, ch in enumerate(line):
        if ch == '#':
            elves.add((r, c))

DIRS = [
    (-1, 0), # N
    (1, 0), # S
    (0, -1), # W
    (0, 1), # E
]
CHECKS = [
    [(-1, -1), (-1, 0), (-1, 1)],
    [(1, -1), (1, 0), (1, 1)],
    [(-1, -1), (0, -1), (1, -1)],
    [(-1, 1), (0, 1), (1, 1)],
]

def print_elves(elves):
    r_min = min(r for r, _ in elves)
    r_max = max(r for r, _ in elves)
    c_min = min(c for _, c in elves)
    c_max = max(c for _, c in elves)
    for r in range(r_min, r_max + 1):
        line = ''
        for c in range(c_min, c_max + 1):
            line += '#' if (r, c) in elves else '.'
        print(line)
    print()
            

first_dir = -1
for step in range(999999):
    # print_elves(elves)
    first_dir += 1
    proposed = collections.defaultdict(list)
    for elf in elves:
        alone = True
        for dr in (-1, 0, 1):
            for dc in (-1, 0, 1):
                if dr == dc and dr == 0:
                    continue
                if (elf[0] + dr, elf[1] + dc) in elves:
                    alone = False
                    break
        if alone:
            proposed[elf] = [elf]
            continue
        moved = False
        for i in range(4):
            checks = CHECKS[(first_dir + i) % 4]
            open = True
            for dr, dc in checks:
                if (elf[0] + dr, elf[1] + dc) in elves:
                    open = False
                    break
            # print(elf, i, open)
            if not open:
                continue
            proposed[(
                elf[0] + DIRS[(first_dir + i) % 4][0],
                elf[1] + DIRS[(first_dir + i) % 4][1])].append(elf)
            moved = True
            break
        if not moved:
            proposed[elf].append(elf)
    # print(elves)
    # print(proposed)
    # print()
    new_elves = set()
    for pos, elves_from in proposed.items():
        if len(elves_from) == 1:
            new_elves.add(pos)
        else:
            for elf in elves_from:
                new_elves.add(elf)
    if list(sorted(list(elves))) == list(sorted(list(new_elves))):
        print(step + 1)
        break
    elves = new_elves

    if step == 9:
        print(
            ((1 + max(r for r, _ in elves) - min(r for r, _ in elves)) *
            (1 + max(c for _, c in elves) - min(c for _, c in elves))) -
            len(elves))


#nums = list(map(int, inp.splitlines()))