import collections
import itertools
import math
import re

inp = open(re.match(r"day\d\d", __file__)[0] + 'input.txt').read().strip()
PACKAGE_WEIGHTS = set([int(n) for n in inp.splitlines()])

def min_num_packages(package_weights, target_weight):
  min_packages = [0] * (target_weight + 1)
  for num in package_weights:
    min_packages[num] = 1
    for j in range(num + 1, target_weight + 1):
      if min_packages[j - num] > 0:
        if min_packages[j] == 0:
          min_packages[j] = min_packages[j - num] + 1
        else:
          min_packages[j] = min(min_packages[j], min_packages[j - num] + 1)
  return min_packages[-1]

target_weight = sum(PACKAGE_WEIGHTS) // 3
small_group_size = min_num_packages(PACKAGE_WEIGHTS, target_weight)

lowest_qe = 10**12
for sizes in itertools.combinations(PACKAGE_WEIGHTS, small_group_size):
  if sum(sizes) == target_weight:
    remaining_packages = PACKAGE_WEIGHTS - set(sizes)
    if min_num_packages(remaining_packages, target_weight) > 0:
      lowest_qe = min(lowest_qe, math.prod(sizes))

print('part1:', lowest_qe)

def can_split_in_three(package_weights, target_weight):
  group_size = min_num_packages(package_weights, target_weight)
  # There's an assumption here that the secound group would
  # be the smallest size. This is pretty likely since there's
  # only 25 packages to be split into 3 groups.
  for sizes in itertools.combinations(package_weights, group_size):
    if sum(sizes) == target_weight:
      remaining_packages = package_weights - set(sizes)
      if min_num_packages(remaining_packages, target_weight) > 0:
        return True
  return False

target_weight = sum(PACKAGE_WEIGHTS) // 4
small_group_size = min_num_packages(PACKAGE_WEIGHTS, target_weight)

lowest_qe = 10**12
for sizes in itertools.combinations(PACKAGE_WEIGHTS, small_group_size):
  if sum(sizes) == target_weight:
    remaining_packages = PACKAGE_WEIGHTS - set(sizes)
    if can_split_in_three(remaining_packages, target_weight):
      lowest_qe = min(lowest_qe, math.prod(sizes))

print('part2:', lowest_qe)
