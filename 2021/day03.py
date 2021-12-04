import collections
import itertools
import math
import re

inp = open(re.match(r"day\d\d", __file__)[0] + 'input.txt').read().strip()
# inp = '''00100
# 11110
# 10110
# 10111
# 10101
# 01111
# 00111
# 11100
# 10000
# 11001
# 00010
# 01010'''

lines = inp.splitlines()
def countOnesInColumns(numbers):
    columns = zip(*numbers)
    ones = list(map(lambda col: col.count('1'), columns))
    return ones

ones = countOnesInColumns(lines)
gamma = ''
epsilon = ''
for cnt in ones:
    if cnt > len(lines) / 2:
        gamma += '1'
        epsilon += '0'
    else:
        gamma += '0'
        epsilon += '1'
part1 = int(gamma, 2) * int(epsilon, 2)
print(part1)

def filter_numbers(numbers, column, is_oxygen):
    ones = countOnesInColumns(numbers)
    ret = []
    if is_oxygen:
        for number in numbers:
            if ((ones[column] > len(numbers) / 2 and number[column] == '1')
                or (ones[column] < len(numbers) / 2 and number[column] == '0')
                or (ones[column] == len(numbers) / 2 and number[column] == '1')):
                ret.append(number)
    else:
        for number in numbers:
            if ((ones[column] > len(numbers) / 2 and number[column] == '0')
                or (ones[column] < len(numbers) / 2 and number[column] == '1')
                or (ones[column] == len(numbers) / 2 and number[column] == '0')):
                ret.append(number)
    return ret


possible = lines[:]
column = 0
while len(possible) > 1:
    possible = filter_numbers(possible, column, is_oxygen=True)
    column += 1
oxygen_rating = possible[0]

possible = lines[:]
column = 0
while len(possible) > 1:
    possible = filter_numbers(possible, column, is_oxygen=False)
    column += 1
co2_rating = possible[0]
print(int(oxygen_rating, 2) * int(co2_rating, 2))
