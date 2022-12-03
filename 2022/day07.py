import collections
import itertools
import math
import re

inp = open(re.search(r"day\d\d", __file__)[0] + 'input.txt').read().strip()
lines = inp.splitlines()

root = {}
cwd = root
cmd = 0
while cmd < len(lines):
    if lines[cmd].startswith('$ cd '):
        dirname = lines[cmd].split(' ')[-1]
        if dirname == '..':
            cwd = cwd[dirname]
        else:
            cwd[dirname] = {'..': cwd}            
            cwd = cwd[dirname]
        cmd += 1
    elif lines[cmd] == '$ ls':
        cmd += 1
        while cmd < len(lines) and not lines[cmd].startswith('$ '):
            if lines[cmd].startswith('dir'):
                dirname = lines[cmd].split(' ')[-1]
                if dirname not in cwd:
                    cwd[dirname] = {}
            else:
                size_str, filename = lines[cmd].split(' ')
                cwd[filename] = int(size_str)
            cmd += 1

def size(d):
    s = 0
    for key, value in d.items():
        if key == '..':
            pass
        elif type(value) == int:
            s += value
        else:
            s += size(value)
    return s

def part1(d):
    ans = 0
    for key, value in d.items():
        if key == '..':
            pass
        elif type(value) == int:
            pass
        else:
            s = size(value)
            if s <= 100000:
                ans += s
            ans += part1(value)
    return ans
print(part1(root))

disk_size = 70000000
target_space = 30000000
space_free = disk_size - size(root)

def part2(d, best):
    for key, value in d.items():
        if key == '..':
            pass
        elif type(value) == int:
            pass
        else:
            s = size(value)
            if space_free + s >= target_space:
                best = min(s, best)
            best = part2(value, best)
    return best
print(part2(root, disk_size))