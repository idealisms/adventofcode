import collections
import heapq
import itertools
import math
import re

class UnionFind:
    def __init__(self, size):
        """
        Initializes the Union-Find structure with 'size' elements.
        Each element is initially in its own set.
        """
        self.parent = list(range(size))  # parent[i] stores the parent of element i
        self.rank = [1] * size           # rank[i] stores the rank (or size) of the tree rooted at i
        self.size = size

    def find(self, x):
        """
        Finds the representative (root) of the set containing element x.
        Applies path compression to flatten the tree.
        """
        if self.parent[x] == x:
            return x
        self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, x, y):
        """
        Merges the sets containing elements x and y.
        Applies union by rank to keep the tree balanced.
        Returns True if a union occurred, False otherwise (if already in the same set).
        """
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            # Union by rank: attach the smaller rank tree under the root of the larger rank tree
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1  # Increment rank if ranks are equal
            return True
        return False

    def same_set(self, x, y):
        """
        Checks if elements x and y belong to the same set.
        """
        return self.find(x) == self.find(y)

    def count_sets(self):
        """
        Returns the number of disjoint sets currently in the structure.
        """
        num_sets = 0
        for i in range(len(self.parent)):
            if self.parent[i] == i:  # If an element is its own parent, it's a root
                num_sets += 1
        return num_sets

    def part1(self):
        sizes = collections.defaultdict(int)
        for i in range(self.size):
            sizes[self.find(i)] += 1
        return math.prod(list(reversed(sorted(sizes.values())))[:3])

inp = open(re.search(r"day\d\d", __file__)[0] + 'input.txt').read().strip()
pts = []
for line in inp.splitlines():
    pts.append(tuple(map(int, line.split(','))))
N = len(pts)

def dist(a, b):
    return (
        (pts[a][0]-pts[b][0])**2 +
        (pts[a][1]-pts[b][1])**2 +
        (pts[a][2]-pts[b][2])**2)

edges = []
for u in range(N):
    for v in range(u+1, N):
        edges.append((dist(u, v), u, v))
edges.sort()

uf = UnionFind(N)
for i in range(1000):
    _, u, v = edges[i]
    uf.union(u, v)
print(uf.part1())

for i in range(1000, len(edges)):
    _, u, v = edges[i]
    uf.union(u, v)
    if uf.count_sets() == 1:
        print(pts[u][0] * pts[v][0])
        break
