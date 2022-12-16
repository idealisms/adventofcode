import collections
import itertools
import math
import re

inp = open('day16input.txt').read().strip()
_inp = '''Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
Valve BB has flow rate=13; tunnels lead to valves CC, AA
Valve CC has flow rate=2; tunnels lead to valves DD, BB
Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
Valve EE has flow rate=3; tunnels lead to valves FF, DD
Valve FF has flow rate=0; tunnels lead to valves EE, GG
Valve GG has flow rate=0; tunnels lead to valves FF, HH
Valve HH has flow rate=22; tunnel leads to valve GG
Valve II has flow rate=0; tunnels lead to valves AA, JJ
Valve JJ has flow rate=21; tunnel leads to valve II'''

edges = {}
rates = {}
for line in inp.splitlines():
    valves = re.findall('[A-Z][A-Z]', line)
    edges[valves[0]] = valves[1:]
    rate = int(re.split('[=;]', line)[1])
    if rate:
        rates[valves[0]] = int(re.split('[=;]', line)[1])
rates['AA'] = 0 # true for my input and sample input
# Build the time to move between valves.
dist = {}
target_vs = set(rates.keys())
def calc_dists(s):
    dist[s] = {}
    seen = {s}
    q = [(v, 1) for v in edges[s]]
    while len(dist[s]) < len(rates) - 1:
        v, d = q.pop(0)
        if v in seen:
            continue
        seen.add(v)
        if v in target_vs:
            dist[s][v] = d
        q.extend((target_v, d+1) for target_v in edges[v])

for s in rates.keys():
    calc_dists(s)

def maxp(v, t, p, visited, dists, time):
    best = (time - t) * p
    # print(v, t, p, order, best)
    for target_v, dt in dists[v].items():
        if target_v in visited:
            continue
        # one time to open, pressure adds the following time
        if t + dt + 1 >= time:
            continue
        best = max(best, p * (dt + 1) + maxp(
            target_v, t + dt + 1, p + rates[target_v], visited | {target_v}, dists, time))
    return best

part1 = maxp('AA', 0, 0, {'AA'}, dist, 30)
print(part1)

def powerset(iterable):
    '''From https://docs.python.org/3/library/itertools.html'''
    s = list(iterable)
    return itertools.chain.from_iterable(itertools.combinations(s, r) for r in range(len(s)+1))

subsets = powerset(set(rates.keys()) - {'AA'})

def make_dist_sub(dist, subset):
    dist_sub = {}
    for v in subset:
        dist_sub[v] = {}
        for tv in dist[v]:
            if tv not in subset:
                continue
            dist_sub[v][tv] = dist[v][tv]
    return dist_sub

times = {}
for i, subset in enumerate(subsets):
    # if i % 1000 == 0:
    #     print(' %d' % i)
    dist_sub = make_dist_sub(dist, ('AA',) + subset)
    times[tuple(sorted(subset))] = maxp('AA', 0, 0, {'AA'}, dist_sub, 26)
    # print(subset, times[subset])

part2 = 0
all_nodes = set(rates.keys()) - {'AA'}
for subset, t1 in times.items():
    part2 = max(part2, t1 + times[tuple(sorted(all_nodes - set(subset)))])
print(part2) # 2723?