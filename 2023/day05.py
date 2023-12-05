import collections
import itertools
import math
import re

inp = open(re.search(r"day\d\d", __file__)[0] + 'input.txt').read().strip()
# inp = '''seeds: 79 14 55 13

# seed-to-soil map:
# 50 98 2
# 52 50 48

# soil-to-fertilizer map:
# 0 15 37
# 37 52 2
# 39 0 15

# fertilizer-to-water map:
# 49 53 8
# 0 11 42
# 42 0 7
# 57 7 4

# water-to-light map:
# 88 18 7
# 18 25 70

# light-to-temperature map:
# 45 77 23
# 81 45 19
# 68 64 13

# temperature-to-humidity map:
# 0 69 1
# 1 0 69

# humidity-to-location map:
# 60 56 37
# 56 93 4'''

parts = inp.split('\n\n')
seeds = list(map(int, parts[0].split(': ')[1].split(' ')))
maps = []
for input_blob in parts[1:]:
    cur_map = []
    for line in input_blob.splitlines()[1:]:
        cur_map.append(list(map(int, line.split(' '))))
    cur_map.sort(key=lambda tu: tu[1])
    maps.append(cur_map)

def map_num(num, map_index):
    new_value = num
    for dest_start, source_start, size in maps[map_index]:
        if source_start <= num < source_start + size:
            new_value = dest_start + num - source_start
            break
    if map_index == len(maps) - 1:
        return new_value
    return map_num(new_value, map_index + 1)

part1 = 99999999999999
for seed in seeds:
    part1 = min(part1, map_num(seed, 0))
print(part1)

def map_range(start, length, map_index):
    if map_index == len(maps):
        return start

    best = 99999999999999
    for dest_start, source_start, size in maps[map_index]:
        if source_start <= start < source_start + size:
            sub_length = min(start+length, source_start + size) - start
            best = min(best, map_range(
                dest_start + start - source_start,
                sub_length,
                map_index + 1))
            if sub_length != length:
                best = min(best, map_range(
                    start+sub_length,
                    length - sub_length,
                    map_index
                ))
    if best == 99999999999999:
        for dest_start, source_start, size in maps[map_index]:
            if start <= source_start < start + length:
                sub_length = source_start - start
                best = min(best, map_range(
                    start,
                    sub_length,
                    map_index + 1,
                ))
                best = min(best, map_range(
                    start + sub_length,
                    length - sub_length,
                    map_index
                ))
                break
    if best == 99999999999999:
        best = map_range(start, length, map_index + 1)

    return best

part2 = 99999999999999
while len(seeds):
    start, length = seeds[:2]
    seeds = seeds[2:]
    part2 = min(part2, map_range(start, length, 0))
print(part2)
