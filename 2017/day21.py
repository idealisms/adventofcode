import collections
import itertools
import math
import re

inp = open(re.match(r"day\d\d", __file__)[0] + 'input.txt').read().strip()

def rotate(image):
  out = [''] * len(image)
  for r in range(len(image)):
    for c in range(len(image)):
      out[-c - 1] += image[r][c]
  return out

def flip(image):
  out = [row for row in image]
  out[0], out[-1] = out[-1], out[0]
  return out

def gen_input(input_string):
  image = input_string.split('/')
  for _ in range(4):
    yield ''.join(image)
    image = rotate(image)
  image = flip(image)
  for _ in range(4):
    yield ''.join(image)
    image = rotate(image)

rules = {}
for line in inp.splitlines():
  in_, output = line.split(' => ')
  for in_variant in gen_input(in_):
    # print(in_variant)
    rules[in_variant] = output.split('/')
  # print()

def step(grid):
  size = len(grid)
  step_size = 2 if size % 2 == 0 else 3
  output_size = (size // step_size) * (step_size + 1)
  output = [''] * output_size
  for r, c in itertools.product(
      range(size // step_size), range(size // step_size)):
    key = ''.join([grid[r * step_size + dr][c * step_size:c * step_size + step_size] for dr in range(step_size)])
    out_image = rules[key]
    for dr, row in enumerate(out_image):
      output[r * (step_size + 1) + dr] += row
  return output

grid = '''.#.
..#
###'''.splitlines()
part1 = 0
for i in range(18):
  if i == 5:
    part1 = ''.join(grid).count('#')
  grid = step(grid)
print('part1:', part1)
print('part2:', ''.join(grid).count('#'))
