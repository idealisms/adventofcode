import collections
import itertools
import math
import re

inp = open(re.search(r"day\d\d", __file__)[0] + 'input.txt').read().strip()
lines = inp.splitlines()

maxes = {
    'red': 12,
    'green': 13,
    'blue': 14,
}
part1 = 0
part2 = 0
for line in lines:
    game_str, grabs_str = line.split(': ')
    is_impossible = False
    mins = {
        'red': 0,
        'green': 0,
        'blue': 0,
    }
    for grab_str in grabs_str.split('; '):
        tokens = re.split('[ ,]+', grab_str)
        for i in range(len(tokens) // 2):
            num_marbles = int(tokens[i * 2])
            color = tokens[i*2+1]

            # part 1
            if num_marbles > maxes[color]:
                is_impossible = True

            # part 2
            mins[color] = max(mins[color], num_marbles)
    if not is_impossible:
        part1 += int(game_str.split(' ')[1])
    part2 += math.prod(mins.values())
print(part1)
print(part2)