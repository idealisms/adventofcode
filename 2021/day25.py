import collections
import itertools
import math
import re

inp = open(re.search(r"day\d\d", __file__)[0] + 'input.txt').read().strip()

# inp = '''v...>>.vv>
# .vv>>.vv..
# >>.>v>...v
# >>v>>.>.v.
# v>v.vv.v..
# >.>>..v...
# .vv..>.>v.
# v.v..>>v.v
# ....v..v.>'''

board = [list(row) for row in inp.splitlines()]

rows = len(board)
cols = len(board[0])
print(board, rows, cols)
step = 1
while True:
    print(step)
    # Move east.
    new_board = []
    has_moved = False
    for row in board:
        new_row = []
        for c in range(cols):
            if row[c] == 'v':
                new_row.append('v')
            if row[c] == '>':
                if row[(c+1) % cols] == '.':
                    new_row.append('.')
                    has_moved = True
                else:
                    new_row.append('>')
            if row[c] == '.':
                if row[(c+cols-1) % cols] == '>':
                    new_row.append('>')
                else:
                    new_row.append('.')
        new_board.append(new_row)
    board = new_board
    # Move down.
    new_board = []
    for r, row in enumerate(board):
        new_row = []
        for c in range(cols):
            if row[c] == '>':
                new_row.append('>')
            if row[c] == 'v':
                if board[(r+1) % rows][c] == '.':
                    new_row.append('.')
                    has_moved = True
                else:
                    new_row.append('v')
            if row[c] == '.':
                if board[(r+rows-1) % rows][c] == 'v':
                    new_row.append('v')
                else:
                    new_row.append('.')
        new_board.append(new_row)
    board = new_board
    if not has_moved:
        break
    step += 1

print(step)
