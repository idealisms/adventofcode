import collections
import heapq
import itertools
import math
import re

inp = open(re.search(r"day\d\d", __file__)[0] + 'input.txt').read().strip()
# inp = '''jqt: rhn xhk nvd
# rsh: frs pzl lsr
# xhk: hfx
# cmg: qnr nvd lhk bvb
# rhn: xhk bvb hfx
# bvb: xhk hfx
# pzl: lsr hfx nvd
# qnr: nvd
# ntq: jqt hfx bvb xhk
# nvd: lhk
# lsr: lhk
# rzs: qnr cmg lsr rsh
# frs: qnr lhk lsr'''

graph = collections.defaultdict(set)
nodes = set()
edges = set()
for line in inp.splitlines():
    tokens = line.replace(':', '').split()
    nodes.add(tokens[0])
    for rhs in tokens[1:]:
        graph[tokens[0]].add(rhs)
        graph[rhs].add(tokens[0])
        nodes.add(rhs)
        edges.add(tuple(sorted((tokens[0], rhs))))

# print('graph {')
# for n in nodes:
#     edges_ = [edge for edge in graph[n] if edge > n]
#     if edges_:
#         print(n, '-- {', ' '.join(edges_), '}')
# print('}')
# dot -Tsvg < day25.dot > day25.svg
# View the svg file in chrome. There are three lines that cross
# the middle. Hover over them to see which nodes they connect.

edges_to_remove = (
    ('gqr', 'vbk'),
    ('klj', 'scr'),
    ('mxv', 'sdv'),
)
for (a, b) in edges_to_remove:
    graph[a].remove(b)
    graph[b].remove(a)

sub_graph = set()
q = [next(iter(nodes))]
while q:
    n = q.pop(0)
    if n in sub_graph:
        continue
    sub_graph.add(n)
    q.extend(graph[n])
print(len(sub_graph) * (len(nodes) - len(sub_graph)))
