import collections
import itertools
import math
import re

inp = open(re.search(r"day\d\d", __file__)[0] + 'input.txt').read().strip()
lines = inp.splitlines()

# lines = '''NNCB

# CH -> B
# HH -> N
# CB -> H
# NH -> C
# HB -> C
# HC -> B
# HN -> C
# NN -> C
# BH -> H
# NC -> B
# NB -> B
# BN -> B
# BB -> N
# BC -> B
# CC -> N
# CN -> C'''.splitlines()

polymer = lines[0]

rules = {}
for line in lines[2:]:
    a, b = line.split(' -> ')
    rules[a] = b

for step in range(10):
    new_poly = ''
    for i in range(len(polymer) - 1):
        key = polymer[i:i+2]
        new_poly += polymer[i] + rules[key]
    polymer = new_poly + polymer[-1]

letters = set(polymer)
counts = [polymer.count(c) for c in letters]
print(max(counts) - min(counts))

mem = {}
def solve(pair, steps):
    results = collections.defaultdict(int)
    if steps == 0:
        for c in pair:
           results[c] += 1
        return results
    key = (pair, steps)
    # print(key)
    if key in mem:
        return mem[key]

    mid = rules[pair]
    r1 = solve(pair[0] + mid, steps - 1)
    r2 = solve(mid + pair[1], steps - 1)
    for letter, count in r1.items():
        results[letter] += count
    for letter, count in r2.items():
        results[letter] += count
    results[mid] -= 1

    # print(key, results)

    mem[key] = results
    return results

def part2(polymer, steps):
    counts = collections.defaultdict(int)
    for i in range(len(polymer) - 1):
        pair = polymer[i:i+2]
        new_counts = solve(pair, steps)
        mid = rules[pair]
        for letter, count in new_counts.items():
            counts[letter] += count
        if i > 0:
            counts[pair[0]] -= 1
    return counts

counts = part2(lines[0], 40)
print(max(counts.values()) - min(counts.values()))



