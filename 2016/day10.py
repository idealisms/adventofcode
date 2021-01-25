import collections
import itertools
import math
import re

inp = open(re.match(r"day\d\d", __file__)[0] + 'input.txt').read().strip()

holding = collections.defaultdict(list)
rules = {}
for line in inp.splitlines():
  if line.startswith('value'):
    value, to_bot = [int(n) for n in re.findall(r'\d+', line)]
    holding[to_bot].append(value)
  else:
    from_bot, to_low, to_high = re.match(
      r'bot (\d+) gives low to ((bot|output) \d+) and high to ((bot|output) \d+)',
      line).group(1, 2, 4)
    rules[int(from_bot)] = (to_low, to_high)

workqueue = []
for bot, chips in holding.items():
  if len(chips) == 2:
    workqueue.append(bot)

part1 = None
output = {}
while len(workqueue):
  bot = workqueue.pop(0)
  chips = sorted(holding[bot])
  if chips == [17, 61]:
    part1 = bot
  holding[bot] = []
  to_low, to_high = rules[bot]
  if to_low.startswith('output '):
    output[int(to_low[7:])] = chips[0]
  else:
    low_bot = int(to_low[4:])
    holding[low_bot].append(chips[0])
    if len(holding[low_bot]) == 2:
      workqueue.append(low_bot)
  if to_high.startswith('output '):
    output[int(to_high[7:])] = chips[1]
  else:
    hi_bot = int(to_high[4:])
    holding[hi_bot].append(chips[1])
    if len(holding[hi_bot]) == 2:
      workqueue.append(hi_bot)

print('part1:', part1)
print('part2:', math.prod(output[n] for n in range(3)))
