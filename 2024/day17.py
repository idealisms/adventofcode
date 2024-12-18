import collections
import itertools
import math
import re

inp = open(re.search(r"day\d\d", __file__)[0] + 'input.txt').read().strip()
# inp = '''Register A: 729
# Register B: 0
# Register C: 0

# Program: 0,1,5,4,3,0'''

# inp = '''Register A: 2024
# Register B: 0
# Register C: 0

# Program: 0,3,5,4,3,0'''

regs_str, program_str = inp.split('\n\n')
REGS = list(map(int, re.findall(r'\d+', regs_str)))
A, B, C = range(3)
program = list(map(int, re.findall(r'\d', program_str)))


def run(program, rega, target=None):
    def combo(n):
        if n < 4:
            return n
        return regs[n - 4]

    regs = [rega, 0, 0]
    out = []
    ip = 0
    while True:
        if ip >= len(program):
            break
        inst = program[ip]
        # print(ip, inst, regs)
        if inst == 0:
            regs[A] = regs[A] >> combo(program[ip+1])
            ip += 2
        elif inst == 1:
            regs[B] = regs[B] ^ program[ip+1]
            ip += 2
        elif inst == 2:
            regs[B] = combo(program[ip+1]) % 8
            ip += 2
        elif inst == 3:
            if regs[A] == 0:
                ip += 2
            else:
                ip = program[ip+1]
        elif inst == 4:
            regs[B] = regs[B] ^ regs[C]
            ip += 2
        elif inst == 5:
            out.append(combo(program[ip+1]) % 8)
            ip += 2
        elif inst == 6:
            regs[B] = regs[A] >> combo(program[ip+1])
            ip += 2
        elif inst == 7:
            regs[C] = regs[A] >>combo(program[ip+1])
            ip += 2
    return out

# part1 = run(program, REGS[0])
# print(part1)
# print(','.join(map(str, part1)))

for a in range(29569499671493 << 3, 29569499671493 << 4):
    try:
        out = run(program, a)
        print(a, out)
    except ValueError:
        pass

# Program instructions
# 2,4  B = A % 8
# 1,3  B = B ^ 3
# 7,5  C = A >> B
# 4,7  B = B ^ C
# 0,3  A = A >> B
# 1,5  B = B ^ 5
# 5,5  out <- B
# 3,0  if A != 0: goto 0

# program: 2,4,1,3,7,5,4,7,0,3,1,5,5,5,3,0
# 3145 [5, 5, 3, 0]
# 25161 [5, 5, 5, 3, 0]
# 201290 [1, 5, 5, 5, 3, 0]
# 1610321 [3, 1, 5, 5, 5, 3, 0]
# 14099780 [0, 3, 1, 5, 5, 5, 3, 0]
# 112798241 [7, 0, 3, 1, 5, 5, 5, 3, 0]
# 902389516 [4, 7, 0, 3, 1, 5, 5, 5, 3, 0]
# 7219116130 [5, 4, 7, 0, 3, 1, 5, 5, 5, 3, 0]
# 57752929045 [7, 5, 4, 7, 0, 3, 1, 5, 5, 5, 3, 0]
# 462023432360 [3, 7, 5, 4, 7, 0, 3, 1, 5, 5, 5, 3, 0]
# 3696187458936 [1, 3, 7, 5, 4, 7, 0, 3, 1, 5, 5, 5, 3, 0]
# 29569499671493 [4, 1, 3, 7, 5, 4, 7, 0, 3, 1, 5, 5, 5, 3, 0]
# 236555997372013 [2, 4, 1, 3, 7, 5, 4, 7, 0, 3, 1, 5, 5, 5, 3, 0]

