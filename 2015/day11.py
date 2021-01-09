import collections
import itertools
import math
import re

inp = open(re.match(r"day\d\d", __file__)[0] + 'input.txt').read().strip()

def inc(passwd):
  pos = -1
  while True:
    passwd[pos] += 1
    if passwd[pos] == 26:
      passwd[pos] = 0
      pos -= 1
    else:
      return passwd

def is_valid(passwd):
  has_straight = False
  for i in range(len(passwd) - 2):
    if passwd[i] == passwd[i+1] - 1 == passwd[i+2] - 2:
      has_straight = True
      break
  has_confusing_letters = (
    ord('i') - ord('a') in passwd or
    ord('o') - ord('a') in passwd or
    ord('l') - ord('a') in passwd
  )
  has_two_pairs = False
  for i in range(len(passwd) - 2):
    if passwd[i] == passwd[i+1]:
      for j in range(i+2, len(passwd) - 1):
        if passwd[j] == passwd[j+1]:
          has_two_pairs = True
          break
      break

  return has_straight and not has_confusing_letters and has_two_pairs

passwd = []
for c in inp:
  passwd.append(ord(c) - ord('a'))

for _ in itertools.count(0):
  passwd = inc(passwd)
  if is_valid(passwd):
    break

print('part1:', ''.join(chr(n + ord('a')) for n in passwd))

for _ in itertools.count(0):
  passwd = inc(passwd)
  if is_valid(passwd):
    break
print('part2:', ''.join(chr(n + ord('a')) for n in passwd))
