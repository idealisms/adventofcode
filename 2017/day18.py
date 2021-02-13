import collections
import itertools
import math
import re

inp = open(re.match(r"day\d\d", __file__)[0] + 'input.txt').read().strip()
commands = []
for line in inp.splitlines():
  commands.append(line.split())

def run(registers, pc, send_queue, receive_queue, part1=True):
  def get_value(s):
    try:
      return int(s)
    except:
      return registers[s]

  num_sends = 0
  while True:
    # print('pc:', pc, registers)
    command = commands[pc]
    if command[0] == 'snd':
      send_queue.append(get_value(command[1]))
      num_sends += 1
      pc += 1
    elif command[0] == 'set':
      registers[command[1]] = get_value(command[2])
      pc += 1
    elif command[0] == 'add':
      registers[command[1]] += get_value(command[2])
      pc += 1
    elif command[0] == 'mul':
      registers[command[1]] *= get_value(command[2])
      pc += 1
    elif command[0] == 'mod':
      registers[command[1]] = registers[command[1]] % get_value(command[2])
      pc += 1
    elif command[0] == 'rcv':
      if part1:
        if 0 != get_value(command[1]):
          return send_queue[-1]
      else:
        if not len(receive_queue):
          return registers, pc, send_queue, receive_queue, num_sends
        else:
          registers[command[1]] = receive_queue.pop(0)
      pc += 1
    elif command[0] == 'jgz':
      if get_value(command[1]) > 0:
        pc += get_value(command[2])
      else:
        pc += 1

registers = collections.defaultdict(int)
print('part1:', run(registers, 0, [], []))

regs0 = collections.defaultdict(int)
regs1 = collections.defaultdict(int)
regs1['p'] = 1
pc0 = 0
pc1 = 0
num_sends_p1 = 0
p0_send_q = []
p1_send_q = []
while True:
  regs0, pc0, p0_send_q, p1_send_q, _ = run(regs0, pc0, p0_send_q, p1_send_q, part1=False)
  regs1, pc1, p1_send_q, p0_send_q, num_sends = run(regs1, pc1, p1_send_q, p0_send_q, part1=False)
  if len(p0_send_q) == 0 and len(p1_send_q) == 0:
    break
  num_sends_p1 += num_sends

print('part2:', num_sends_p1)
