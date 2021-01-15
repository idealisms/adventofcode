import collections
import itertools
import math
import re

inp = open(re.match(r"day\d\d", __file__)[0] + 'input.txt').read().strip()

PRESENTS_TARGET = int(inp)
# for house_num in itertools.count(1):
#   presents = 0
#   for i in range(1, int(math.sqrt(house_num))):
#     if house_num % i == 0:
#       presents += i * 10
#       if house_num // i != i:
#         presents += (house_num // i) * 10
#   if presents >= PRESENTS_TARGET:
#     print('part1:', house_num)  # 776160
#     break
# time pypy3 day20.py (part1 only)
# real    0m4.614s
# user    0m4.604s
# sys     0m0.010s

for house_num in itertools.count(1):
  presents = 0
  for i in range(1, int(math.sqrt(house_num))):
    if house_num % i == 0:
      if i * 50 >= house_num:
        presents += i * 11
      n = house_num // i
      if n != i and n * 50 >= house_num:
        presents += n * 11
  if presents >= PRESENTS_TARGET:
    print('part2:', house_num)  # 786240
    break
# time pypy3 day20.py (part2 only)
# real    0m4.787s
# user    0m4.777s
# sys     0m0.010s
