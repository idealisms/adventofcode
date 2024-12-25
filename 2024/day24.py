import collections
import heapq
import itertools
import math
import re

inp = open(re.search(r"day\d\d", __file__)[0] + 'input.txt').read().strip()
known_lines, equations_lines = inp.split('\n\n')

vals = {}
for line in known_lines.splitlines():
    k, v = line.split(': ')
    vals[k] = v == '1'

cmds = []
for line in equations_lines.splitlines():
    a, op, b, _, c = line.split(' ')
    cmds.append((a, op, b, c))

def resolve_commands(cmds, vals):
    ret_vals = vals.copy()
    while cmds:
        retry_cmds = []
        for cmd in cmds:
            a, op, b, c = cmd
            if a not in ret_vals or b not in ret_vals:
                retry_cmds.append(cmd)
                continue

            res = -1
            if op == 'XOR':
                res = ret_vals[a] ^ ret_vals[b]
            elif op == 'OR':
                res = ret_vals[a] | ret_vals[b]
            elif op == 'AND':
                res = ret_vals[a] & ret_vals[b]
            ret_vals[c] = res
        if len(retry_cmds) == len(cmds):
            raise ValueError
        cmds = retry_cmds
    return ret_vals

part1 = 0
ret_vals = resolve_commands(cmds, vals)
for k in ret_vals.keys():
    if k.startswith('z'):
        shift = int(k[1:])
        part1 |= ret_vals[k] << shift
print(part1)  # 36035961805936

def incorrect_bits(vals):
    Z_DIGITS = 46
    x = [0] * Z_DIGITS
    y = [0] * Z_DIGITS
    z = [0] * Z_DIGITS
    for k in vals.keys():
        if k.startswith('x'):
            x[int(k[1:])] = vals[k]
        elif k.startswith('y'):
            y[int(k[1:])] = vals[k]
        elif k.startswith('z'):
            z[int(k[1:])] = vals[k]

    carry = 0
    error_bits = set()
    for i in range(Z_DIGITS):
        xd = int(x[i])
        yd = int(y[i])
        zd = int(z[i])
        if (xd + yd + carry) % 2 == zd:
            print(carry, '+', int(x[i]), '+', int(y[i]), '=', int(z[i]), '    ok')
        else:
            print(carry, '+', int(x[i]), '+', int(y[i]), '=', int(z[i]), '    error', i)
            error_bits.add(i)
        if xd + yd + carry > 1:
            carry = 1
        else:
            carry = 0
    return error_bits

C = len(cmds)
# # print(C) # 222
# swappable0 = set()
# swappable1 = set()
# testable_swaps = set()
# cur_errors = incorrect_bits(ret_vals)
# for i in range(C):
#     for j in range(i + 1, C):
#         if ret_vals[cmds[i][3]] == ret_vals[cmds[j][3]]:
#             continue
#         test_cmds = cmds.copy()
#         test_cmds[i] = (cmds[i][0], cmds[i][1], cmds[i][2], cmds[j][3])
#         test_cmds[j] = (cmds[j][0], cmds[j][1], cmds[j][2], cmds[i][3])
#         new_ret_vals = None
#         try:
#             new_ret_vals = resolve_commands(test_cmds, vals)
#         except ValueError:
#             continue
#         if new_ret_vals:
#             error_bits = incorrect_bits(new_ret_vals)
#             if len(error_bits) < len(cur_errors) and error_bits.union(cur_errors) == cur_errors:
#                 if ret_vals[cmds[i][3]]:
#                     swappable1.add(cmds[i][3])
#                     swappable0.add(cmds[j][3])
#                 else:
#                     swappable0.add(cmds[i][3])
#                     swappable1.add(cmds[j][3])
#                 testable_swaps.add((i, j))
#                 print(cmds[i][3], cmds[j][3], ret_vals[cmds[i][3]], ret_vals[cmds[j][3]])

# print(len(swappable0), swappable0)
# print(len(swappable1), swappable1)

# cnt = 0
# for swaps in itertools.combinations(testable_swaps, 4):
#     if len(set(itertools.chain.from_iterable(swaps))) != 8:
#         continue
#     cnt += 1
#     if cnt % 100000 == 0:
#         print(cnt)

incorrect_bits(ret_vals)
# 1 + 0 + 1 = 1     error 11
# 1 + 0 + 1 = 1     error 12
# 1 + 1 + 1 = 0     error 13
# 0 + 1 + 1 = 1     error 15
# 1 + 0 + 1 = 1     error 16
# 1 + 1 + 0 = 1     error 17
# 1 + 0 + 0 = 0     error 18
# 0 + 1 + 0 = 0     error 19
# 0 + 0 + 0 = 1     error 20
# 1 + 0 + 0 = 0     error 37
# 0 + 1 + 1 = 1     error 38

def pv(k):
    print(k, int(ret_vals[k]))

# qqw or gkc fixes 11-13, thus, z11 must be wrong

# gkc AND qqw -> z11
pv('qqw') # is 1
pv('gkc') # is 1, should be 0 # based on x&y
pv('z11') # 1, becomes 0

# htn XOR dtq -> z12
pv('htn') # 1, should be 0 # based on x&y
pv('dtq') # 0
pv('z12') # 1, becomes 0

# jkm XOR dmp -> z13
pv('jkm') # 0
pv('dmp') # 0, should be 1 # based on x&y
pv('z13') # 0



# pv('wpd') # is 0, becomes 1
# # wpd OR dpf -> dtq
# pv('dpf') # is 0
# pv('dtq') # is 0, becomes 1
# # htn XOR dtq -> z12
# pv('htn') # is 1
# pv('z12') # is 1, becomes 0

# # htn AND dtq -> gvh
# pv('gvh') # is 0, becomes 1
# # bnn OR gvh -> jkm
# pv('bnn') # is 0
# pv('jkm') # is 0, becomes 1
# # jkm XOR dmp -> z13
# pv('dmp') # is 0
# pv('z13') # is 0, becomes 1
# # dmp AND jkm -> qpw
# pv('qpw') # is 0, stays 0

# # skh XOR rkt -> z15
pv('skh') # 1 # based on x&y
pv('rkt') # 0 should be 1 # fixes 15-18
pv('z15') # 1, becomes 0
# # rkt AND skh -> kjk
# pv('skh') # 1
# pv('kjk') # 0, becomes 1
# # jqf OR kjk -> kbq
# pv('jqf') # 0
# pv('kbq') # 0, becomes 1
# # rvn XOR kbq -> z16
# pv('rvn') # 1 # based on x&y
# pv('z16') # 1, becomes 0
# # kbq AND rvn -> vtm
# pv('vtm') # 0, becomes 1
# # rhd OR vtm -> wrc
# pv('rhd') # 0
# pv('wrc') # 0, becomes 1
# # wrc XOR hbw -> z17
# pv('hbw') # 1 # based on x&y
# pv('z17') # 1, becomes 0
# # hbw AND wrc -> jks
# pv('jks') # 0, becomes 1
# # jks OR cwn -> qvq
# pv('cwn') # 0
# pv('qvq') # 0, becomes 1
# # qvq XOR hns -> z18
# pv('hns') # 0 # based on x&y
# pv('z18') # 0, becomes 1
# # hns AND qvq -> mts
# pv('mts') # 0, stays 0
# # y19 AND x19 -> z19 # based on x&y
# pv('z19') # is 0, should be 1

# # bvw XOR hvn -> z20
# pv('bvw') # 0 # based on x&y
# pv('hvn') # 1
# pv('z20') # 1, should be 0
# # y20 XOR x20 -> bvw
# # 0 ^ 0 = 0


# # jgw OR rhh -> z37
# pv('jgw') # is 0
# pv('rhh') # 0 # based on x&y
# pv('z37') # 0
# # sqj XOR wts -> z38
pv('sqj') # 0 # based on x&y
pv('wts') # 1
pv('z38') # 1

# swap = ['gkc', 'z19', 'rkt']

cmds_idx = {}
for i in range(C):
    cmds_idx[cmds[i][3]] = i

def try_swap(cmds, a, b):
    i, j = cmds_idx[a], cmds_idx[b]
    test_cmds = cmds.copy()
    test_cmds[i] = (cmds[i][0], cmds[i][1], cmds[i][2], cmds[j][3])
    test_cmds[j] = (cmds[j][0], cmds[j][1], cmds[j][2], cmds[i][3])
    incorrect_bits(resolve_commands(test_cmds, vals))
    return test_cmds

# z11 1
# z19 0
# z37 0
# sqj 0
# htn 1
# 
cmds = try_swap(cmds, 'rkt', 'z11')
cmds = try_swap(cmds, 'hvn', 'z19')
cmds = try_swap(cmds, 'htn', 'sqj')
# cmds = try_swap(cmds, 'dmp', 'skh')
# cmds = try_swap(cmds, 'bnn', 'z37')

# # cmds = equations_lines.splitlines()
# # error_inputs = set()
# # for line in cmds:
# #     a, op, b, _, c = line.split(' ')
# #     if c.startswith('z') and int(c[1:]) in error_bits:
# #         print(line)
# #         error_inputs.add(a)
# #         error_inputs.add(b)
# # print(error_inputs)

# x00 XOR y00 -> z00
#
# hjp XOR kjs -> z01
# (x00 AND y00) XOR (x01 XOR y01) -> z01
# carry XOR x01 XOR y01 -> z01
#
# rvm XOR vdq -> z02
# ((x01 AND y01) OR ((x01 XOR y01) AND (x00 AND y00))) XOR (y02 XOR x02) -> z02
# carry XOR y02 XOR x02 -> z02
# We expect this pattern to continue throughout.
# I just manually examined the rules.
