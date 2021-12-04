import collections
import itertools
import math
import re

inp = open(re.match(r"day\d\d", __file__)[0] + 'input.txt').read().strip()
lines = inp.splitlines()
# lines = '''7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

# 22 13 17 11  0
#  8  2 23  4 24
# 21  9 14 16  7
#  6 10  3 18  5
#  1 12 20 15 19

#  3 15  0  2 22
#  9 18 13 17  5
# 19  8  7 25 23
# 20 11 10 24  4
# 14 21 16 12  6

# 14 21 17 24  4
# 10 16 15  9 19
# 18  8 23 26 20
# 22 11 13  6  5
#  2  0 12  3  7'''.splitlines()
numbers = list(map(int, lines[0].split(',')))

boards = []
lines = lines[2:]
board = []
for line in lines:
    if line == '':
        boards.append(board)
        board = []
    else:
        board.append(list(map(int, line.split())))
boards.append(board)
# print(boards[0])
# print(len(boards))

def findWinningBoard(boards):
    for board in boards:
        for row in board:
            if row.count('X') == 5:
                return board
        cols = zip(*board)
        for col in cols:
            if col.count('X') == 5:
                return board

part1 = None
lastWinningBoard = None
lastNumber = None
for number in numbers:
    # print(number, len(boards))
    if len(boards) == 0:
        break
    for board in boards:
        for row in board:
            for i, n in enumerate(row):
                if row[i] == number:
                    row[i] = 'X'
    winningBoard = findWinningBoard(boards)
    while winningBoard:
        if not part1:
            sumUnmarked = 0
            for row in winningBoard:
                for n in row:
                    if n != 'X':
                        sumUnmarked += n
            # print(sumUnmarked, number)
            part1 = sumUnmarked * number
            print(part1)
        boards.remove(winningBoard)
        lastWinningBoard = winningBoard
        lastNumber = number
        winningBoard = findWinningBoard(boards)

# print(lastWinningBoard)
sumUnmarked = 0
for row in lastWinningBoard:
    for n in row:
        if n != 'X':
            sumUnmarked += n
# print(sumUnmarked, lastNumber)
part2 = sumUnmarked * lastNumber
print(part2)
