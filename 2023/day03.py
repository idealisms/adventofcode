import collections
import itertools
import math
import re

inp = open(re.search(r"day\d\d", __file__)[0] + 'input.txt').read().strip()
# inp = '''467..114..
# ...*....5.
# ..35..633.
# ......#...
# 617*......
# .....+.58.
# ..592.....
# ......755.
# ...$.*....
# .664.598..'''

# inp = '''.....
# .....
# .5.+.
# .....
# .....'''

board = inp.splitlines()

# ((row, col), number_string)
nums = []
for r, row in enumerate(board):
    for mo in re.finditer(r'\d+', row):
        nums.append(((r, mo.start()), mo[0]))

# (row, col) => [number_strs]
symbol_nums = collections.defaultdict(list)
part1 = 0
for (row, col), num_str in nums:
    found = False
    for r in range(row-1, row+2):
        for c in range(col-1, col+len(num_str) + 1):
            if 0 <= r < len(board) and 0 <= c < len(board[0]):
                if board[r][c] in '.0123456789':
                    continue
                if not found:
                    found = True
                    # print(row, col, num_str, board[r][c], r, c)
                    part1 += int(num_str)
                if board[r][c] == '*':
                    symbol_nums[(r, c)].append(num_str)
print(part1)

part2 = 0
for lst in symbol_nums.values():
    if len(lst) == 2:
        part2 += int(lst[0]) * int(lst[1])
print(part2)
