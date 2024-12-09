import collections
import itertools
import math
import re

inp = open(re.search(r"day\d\d", __file__)[0] + 'input.txt').read().strip()
# inp = '2333133121414131402'

digits = []
for d in inp.strip():
    digits.append(int(d))

part1 = 0
offset = 0
i = 0
id_ = 0
while i < len(digits):
    d = digits[i]
    if i % 2 == 0:
        for j in range(d):
            # print(offset, id_)
            part1 += offset * id_
            offset += 1
        id_ += 1
    else:
        assert(len(digits) % 2 == 1)
        for j in range(d):
            back_id = len(digits) // 2
            # print(offset, back_id)
            part1 += offset * back_id
            offset += 1
            digits[-1] -= 1
            if digits[-1] == 0:
                digits = digits[:-2]
    i += 1
print(part1)

digits = []
for d in inp.strip():
    digits.append(int(d))

disk = []
id_ = 0
gaps = []
files = []
for i, d in enumerate(digits):
    if i % 2 == 0:
        if d > 0:
            files.append((len(disk), d))
            disk += [id_] * d
        id_ += 1
    else:
        if d > 0:
            gaps.append((len(disk), d))
            disk += ['.'] * d
# print(''.join(map(str, disk)))
# print(gaps)
# print(files)
for i, file in enumerate(reversed(files)):
    id_ = len(files) - 1 - i
    file_start, file_size = file
    # print(id_, file_start, file_size)
    for g, gap in enumerate(gaps):
        gap_start, gap_size = gap
        if file_size <= gap_size and gap_start < file_start:
            for j in range(file_size):
                disk[gap_start + j] = id_
                disk[file_start + j] = '.'
            gaps[g] = (gap_start + file_size, gap_size - file_size)
            break
    # print(''.join(map(str, disk)))
part2 = 0
for i, d in enumerate(disk):
    if d != '.':
        part2 += i * d
print(part2)
