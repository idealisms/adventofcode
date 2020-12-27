import re

inp = open(re.match(r"day\d\d", __file__)[0] + 'input.txt').read().strip()

floor = inp.count('(') - inp.count(')')
print('part1:', floor)

floor = 0
for i, c in enumerate(inp):
  if floor == -1:
    print('part2:', i)
    break
  floor += 1 if c == '(' else -1
