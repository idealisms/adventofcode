import collections
import itertools
import math
import re

inp = open(re.search(r"day\d\d", __file__)[0] + 'input.txt').read().strip()
inp_ = '''???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1'''

# Brute force generate all arrangements.
'''
def gen_arrangement(line):
    pos = line.find('?')
    if pos == -1:
        yield line
        return
    for possible in gen_arrangement(line[:pos] + '#' + line[pos+1:]):
        yield possible
    for possible in gen_arrangement(line[:pos] + '.' + line[pos+1:]):
        yield possible

part1 = 0
for line in inp.splitlines():
    line, nums_str = line.split(' ')
    nums = nums_str.split(',')
    pattern = re.compile(
        '^[.]+' + '[.]+'.join('#{' + n + '}' for n in nums) + '[.]+$')
    # print(line)
    for possible in gen_arrangement('.' + line + '.'):
        if re.search(pattern, possible):
            # print(pattern, possible)
            part1 += 1
    print(part1)
'''

# Recursion with backtracking and memoization.
mem = {}
def count_arrangements(line, nums):
    if len(nums) == 0:
        return 1 if line.find('#') == -1 else 0
    if len(line) == 0:
        return 0
    if line[0] == '.':
        return count_arrangements(line[1:], nums)
    
    key = (line, tuple(nums))
    if key in mem:
        return mem[key]

    total = 0
    if line[0] == '?':
        total += count_arrangements(line[1:], nums)
        total += count_arrangements('#' + line[1:], nums)
    else:
        # nums[0] # or ? followed by . or ?
        for c in line[:nums[0]]:
            if c not in '#?':
                return 0
        if line[nums[0]] not in '.?':
            return 0
        total += count_arrangements(line[nums[0]+1:], nums[1:])
    mem[key] = total
    return total

part1 = part2 = 0
for line in inp.splitlines():
    line, nums_str = line.split(' ')
    nums = list(map(int, nums_str.split(',')))
    part1 += count_arrangements(line + '.', nums)
    part2 += count_arrangements('?'.join([line] * 5) + '.', nums * 5)
    print(part1, part2)
