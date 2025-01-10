import collections
import heapq
import itertools
import math
import re

inp = open(re.search(r"day\d\d", __file__)[0] + 'input.txt').read().strip()
# inp = '''broadcaster -> a, b, c
# %a -> b
# %b -> c
# %c -> inv
# &inv -> a'''
# inp = '''broadcaster -> a
# %a -> inv, con
# &inv -> b
# %b -> con
# &con -> output'''

class FlipFlop(object):
    def __init__(self, dests):
        self.type = '%'
        self.status = 0
        self.dests = dests

    def process(self, source, pulse):
        outs = []

        if pulse == 'l':
            for dest in self.dests:
                outs.append(('hl'[self.status], dest))
            self.status = (self.status + 1) % 2

        return outs

    def state(self):
        return (self.status, )

class Conjunction(object):
    def __init__(self, dests):
        self.type = '&'
        self.inputs = []
        self.last = {}
        self.dests = dests

    def set_inputs(self, inputs):
        self.inputs = sorted(inputs)
        for input in self.inputs:
            self.last[input] = 'l'

    def process(self, source, pulse):
        outs = []
        self.last[source] = pulse
        out_pulse = 'l' if all([p == 'h' for p in self.last.values()]) else 'h'

        for dest in self.dests:
            outs.append((out_pulse, dest))

        return outs

    def state(self):
        last = []
        for input in self.inputs:
            last.append(self.last[input])
        return tuple(last)

class Broadcast(object):
    def __init__(self, dests):
        self.type = 'b'
        self.dests = dests

    def process(self, source, pulse):
        outs = []
        for dest in self.dests:
            outs.append((pulse, dest))
        return outs

modules = {}
for line in inp.splitlines():
    name, dests = line.split(' -> ')
    dests = dests.split(', ')
    if name[0] == 'b':
        modules[name] = Broadcast(dests)
    elif name[0] == '%':
        modules[name[1:]] = FlipFlop(dests)
    else:
        modules[name[1:]] = Conjunction(dests)

for name, mod in modules.items():
    if mod.type == '&':
        in_names = []
        for in_name, in_mod in modules.items():
            if name in in_mod.dests:
                in_names.append(in_name)
        # print(name, 'inputs', in_names)
        mod.set_inputs(in_names)

def print_val(nodes):
    out = []
    for node in nodes:
        out.append(str(modules[node].status))
    print(' '.join(out))

def push_button(step):
    q = [('button', 'l', 'broadcaster')]
    counts = collections.Counter()
    while len(q) > 0:
        source, pulse, dest = q.pop(0)
        if dest == 'ls' and pulse == 'h':
            print(step, source)

        # print(source, pulse, dest)
        counts[pulse] += 1
        if dest == 'rx':
            if pulse == 'l':
                counts['rx'] += 1
            continue
        mod = modules[dest]
        outs = mod.process(source, pulse)
        for out in outs:
            q.append((dest, out[0], out[1]))
   
    return counts

totals = collections.Counter()
for i in range(100000):
    totals += push_button(i+1)
    if i == 999:
        print(totals['l'] * totals['h'])

# ph 3779
# dd 3889
# nz 3907
# tx 4051
print(3779 * 3889 * 3907 * 4051)