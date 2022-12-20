import collections
import itertools
import math
import re

inp = open(re.search(r"day\d\d", __file__)[0] + 'input.txt').read().strip()
VAL = {
    '0': 0,
    '1': 1,
    '2': 2,
    '-': -1,
    '=': -2,
}

total = 0
for line in inp.splitlines():
    p = 1
    num = 0
    for c in reversed(line):
        num += VAL[c] * p
        p *= 5
    total += num

print(total)

REV = {
    0: '0',
    1: '1',
    2: '2',
    3: '1=',
    4: '1-',
    -1: '-',
    -2: '=',
}
nums = []
pad = 0
while total:
    n = REV[total % 5]
    nums.append(n + '0' * pad)
    pad += 1
    total = total // 5

def add(s1, s2):
    while len(s1) < len(s2):
        s1 = '0' + s1
    while len(s2) < len(s1):
        s2 = '0' + s2
    ans = ''
    for a, b in zip(s1, s2):
        ans += REV[VAL[a] + VAL[b]]
    return ans

snafu = '0'
for n in nums:
    snafu = add(snafu, n)

print(snafu)
