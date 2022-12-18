import collections
import itertools
import math
import re

inp = open('day19input.txt').read().strip()
_inp = '''Blueprint 1: Each ore robot costs 4 ore. Each clay robot costs 2 ore. Each obsidian robot costs 3 ore and 14 clay. Each geode robot costs 2 ore and 7 obsidian.
Blueprint 2: Each ore robot costs 2 ore. Each clay robot costs 3 ore. Each obsidian robot costs 3 ore and 8 clay. Each geode robot costs 3 ore and 12 obsidian.'''

blueprints = []
max_ore_bots = []
mems = []
for line in inp.splitlines():
    nums = list(map(int, re.findall('\d+', line)))
    blueprints.append([
        (nums[1], 0, 0),
        (nums[2], 0, 0),
        (nums[3], nums[4], 0),
        (nums[5], 0, nums[6]),
    ])
    max_ore_bots.append(max(nums[1], nums[2], nums[3], nums[5]))
    mems.append({})

# print(blueprints)
# print(max_ore_bots)


def solve(bid, bots, res, time):
    if time == 1:
        return 0

    key = (bots, res, time)
    if key in mems[bid]:
        return mems[bid][key]

    costs = blueprints[bid]

    # print(key)
    best = -1

    for i, cost in enumerate(costs):
        if i == 0 and bots[0] >= max_ore_bots[bid]:
            continue
        if i == 1 and bots[1] >= costs[2][1]:
            continue
        if i == 2 and bots[2] >= costs[3][2]:
            continue
        if time == 2 and i <= 2:
            continue
        if time == 3 and i <= 1:
            continue
        if time == 4 and i == 0:
            continue
        new_res = tuple(r - c for r, c in zip(res, cost))
        if all(map(lambda x: x >= 0, new_res)):
            new_res = tuple(b + r for b, r in zip(bots, new_res))
            if i == 3:
                best = max(best, time - 1 + solve(bid, bots, new_res, time - 1))
            else:
                new_bots = list(bots)
                new_bots[i] += 1
                best = max(best, solve(bid, tuple(new_bots), new_res, time - 1))

    if time == 2 and best != -1:
        mems[bid][key] = best
        return best
    best = max(best, solve(bid, bots, tuple(b + r for b, r, in zip(bots, res)), time - 1))
    mems[bid][key] = best
    return best

def part1():
    total = 0
    for bid, bp in enumerate(blueprints):
        geos = solve(bid, (1, 0, 0), (0, 0, 0), 24)
        print(bid+1, geos)
        total += (bid + 1) * geos
    return total
# print(part1()) # 817

def part2():
    total = 1
    for bid, bp in enumerate(blueprints[:3]):
        geos = solve(bid, (1, 0, 0), (0, 0, 0), 32)
        print(bid+1, geos)
        total *= geos
    return total
print(part2())
# pypy running time
# real    5m34.568s
# user    5m0.993s
# sys     0m7.772s