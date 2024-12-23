import collections
import heapq
import itertools
import math
import re

inp = open(re.search(r"day\d\d", __file__)[0] + 'input.txt').read().strip()
conns = collections.defaultdict(set)
for line in inp.splitlines():
    a = line[:2]
    b = line[3:5]
    conns[a].add(b)
    conns[b].add(a)

part1 = set()
for a in conns.keys():
    for b in conns[a]:
        for c in conns[b]:
            if c != a and c in conns[a]:
                if 't' in (a[0], b[0], c[0]):
                    part1.add(tuple(sorted([a, b, c])))
print(len(part1))

def is_fully_connected(t, s):
    for n in s:
        if t not in conns[n]:
            return False
    return True


# I learned about the Bron–Kerbosch algorithm after writing this.
# This would fail for some inputs, but luckily this was not one
# of those cases.
seen = set()
part2 = set()
for a in conns.keys():
    # if a in seen:
    #     continue
    cur = set()
    cur.add(a)
    q = list(conns[a])
    while len(q) > 0:
        t = q.pop()
        if t in cur:
            continue
        if is_fully_connected(t, cur):
            cur.add(t)
            seen.add(t)
            q.extend(conns[t])
    if len(cur) > len(part2):
        part2 = cur

print(len(part2))
print(','.join(sorted(part2)))
