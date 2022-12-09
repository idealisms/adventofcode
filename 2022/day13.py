import collections
import itertools
import functools
import math
import re

WRONG, CONT, CORRECT = -1, 0, 1

inp = open(re.search(r"day\d\d", __file__)[0] + 'input.txt').read().strip()
_inp = '''[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]'''

cases = inp.split('\n\n')

def compare(left, right):
    # print('compare', left, right)
    if type(left) == int and type(right) == int:
        if left < right:
            return 1
        elif left > right:
            return -1
        return 0
    elif type(left) == int and type(right) == list:
        return compare([left], right)
    elif type(left) == list and type(right) == int:
        return compare(left, [right])
    else:
        for l, r in zip(left, right):
            res = compare(l, r)
            if res != 0:
                return res
        if len(left) < len(right):
            return 1
        elif len(left) > len(right):
            return -1
        return 0

part1 = 0
all_packets = [
    [[2]],
    [[6]],
]
for i, case in enumerate(cases):
    left = eval(case.split('\n')[0], {})
    right = eval(case.split('\n')[1], {})
    all_packets.append(left)
    all_packets.append(right)
    result = compare(left, right)
    # print(i+1, result)
    if result == CORRECT:
        part1 += i + 1
print(part1)

all_packets = sorted(all_packets, key=functools.cmp_to_key(compare), reverse=True)
# print(all_packets)
a = b = 0
for i, packet in enumerate(all_packets):
    if packet == [[2]]:
        a = i + 1
    elif packet == [[6]]:
        b = i + 1
# part2
print(a*b)