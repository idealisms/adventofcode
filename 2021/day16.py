import collections
import itertools
import math
import re

inp = open(re.search(r"day\d\d", __file__)[0] + 'input.txt').read().strip()

# inp = 'D2FE28'
# inp = '8A004A801A8002F478'
# inp = '38006F45291200'

binary = bin(int(inp, 16))[2:]
zero_pad = len(binary) % 4
if zero_pad:
    binary = ('0' * (4 - zero_pad)) + binary

print(binary)
part1 = 0

def parseLiteral(s):
    print('parseLiteral', s)
    bina = ''
    while True:
        bits = s[:5]
        s = s[5:]
        bina += bits[1:]
        if bits[0] == '0':
            break
    return int(bina, 2), s

def getValue(typ, sub_values):
    value = None
    if typ == 0:
        value = sum(sub_values)
    elif typ == 1:
        value = math.prod(sub_values)
    elif typ == 2:
        value = min(sub_values)
    elif typ == 3:
        value = max(sub_values)
    elif typ == 5:
        assert len(sub_values) == 2
        value = 1 if sub_values[0] > sub_values[1] else 0
    elif typ == 6:
        assert len(sub_values) == 2
        value = 1 if sub_values[0] < sub_values[1] else 0
    elif typ == 7:
        assert len(sub_values) == 2
        value = 1 if sub_values[0] == sub_values[1] else 0

    assert value is not None
    return value

def parseType0(typ, s):
    print('parseType0', s)
    num_bits = int(s[:15], 2)
    s = s[15:]
    sub_values = []
    while num_bits:
        before = len(s)
        sub_value, s = parse(s)
        sub_values.append(sub_value)
        num_bits -= (before - len(s))
        assert num_bits >= 0

    return getValue(typ, sub_values), s

def parseType1(typ, s):
    print('parseType1', s)
    num_packets = int(s[:11], 2)
    s = s[11:]
    sub_values = []
    for _ in range(num_packets):
        sub_value, s = parse(s)
        sub_values.append(sub_value)

    return getValue(typ, sub_values), s

def parse(s):
    global part1
    ver = int(s[:3], 2)
    typ = int(s[3:6], 2)
    print('parse', ver, typ, s)

    s = s[6:]
    part1 += ver

    value = None
    if typ == 4:
        value, s = parseLiteral(s)
    else:
        if s[0] == '0':
            value, s = parseType0(typ, s[1:])
        else:
            value, s = parseType1(typ, s[1:])

    assert value is not None
    return value, s

value, _ = parse(binary)
print(part1)
print(value)
