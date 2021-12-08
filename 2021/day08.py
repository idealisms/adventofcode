import collections
import itertools
import math
import re

inp = open(re.match(r"day\d\d", __file__)[0] + 'input.txt').read().strip()

# inp = '''acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf'''

inputs = []
for line in inp.splitlines():
    nums, signals = line.split(' | ')
    inputs.append([nums.split(), signals.split()])

part1 = 0
for nums, signals in inputs:
    for sig in signals:
        if len(sig) in (2, 3, 4, 7):
            part1 += 1
print(part1)


# nums = list(map(int, inp.split(',')))

def solve(nums):
    print(nums)
    num4 = [n for n in nums if len(n) == 4 ][0]
    num1 = [n for n in nums if len(n) == 2 ][0]
    num7 = [n for n in nums if len(n) == 3 ][0]
    num8 = [n for n in nums if len(n) == 7 ][0]

    sega = list(set(num7).difference(num4))[0]
    segb = segc = segd = sege = segf = segg = 0
    for digit in 'abcdefg':
        freq = sum([n.count(digit) for n in nums])
        if freq == 4:
            sege = digit
        elif freq == 6:
            segb = digit
        elif freq == 8 and digit != sega:
            segc = digit
        elif freq == 9:
            segf = digit

    for digit in 'abcdefg':
        freq = sum([n.count(digit) for n in nums])
        if freq == 7 and digit in num4 and digit not in num7:
            segd = digit
        elif freq == 7:
            segg = digit
    print(sega, segb, segc, segd, sege, segf, segg)
    return     [
        ''.join(sorted([sega, segb, segc, sege, segf, segg])),
        ''.join(sorted([segc, segf])),
        ''.join(sorted([sega, segc, segd, sege, segg])),
        ''.join(sorted([sega, segc, segd, segf, segg])),
        ''.join(sorted([segb, segc, segd, segf])),
        ''.join(sorted([sega, segb, segd, segf, segg])),
        ''.join(sorted([sega, segb, segd, sege, segf, segg])),
        ''.join(sorted([sega, segc, segf])),
        'abcdefg',
        ''.join(sorted([sega, segb, segc, segd, segf, segg])),
    ]

def decode(mapping, digits):
    print(mapping)
    n = 0
    for digit in digits:
        digit = ''.join(sorted(digit))
        print(digit)
        for i, map_ in enumerate(mapping):
            if digit == map_:
                print('found', i)
                n += i
                n *= 10
    n = n // 10
    print(n)
    return n

part2 = 0
for input in inputs:
    part2 += decode(solve(input[0]), input[1])
print(part2)

# a has 8
# b has 6*
# c has 8
# d has 7
# e has 4*
# f has 9*
# g has 7 

# 1: 2
# 7: 3
# 4: 4
# 8: 7

# 0: 6
# 2: 5
# 3: 5
# 5: 5
# 6: 6
# 9: 6
