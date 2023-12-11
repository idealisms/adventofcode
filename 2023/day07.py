import collections
import itertools
import math
import re
import functools
import pprint

inp = open(re.search(r"day\d\d", __file__)[0] + 'input.txt').read().strip()
# inp = '''32T3K 765
# T55J5 684
# KK677 28
# KTJJT 220
# QQQJA 483'''

hands = []
for line in inp.splitlines():
    hand, bid = line.split()
    hands.append((hand, int(bid)))

HIGH_CARD, ONE_PAIR, TWO_PAIR, THREE, FULL_HOUSE, \
    FOUR, FIVE = list(range(7))

def determine_hand(hand):
    counts = collections.defaultdict(int)
    for card in hand:
        counts[card] += 1
    if 5 in counts.values():
        return FIVE
    if 4 in counts.values():
        return FOUR
    if 3 in counts.values():
        if 2 in counts.values():
            return FULL_HOUSE
        return THREE
    if list(counts.values()).count(2) == 2:
        return TWO_PAIR
    if list(counts.values()).count(2) == 1:
        return ONE_PAIR
    return HIGH_CARD

def cmp_hands(lhs, rhs):
    CARD_SCORES = '23456789TJQKA'
    left_hand = lhs[0]
    right_hand = rhs[0]
    score_lhs = determine_hand(left_hand)
    score_rhs = determine_hand(right_hand)
    if score_lhs < score_rhs:
        return -1
    elif score_lhs > score_rhs:
        return 1
    for l, r in zip(left_hand, right_hand):
        if CARD_SCORES.find(l) < CARD_SCORES.find(r):
            return -1
        elif CARD_SCORES.find(l) > CARD_SCORES.find(r):
            return 1
    raise Exception("should not get here")

hands.sort(key=functools.cmp_to_key(cmp_hands))
# pprint.pp(hands)
part1 = 0
for i, (hand, bid) in enumerate(hands):
    part1 += (i+1) * bid
print(part1)

def determine_hand2(hand):
    counts = collections.defaultdict(int)
    for card in hand:
        counts[card] += 1
    jokers = counts['J']
    counts['J'] = 0
    if 5 in counts.values():
        return FIVE
    if 4 in counts.values():
        if jokers == 1:
            return FIVE
        return FOUR
    if 3 in counts.values():
        if 2 in counts.values():
            return FULL_HOUSE
        if jokers == 2:
            return FIVE
        elif jokers == 1:
            return FOUR
        return THREE
    if list(counts.values()).count(2) == 2:
        if jokers == 1:
            return FULL_HOUSE
        return TWO_PAIR
    if list(counts.values()).count(2) == 1:
        if jokers == 3:
            return FIVE
        elif jokers == 2:
            return FOUR
        elif jokers == 1:
            return THREE
        return ONE_PAIR
    if jokers >= 4:
        return FIVE
    elif jokers == 3:
        return FOUR
    elif jokers == 2:
        return THREE
    elif jokers == 1:
        return ONE_PAIR
    return HIGH_CARD

def cmp_hands2(lhs, rhs):
    CARD_SCORES = 'J23456789TQKA'
    left_hand = lhs[0]
    right_hand = rhs[0]
    score_lhs = determine_hand2(left_hand)
    score_rhs = determine_hand2(right_hand)
    if score_lhs < score_rhs:
        return -1
    elif score_lhs > score_rhs:
        return 1
    for l, r in zip(left_hand, right_hand):
        if CARD_SCORES.find(l) < CARD_SCORES.find(r):
            return -1
        elif CARD_SCORES.find(l) > CARD_SCORES.find(r):
            return 1
    raise Exception("should not get here")

hands.sort(key=functools.cmp_to_key(cmp_hands2))
# pprint.pp(hands)
part2 = 0
for i, (hand, bid) in enumerate(hands):
    part2 += (i+1) * bid
print(part2)
