import collections
import itertools
import math
import re

inp = open(re.match(r"day\d\d", __file__)[0] + 'input.txt').read().strip()
rule_lines, molecule = inp.split('\n\n')

rules = collections.defaultdict(list)
out_rules = {}
for line in rule_lines.splitlines():
  elt, out = line.split(' => ')
  rules[elt].append(tuple(re.findall(r'[A-Z][a-z]?', out)))
  assert out not in out_rules
  out_rules[out] = elt

possible = set()
sequence = re.findall(r'[A-Z][a-z]?', molecule)
for i, elt in enumerate(sequence):
  for out in rules[elt]:
    new_sequence = sequence[:i]
    new_sequence.extend(out)
    new_sequence.extend(sequence[i+1:])
    possible.add(tuple(new_sequence))
print('part1:', len(possible))

# Part 2 was tricky. I tried a general approach of trying every replacement,
# but there are too many combinations, even with backtracking and memoizing.
# The insight, from looking at the rules is that any sequence ending with 'Ar'
# is unique. This means we can solve prefixes of the string up to Ar
# incrementally. This leaves us with HCaF, which can then easily be reduced
# to 'e'.
#
# Test case
# molecule = "CRnCaCaCaSiRnBPTiMgAr"  # CRnCa
# molecule = "CRnCaCaCaSiRnBPTiMgArSiRnSiRnMgAr"
# molecule = "CRnCaSiRnSiRnMgAr"
# molecule = "CRnCaCaCaSiRnBPTiMgArSiRnSiRnMgArSiRnCaFArTiTiBSiThFYCaFArCaCaSiThCaPBSiThSiThCaCaPTiRnPBSiThRnFAr"
mem = {}
def steps(mol):
  if mol in mem:
    return mem[mol]
  next_steps = set()
  for seq, replacement in out_rules.items():
    pos = mol.find(seq)
    while pos != -1:
      new_mol = mol[:pos] + replacement + mol[pos+len(seq):]
      # print(mol, new_mol, seq, replacement)
      next_steps.add(new_mol)
      pos = mol.find(seq, pos + 1)

  if len(next_steps) == 0:
    # print('unreducible:', mol)
    # Not a valid reduction. Give it a high number of steps so we don't use it.
    if mol.endswith('Ar'):
      return 10**7, mol
    return 0, mol
  best = 10**7
  reduced_mol = ''
  for next_step in next_steps:
    s, m = steps(next_step)
    if s + 1 < best:
      best = s + 1
      reduced_mol = m
  mem[mol] = best, reduced_mol
  return best, reduced_mol

pos = molecule.find('Ar')
total_steps = 0
while pos != -1:
  prefix = molecule[:pos+2]
  num_steps, reduced_mol = steps(prefix)
  if num_steps == 0:
    break
  total_steps += num_steps
  molecule = reduced_mol + molecule[pos+2:]
  pos = molecule.find('Ar')

s, m = steps(molecule)
# print(molecule)  # HCaF
assert m == 'e'
print('part2:', total_steps + s)
