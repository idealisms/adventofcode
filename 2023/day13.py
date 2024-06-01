import collections
import itertools
import math
import re

inp = open(re.search(r"day\d\d", __file__)[0] + 'input.txt').read().strip()
# inp = """#.##..##.
# ..#.##.#.
# ##......#
# ##......#
# ..#.##.#.
# ..##..##.
# #.#.##.#.
# #...##..#
# #....#..#
# ..##..###
# #####.##.
# #####.##.
# ..##..###
# #....#..#"""
# inp = """##..#######..
# .#.####.#.#..
# .#.#..#..##.#
# ...#..#.##.#.
# #.#..#....##.
# #.#..#....##.
# ...#..#.##.#.
# .#.#..#..##.#
# .#.##.#.#.#..
# ##..#######..
# #.#.##.#.....
# #.....###..#.
# ###.....###.#
# ###.....###.#
# #.....###..#.
# #.#.##.#.....
# ##..#######.."""
# inp = """#..####.##.##
# .##.##.####.#
# #######.##.##
# ####.........
# #..##..####..
# ....##.#..#.#
# .##..#.####.#
# ....#.#....#.
# .....##....##
# .##.##.#..#.#
# #..##..#..#..
# ####.######.#
# .....#.####.#
# .##.##......#
# #..##........"""
maps = [m.split('\n') for m in inp.split('\n\n')]

def find_horizontal(m, exclude=-1):
    num_rows = len(m)
    for r, row in enumerate(m[:-1]):
        if r == exclude - 1:
            continue
        if row == m[r + 1]:
            steps = max(0, min(num_rows - (r + 2), r))
            # print(r, steps)
            is_mirror = True
            for offset in range(1, steps + 1):
                # print(' ', offset)
                if m[r - offset] != m[r + 1 + offset]:
                    is_mirror = False
                    break
            if is_mirror:
                return r + 1
    return -1

def find_split(m):
    rows_above = find_horizontal(m)
    if rows_above == -1:
        rows_above = find_horizontal([''.join(r) for r in zip(*m)])
    else:
        rows_above *= 100
    return rows_above

part1 = 0
for m in maps:
    part1 += find_split(m)
print(part1)

def diff_chars(r1, r2):
    num_diff = 0
    for c1, c2 in zip(r1, r2):
        if c1 != c2:
            num_diff += 1
    return num_diff

def find_part2_horizontal_score(m):
    part1_score = find_horizontal(m)
    for r, row in enumerate(m):
        for r2 in range(r+1, len(m), 2):
            # print(r, r2, diff_chars(row, m[r2]))
            if diff_chars(row, m[r2]) == 1:
                # print(part1_score, r, r2)
                # print(row)
                # print(m[r2])
                # print()
                m_copy = m[:]
                m_copy[r] = m[r2]
                score = find_horizontal(m_copy, part1_score)
                if score == -1:
                    m_copy = m[:]
                    m_copy[r2] = m[r]
                    score = find_horizontal(m_copy, part1_score)
                if score != -1:
                    return score
    return -1

def find_part2_score(m):
    score = find_part2_horizontal_score(m)
    if score != -1:
        return score * 100
    score = find_part2_horizontal_score([''.join(r) for r in zip(*m)])
    if score == -1:
        print('\n'.join(m))
        print()
        print('\n'.join([''.join(r) for r in zip(*m)]))
        print(find_split(m))
        raise
    return score

part2 = 0
for m in maps:
    part2 += find_part2_score(m)
print(part2)
