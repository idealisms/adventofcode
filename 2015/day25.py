import collections
import itertools
import math
import re

inp = open(re.match(r"day\d\d", __file__)[0] + 'input.txt').read().strip()
row, col = [int(n) for n in re.findall(r'\d+', inp)]

def get_nth(row, col):
  row_count_start = row + (col - 1)
  # The numbers in column 1 are the sum(1..n) + 1.
  start = (((row_count_start - 1) * (row_count_start)) // 2) + 1
  # From the start number, the offset is the column.
  nth = start + col - 1
  return nth

# print(get_nth(1, 1))
# print(get_nth(4, 1))
# print(get_nth(4, 3))
# print(get_nth(1, 6))

def step(n):
  return (n * 252533) % 33554393

nth = get_nth(row, col)
n = 20151125
for _ in range(nth - 1):
  n = step(n)
print('part1:', n)
