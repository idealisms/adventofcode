import collections
import heapq
import itertools
import math
import re

inp = open(re.search(r"day\d\d", __file__)[0] + 'input.txt').read().strip()

def secret(num, iterations=1):
    for _ in range(iterations):
        num = ((num * 64) ^ num) % 16777216
        num = ((num // 32) ^ num) % 16777216
        num = ((num * 2048) ^ num) % 16777216
    return num

# for i in range(1, 11):
#     print(secret(123, i))

SEEN_KEYS = set()

def build_map(num):
    digits = [num % 10]
    deltas = []
    for _ in range(2000):
        num = ((num * 64) ^ num) % 16777216
        num = ((num // 32) ^ num) % 16777216
        num = ((num * 2048) ^ num) % 16777216
        digits.append(num % 10)
        deltas.append(digits[-1] - digits[-2])
    m = {}
    for i in range(len(deltas)-3):
        key = tuple(deltas[i:i+4])
        if key not in m:
            m[key] = digits[i+4]
            SEEN_KEYS.add(key)
    return m

part1 = 0
price_maps = []
for line in inp.splitlines():
    s = int(line)
    part1 += secret(s, 2000)
    price_maps.append(build_map(s))
print(part1)

part2 = 0
for key in SEEN_KEYS:
    bananas = 0
    for m in price_maps:
        bananas += m.get(key, 0)
    part2 = max(part2, bananas)
print(part2)
