import collections
import itertools
import math
import re

inp = open(re.match(r"day\d\d", __file__)[0] + 'input.txt').read().strip()
gena, genb = [int(n) for n in re.findall('\d+', inp)]

part1 = 0
mask = 2**16 - 1
for _ in range(40 * 1000 * 1000):
  gena = (gena * 16807) % 2147483647
  genb = (genb * 48271) % 2147483647

  if gena & mask == genb & mask:
    part1 += 1
print('part1:', part1)

def nexta(gena):
  while True:
    gena = (gena * 16807) % 2147483647
    if gena % 4 == 0:
      return gena
def nextb(genb):
  while True:
    genb = (genb * 48271) % 2147483647
    if genb % 8 == 0:
      return genb

gena, genb = [int(n) for n in re.findall('\d+', inp)]
part2 = 0
for _ in range(5 * 1000 * 1000):
  gena = nexta(gena)
  genb = nextb(genb)
  if gena & mask == genb & mask:
    part2 += 1
print('part2:', part2)
