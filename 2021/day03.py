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
ones = [0] * len(lines[0])
for digits in lines:
    for i, digit in enumerate(digits):
        if digit == '1':
            ones[i] += 1
gamma = ''
epsilon = ''
for cnt in ones:
    if cnt > len(lines) / 2:
        gamma += '1'
        epsilon += '0'
    else:
        gamma += '0'
        epsilon += '1'

print(int(gamma, 2) * int(epsilon, 2))


def find_number(lines, prefix, is_oxygen):
    ones = 0
    for line in lines:
        if line[0] == '1':
            ones += 1
    ret = []
    for line in lines:
        if is_oxygen and ones > len(lines) / 2 and line[0] == '1':
            ret.append(line[1:])
            n_prefix = '1'
        elif is_oxygen and ones < len(lines) / 2 and line[0] == '0':
            ret.append(line[1:])
            n_prefix = '0'
        elif is_oxygen and ones == len(lines) / 2 and line[0] == '1':
            ret.append(line[1:])
            n_prefix = '1'
        elif not is_oxygen and ones > len(lines) / 2 and line[0] == '0':
            ret.append(line[1:])
            n_prefix = '0'
        elif not is_oxygen and ones < len(lines) / 2 and line[0] == '1':
            ret.append(line[1:])
            n_prefix = '1'
        elif not is_oxygen and ones == len(lines) / 2 and line[0] == '0':
            ret.append(line[1:])
            n_prefix = '0'
    return ret, prefix + n_prefix

possible = lines[:]
prefix = ''
while len(possible) > 1:
    possible, prefix = find_number(possible, prefix, True)
oxygen_rating = prefix + possible[0]

possible = lines[:]
prefix = ''
while len(possible) > 1:
    possible, prefix = find_number(possible, prefix, False)
co2_rating = prefix + possible[0]
print(int(oxygen_rating, 2) * int(co2_rating, 2))
