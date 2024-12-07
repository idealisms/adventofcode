import collections
import itertools
import math
import re

inp = open(re.search(r"day\d\d", __file__)[0] + 'input.txt').read().strip()

def solves(target, nums):
    if len(nums) == 1:
        if nums[0] == target:
            return True
        return False
    if target <= 0:
        return False
    if target % nums[-1] == 0 and solves(
            target // nums[-1], nums[:-1]):
        return True
    return solves(target - nums[-1], nums[:-1])

def solves2(target, nums):
    # print(target, nums)
    if len(nums) == 1:
        if nums[0] == target:
            return True
        return False
    if target < nums[0]:
        return False
    if solves2(target, [nums[0] * nums[1]] + nums[2:]):
        return True
    if solves2(target, [nums[0] + nums[1]] + nums[2:]):
        return True
    return solves2(
        target,
        [int(str(nums[0]) + str(nums[1]))] + nums[2:])

part1 = part2 = 0
for line in inp.splitlines():
    target, nums_str = line.split(': ')
    target = int(target)
    nums = list(map(int, nums_str.split(' ')))
    if solves(target, nums):
        part1 += target
    if solves2(target, nums):
        # print(' ', target)
        part2 += target
print(part1)
print(part2)
