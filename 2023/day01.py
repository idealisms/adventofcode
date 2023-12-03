import collections
import itertools
import math
import re

inp = open(re.search(r"day\d\d", __file__)[0] + 'input.txt').read().strip()
lines = inp.splitlines()
# lines = '''two1nine
# eightwo5three
# abcone2threexyz
# xtwone3four
# 4nineeightseven2
# zoneight234
# 7pqrstsixteen'''.splitlines()

sum = 0
for line in lines:
    digits = re.findall(r'\d', line)
    sum += int(digits[0] + digits[-1], 10)
print(sum)

tokens = {
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
}

sum = 0
for line in lines:
   best_pos = 999999
   for k, v in tokens.items():
       pos = line.find(k)
       if pos != -1 and pos < best_pos:
           first = str(v)
           best_pos = pos

   best_pos = -1
   for k, v in tokens.items():
       pos = line.rfind(k)
       if pos > best_pos:
           last_digit = str(v)
           best_pos = pos
   print(line, first, last_digit)
   sum += int(first + last_digit, 10)
print(sum)

