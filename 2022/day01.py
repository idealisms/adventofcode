import collections
import itertools
import math
import re

inp = open(re.search(r"day\d\d", __file__)[0] + 'input.txt').read().strip()

groups = inp.split('\n\n')
print(max([sum(list(map(int, group.splitlines()))) for group in groups]))
print(sum(sorted([sum(list(map(int, group.splitlines()))) for group in groups])[-3:]))
