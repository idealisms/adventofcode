import collections
import itertools
import math
import re

inp = open(re.search(r"day\d\d", __file__)[0] + 'input.txt').read().strip()
part1 = part2 = 0
do = True
for res in re.findall('mul[(](\d+)[,](\d+)[)]|(do[(][)])|(don[\']t[(][)])', inp):
    if res[2]:
        do = True
    elif res[3]:
        do = False
    else:
        part1 += int(res[0]) * int(res[1])
        if do:
            part2 += int(res[0]) * int(res[1])
print(part1)
print(part2)