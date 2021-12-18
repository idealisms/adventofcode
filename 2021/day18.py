import collections
import itertools
import math
import re

inp = open(re.search(r"day\d\d", __file__)[0] + 'input.txt').read().strip()

# inp = '''[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]
# [7,[[[3,7],[4,3]],[[6,3],[8,8]]]]
# [[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]]
# [[[[2,4],7],[6,[0,5]]],[[[6,8],[2,8]],[[2,1],[4,5]]]]
# [7,[5,[[3,8],[1,4]]]]
# [[2,[2,2]],[8,[8,1]]]
# [2,9]
# [1,[[[9,3],9],[[9,0],[0,7]]]]
# [[[5,[7,4]],7],1]
# [[[[4,2],2],6],[8,7]]'''

# inp = '''[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]
# [[[5,[2,8]],4],[5,[[9,9],0]]]
# [6,[[[6,2],[5,6]],[[7,6],[4,7]]]]
# [[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]
# [[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]
# [[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]
# [[[[5,4],[7,7]],8],[[8,3],8]]
# [[9,3],[[9,9],[6,[4,9]]]]
# [[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]
# [[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]'''
# inp = '''[1,1]
# [2,2]
# [3,3]
# [4,4]
# [5,5]
# [6,6]'''

snums = []
for line in inp.splitlines():
    snum = []
    for c in line:
        if c == ',':
            continue
        if c in '[]':
            snum.append(c)
        else:
            snum.append(int(c))
    snums.append(snum)

def isNum(n):
    return str(n) not in '[]'

def sexplode(cur):
    while True:
        has_changed = False
        # print(cur)
        for i, (a, b) in enumerate(zip(cur, cur[1:])):
            if isNum(a) and isNum(b):
                depth = cur[:i].count('[') - cur[:i].count(']')
                if depth < 5:
                    continue
                for j in range(i - 1, -1, -1):
                    if isNum(cur[j]):
                        cur[j] += a
                        break
                for j in range(i + 2, len(cur)):
                    if isNum(cur[j]):
                        cur[j] += b
                        break
                cur = cur[:i - 1] + [0] + cur[i+3:]
                # print('explode:', snumstr(cur))
                has_changed = True
                break
        if not has_changed:
            break

    # print(cur)
    return cur

def ssplit(cur):
    for i, n in enumerate(cur):
        if isNum(n) and n > 9:
            cur = cur[:i] + ['[', n // 2, n // 2 if n % 2 == 0 else (n // 2) + 1, ']'] + cur[i+1:]
            # print('split:', snumstr(cur))
            break
    return cur

def snumstr(snum):
    return ' '.join(map(str, snum))

def sreduce(cur):
    while True:
        before = cur
        cur = sexplode(cur)
        cur = ssplit(cur)
        if before == cur:
            break
    return cur

def addsnums(a, b):
    return ['['] + a + b + [']']

cur = snums[0]
for snum in snums[1:]:
    cur = addsnums(cur, snum)
    # print('addition:', snumstr(cur))
    cur = sreduce(cur)
# print('final', snumstr(cur))

def magnitude(cur):
    while len(cur) > 1:
        for i, (a, b) in enumerate(zip(cur, cur[1:])):
            if isNum(a) and isNum(b):
                cur = cur[:i-1] + [3*a + 2*b] + cur[i+3:]
                break
    return cur[0]

part1 = magnitude(cur)
print(part1)

part2 = 0
for i in range(len(snums)):
    for j in range(i+1, len(snums)):
        part2 = max(part2, magnitude(sreduce(addsnums(snums[i], snums[j]))))
        part2 = max(part2, magnitude(sreduce(addsnums(snums[j], snums[i]))))
print(part2)
