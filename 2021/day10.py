import collections
import itertools
import math
import re

inp = open(re.match(r"day\d\d", __file__)[0] + 'input.txt').read().strip()

points = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}

matching = {
    ')': '(',
    ']': '[',
    '}': '{',
    '>': '<',
}

incomplete_pts = {
    '(': 1,
    '[': 2,
    '{': 3,
    '<': 4,
}
part1 = 0
part2 = []
for line in inp.splitlines():
    stack = []

    for c in line:
        if c in '([{<':
            stack.append(c)
        elif len(stack) == 0 or matching[c] != stack[-1]:
            part1 += points[c]
            stack = []
            break
        else:
            stack = stack[:-1]

    if stack:
        score = 0
        for c in reversed(stack):
            score = score * 5 + incomplete_pts[c]
        part2.append(score)
print(part1)
print(sorted(part2)[len(part2) // 2])
