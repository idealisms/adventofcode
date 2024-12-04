import collections
import itertools
import math
import re

inp = open(re.search(r"day\d\d", __file__)[0] + 'input.txt').read().strip()
# inp = '''MMMSXXMASM
# MSAMXMSMSA
# AMXSXMAAMM
# MSAMASMSMX
# XMASAMXAMM
# XXAMMXXAMA
# SMSMSASXSS
# SAXAMASAAA
# MAMMMXMMMM
# MXMXAXMASX'''
lines = list(inp.splitlines())

# horizontal
part1 = 0
for row in lines:
    part1 += len(re.findall('XMAS', row)) + len(re.findall('SAMX', row))

# verticals
for c in range(len(lines[0])):
    line = ''
    for row in lines:
        line += row[c]
    part1 += len(re.findall('XMAS', line)) + len(re.findall('SAMX', line))

# diagonals
for r in range(3, len(lines)):
    line1 = line2 = line3 = line4 = ''
    
    for c in range(r+1):
        line1 += lines[r-c][c]
        line2 += lines[r-c][len(lines[0])-1-c]
        line3 += lines[len(lines)-1-r+c][c]
        line4 += lines[len(lines)-1-r+c][len(lines[0])-1-c]
    if r == len(lines) - 1:
        line3 = line4 = ''
    # print(line1)
    # print(line2)
    # print(line3)
    # print(line4)
    part1 += len(re.findall('XMAS', line1)) + len(re.findall('SAMX', line1))
    part1 += len(re.findall('XMAS', line2)) + len(re.findall('SAMX', line2))
    part1 += len(re.findall('XMAS', line3)) + len(re.findall('SAMX', line3))
    part1 += len(re.findall('XMAS', line4)) + len(re.findall('SAMX', line4))
print(part1)

def check(r, c, tl, tr, br, bl):
    return (lines[r][c] == tl and
        lines[r][c+2] == tr and
        lines[r+2][c] == bl and
        lines[r+2][c+2] == br and
        lines[r+1][c+1] == 'A')

def count(r, c):
    return 1 if (
            check(r, c, 'M', 'M', 'S', 'S') or
            check(r, c, 'S', 'M', 'M', 'S') or
            check(r, c, 'S', 'S', 'M', 'M') or
            check(r, c, 'M', 'S', 'S', 'M')) else 0

part2 = 0
for r in range(len(lines) - 2):
    for c in range(len(lines[0]) - 2):
        part2 += count(r, c)
print(part2)