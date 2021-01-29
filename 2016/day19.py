import collections
import itertools
import math
import re

inp = open(re.match(r"day\d\d", __file__)[0] + 'input.txt').read().strip()
num_elves = int(inp)

# elf number
deque = collections.deque()
for i in range(num_elves):
  deque.append(i + 1)

while len(deque) > 1:
  elf_number = deque.popleft()
  _ = deque.popleft()
  deque.append(elf_number)
print('part1:', deque.popleft())

class Buckets(object):
  '''Use an array of arrays.

  - Accessing index i is O(lg n)
  - Removing at index i is O(lg n)
  '''

  def __init__(self, num_elves):
    self.size = math.ceil(num_elves**.5)
    self.buckets = []
    bucket = []
    for i in range(num_elves):
      bucket.append(i + 1)
      if len(bucket) == self.size:
        self.buckets.append(bucket)
        bucket = []
    self.buckets.append(bucket)

  def pop(self, idx):
    '''Remove the item at index i and return it.'''
    bucket = 0
    while idx >= len(self.buckets[bucket]):
      idx -= len(self.buckets[bucket])
      bucket += 1
    item = self.buckets[bucket][idx]
    self.buckets[bucket].remove(item)

    # Remove empty buckets.
    if idx == 0 and len(self.buckets[bucket]) == 0:
      self.buckets.remove(self.buckets[bucket])
    return item

  def __getitem__(self, key):
    # We only handle integer values for key.
    bucket = 0
    while key >= len(self.buckets[bucket]):
      key -= len(self.buckets[bucket])
      bucket += 1
    return self.buckets[bucket][key]

buckets = Buckets(num_elves)
# buckets = Buckets(5)
# buckets = Buckets(22222)

pos = 0
size = num_elves
while size > 1:
  # print(size, pos)
  cur_elf = buckets[pos]
  target = pos + (size // 2)
  _ = buckets.pop(target % size)
  # print(f' {cur_elf} steals from {_}')
  from_right = target < size
  size -= 1
  if from_right:
    pos += 1
  pos = pos % size
print('part2:', buckets[0])
