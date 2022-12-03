import collections
import itertools
import math
import re

inp = open(re.search(r"day\d\d", __file__)[0] + 'input.txt').read().strip()
# inp = """vJrwpWtwJgWrhcsFMMfFFhFp
# jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
# PmmdzqPrVvPwwTWBwg
# wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
# ttgJtRGJQctTZtZT
# CrZsJsPPZsGzwwsLwLmpwMDw"""
def find_item(line):
    mid = int(len(line)/2)
    a, b = line[:mid], line[mid:]
    for c in a:
        if c in b:
            return c

pri = ' abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
part1 = 0
for line in inp.splitlines():
    c = find_item(line)
    part1 += pri.index(c)
print(part1) # 7:57

part2 = 0
lines = inp.splitlines()
while lines:
    a, b, c = lines[:3]
    lines = lines[3:]
    x = set(a).intersection(set(b)).intersection(set(c))
    part2 += pri.index(list(x)[0])
print(part2) # 13:11