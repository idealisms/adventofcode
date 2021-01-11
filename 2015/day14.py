import collections
import itertools
import math
import re

inp = open(re.match(r"day\d\d", __file__)[0] + 'input.txt').read().strip()

# Dancer can fly 27 km/s for 5 seconds, but then must rest for 132 seconds.
deers = {}
for line in inp.splitlines():
  mo = re.match(r'(\w+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds.', line)
  deers[mo.group(1)] = [int(n) for n in mo.group(2, 3, 4)]

def get_distance(deer, time):
  fly_distance, fly_time, rest_time = deer
  distance = 0
  while True:
    flying_sec = min(fly_time, time)
    distance += fly_distance * flying_sec
    if fly_time < time:
      time -= fly_time
    if time <= rest_time:
      return distance
    time -= rest_time

TARGET_TIME = 2503
print('part1:', max((get_distance(deer, TARGET_TIME) for deer in deers.values())))

deers = deers.values()
points = [0] * len(deers)
for seconds in range(1, TARGET_TIME + 1):
  distances = [get_distance(deer, seconds) for deer in deers]
  max_distance = max(distances)
  for i, distance in enumerate(distances):
    if distance == max_distance:
      points[i] += 1
print('part2:', max(points))
