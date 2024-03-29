import collections
import itertools
import math
import re

inp = open(re.search(r"day\d\d", __file__)[0] + 'input.txt').read().strip()
# inp = '''Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
# Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
# Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
# Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
# Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
# Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11'''
lines = inp.splitlines()

# (set(), set())
cards = []
for line in lines:
    winning, guesses = line.split(':')[1].split(' | ')
    cards.append((
        set(map(int, re.findall('\d+', winning))),
        set(map(int, re.findall('\d+', guesses)))
    ))

part1 = 0
for winning, guesses in cards:
    matches = 0
    for guess in guesses:
        if guess in winning:
            matches += 1
    if matches >= 1:
        part1 += pow(2, matches - 1)
print(part1)

scores = {}
def score(card_num):
    if card_num in scores:
        return scores[card_num]
    winning, guesses = cards[card_num]
    matches = 0
    for guess in guesses:
        if guess in winning:
            matches += 1
    total = 1
    for i in range(matches):
        total += score(card_num + i + 1)
    scores[card_num] = total
    return total

part2 = 0
for c, card in enumerate(cards):
    part2 += score(c)
# print(scores)
print(part2)

