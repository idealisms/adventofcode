import collections
import itertools
import math
import re

inp = open(re.search(r"day\d\d", __file__)[0] + 'input.txt').read().strip()
_inp = '''Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1'''

Monkey = collections.namedtuple('Monkey', ['items', 'op', 'test', 'iftrue', 'iffalse'])
def parse(lines):
    return Monkey(
        list(map(int, re.findall('\d+', lines[1]))),
        lines[2].split(' = ')[1],
        int(re.findall('\d+', lines[3])[0]),
        int(re.findall('\d+', lines[4])[0]),
        int(re.findall('\d+', lines[5])[0]),
    )

monkeys = []
for input_lines in inp.split('\n\n'):
    monkey = parse(input_lines.split('\n'))
    monkeys.append(monkey)

inspected = [0] * len(monkeys)
for _ in range(20):
    for i, monkey in enumerate(monkeys):
        while monkey.items:
            item = monkey.items.pop(0)
            inspected[i] += 1
            worry = eval(monkey.op, {'old': item})
            worry = worry // 3
            if worry % monkey.test == 0:
                monkeys[monkey.iftrue].items.append(worry)
            else:
                monkeys[monkey.iffalse].items.append(worry)
# print(monkeys)
# print(inspected)
print(math.prod(list(sorted(inspected))[-2:]))

# part 2
monkeys = []
for input_lines in inp.split('\n\n'):
    monkey = parse(input_lines.split('\n'))
    monkeys.append(monkey)
lcm = 1
for monkey in monkeys:
    lcm *= monkey.test
inspected = [0] * len(monkeys)
for _ in range(10000):
    for i, monkey in enumerate(monkeys):
        while monkey.items:
            item = monkey.items.pop(0)
            inspected[i] += 1
            worry = eval(monkey.op, {'old': item})
            worry = worry % lcm
            if worry % monkey.test == 0:
                monkeys[monkey.iftrue].items.append(worry)
            else:
                monkeys[monkey.iffalse].items.append(worry)
print(inspected)
print(math.prod(list(sorted(inspected))[-2:]))
