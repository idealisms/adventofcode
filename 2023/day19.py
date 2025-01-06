import collections
import heapq
import itertools
import math
import re

inp = open(re.search(r"day\d\d", __file__)[0] + 'input.txt').read().strip()
# inp = '''px{a<2006:qkq,m>2090:A,rfg}
# pv{a>1716:R,A}
# lnx{m>1548:A,A}
# rfg{s<537:gd,x>2440:R,A}
# qs{s>3448:A,lnx}
# qkq{x<1416:A,crn}
# crn{x>2662:A,R}
# in{s<1351:px,qqz}
# qqz{s>2770:qs,m<1801:hdj,R}
# gd{a>3333:R,R}
# hdj{m>838:A,pv}

# {x=787,m=2655,a=1222,s=2876}
# {x=1679,m=44,a=2067,s=496}
# {x=2036,m=264,a=79,s=2244}
# {x=2461,m=1339,a=466,s=291}
# {x=2127,m=1623,a=2188,s=1013}'''

workflow_lines, parts_lines = inp.split('\n\n')
workflows = {}
for line in workflow_lines.splitlines():
    name, rules_line = line.split('{')
    rules = []
    for rule in rules_line[:-1].split(','):
        if rule in 'AR':
            rules.append((rule,))
        elif '<' in rule or '>' in rule:
            cat, val, res = re.split('[<>:]', rule)
            rules.append((
                '<' if '<' in rule else '>',
                cat,
                int(val),
                res))
        else:
            rules.append((rule,))
    workflows[name] = rules

def work(name, values):
    flow = workflows[name]
    for rule in flow:
        if rule[0] in 'AR':
            return rule[0]
        if rule[0] == '<':
            if values[rule[1]] < rule[2]:
                if rule[3] in 'AR':
                    return rule[3]
                return work(rule[3], values)
        elif rule[0] == '>':
            if values[rule[1]] > rule[2]:
                if rule[3] in 'AR':
                    return rule[3]
                return work(rule[3], values)
        else:
            return work(rule[0], values)
    raise "Should not be here"

part1 = 0
for line in parts_lines.splitlines():
    x, m, a, s = map(int, re.findall('\d+', line))
    values = dict(x=x, m=m, a=a, s=s)
    if work('in', values) == 'A':
        part1 += x + m + a + s
print(part1)

def invert(rule):
    sign, symbol, value, _ = rule
    if sign == '<':
        return ('>', symbol, value - 1)
    return ('<', symbol, value + 1)

def combos(conds):
    ranges = {
        'x': [1, 4000],
        'm': [1, 4000],
        'a': [1, 4000],
        's': [1, 4000],
    }
    for cond in conds:
        if cond[0] == '<':
            ranges[cond[1]][1] = min(ranges[cond[1]][1], cond[2] - 1)
        else:
            ranges[cond[1]][0] = max(ranges[cond[1]][0], cond[2] + 1)
    total = 1
    for lo, hi in ranges.values():
        if hi < lo:
            total = 0
        else:
            total *= hi - lo + 1
    # print(total, conds, ranges)
    return total

def count_combos(name, conds):
    flow = workflows[name]
    total = 0
    for rule in flow:
        # print(name, rule)
        # print('  ', conds)
        if rule[0] == 'R':
            return total
        if rule[0] == 'A':
            return total + combos(conds)
        if rule[0] in '<>':
            if rule[3] == 'A':
                total += combos(conds + [rule])
            elif rule[3] != 'R':
                total += count_combos(rule[3], conds + [rule])
            conds.append(invert(rule))
        else:
            return total + count_combos(rule[0], conds)

print(count_combos('in', []))
