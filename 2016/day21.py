import collections
import itertools
import math
import re

inp = open(re.match(r"day\d\d", __file__)[0] + 'input.txt').read().strip()
passwd = list('abcdefgh')

# inp = '''swap position 4 with position 0
# swap letter d with letter b
# reverse positions 0 through 4
# rotate left 1 step
# move position 1 to position 4
# move position 3 to position 0
# rotate based on position of letter b
# rotate based on position of letter d'''
# passwd = list('abcde')

def scramble(commands, passwd):
  for line in commands:
    # print(''.join(passwd))
    tokens = line.split()
    if tokens[0] == 'swap':
      a = b = None
      if tokens[1] == 'position':
        a = int(tokens[2])
        b = int(tokens[5])
      elif tokens[1] == 'letter':
        a = passwd.index(tokens[2])
        b = passwd.index(tokens[5])
      passwd[a], passwd[b] = passwd[b], passwd[a]
    elif tokens[0] == 'rotate':
      steps = None
      if tokens[1] in ('left', 'right'):
        steps = int(tokens[2]) % len(passwd)
        if tokens[1] == 'right':
          steps = -steps
      elif tokens[1] == 'based':
        letter = tokens[6]
        index = passwd.index(letter)
        steps = (1 + index + (1 if index >= 4 else 0)) % len(passwd)
        steps = -steps
      passwd = passwd[steps:] + passwd[:steps]
    elif tokens[0] == 'reverse':
      a = int(tokens[2])
      b = int(tokens[4])
      a, b = min(a, b), max(a, b)
      passwd = passwd[:a] + list(reversed(passwd[a:b + 1])) + passwd[b + 1:]
    elif tokens[0] == 'move':
      a = int(tokens[2])
      b = int(tokens[5])
      letter = passwd[a]
      passwd.remove(letter)
      passwd.insert(b, letter)
    elif tokens[0] == 'unrotate':
      passwd = unrotate(passwd, tokens[6])
  return ''.join(passwd)

print('part1:', scramble(inp.splitlines(), list('abcdefgh')))

def unrotate(passwd, letter):
  # print('unrotate', ''.join(passwd), letter)
  steps = 1
  while True:
    index = steps - 1
    if index >= 5:
      index -= 1
    guess = passwd[steps % len(passwd):] + passwd[:steps % len(passwd)]
    if guess.index(letter) == index:
      return guess
    steps += 1

unscrambled_commands = []
for i, command in enumerate(reversed(inp.splitlines())):
  tokens = command.split()
  if tokens[0] == 'move':
    tokens[2], tokens[5] = tokens[5], tokens[2]
  elif tokens[0] == 'rotate':
    if tokens[1] in ('left', 'right'):
      tokens[1] = 'left' if tokens[1] == 'right' else 'right'
    else:
      tokens[0] = 'unrotate'

  unscrambled_commands.append(' '.join(tokens))

print('part2:', scramble(unscrambled_commands, list('fbgdceah')))
