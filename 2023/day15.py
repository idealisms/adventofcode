import collections
import itertools
import math
import re

inp = open(re.search(r"day\d\d", __file__)[0] + 'input.txt').read().strip()

tokens = inp.strip().split(',')

def hash(s):
    cv = 0
    for c in s:
        cv += ord(c)
        cv *= 17
        cv %= 256
    return cv
# print(hash('HASH'))
# print(hash('rn'))
# print(hash('cm'))

part1 = 0
for token in tokens:
    part1 += hash(token)
print(part1)

hashmap = [[] for _ in range(256)]
for token in tokens:
    if token[-1] == '-':
        k = token[:-1]
        bucket = hashmap[hash(k)]
        for b in bucket:
            if b.startswith(k + '='):
                bucket.remove(b)
                break
    else:
        k = token[:-2]
        bucket = hashmap[hash(k)]
        replace = False
        for i, b in enumerate(bucket):
            if b.startswith(k + '='):
                bucket[i] = token
                replace = True
                break
        if not replace:
            bucket.append(token)

part2 = 0
for box, bucket in enumerate(hashmap):
    for slot, entry in enumerate(bucket):
        part2 += (box + 1) * (slot + 1) * int(entry[-1])
print(part2)

