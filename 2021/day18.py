import collections
import itertools
import math
import re

inp = open(re.search(r"day\d\d", __file__)[0] + 'input.txt').read().strip()

# inp = '''[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]
# [7,[[[3,7],[4,3]],[[6,3],[8,8]]]]
# [[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]]
# [[[[2,4],7],[6,[0,5]]],[[[6,8],[2,8]],[[2,1],[4,5]]]]
# [7,[5,[[3,8],[1,4]]]]
# [[2,[2,2]],[8,[8,1]]]
# [2,9]
# [1,[[[9,3],9],[[9,0],[0,7]]]]
# [[[5,[7,4]],7],1]
# [[[[4,2],2],6],[8,7]]'''

# inp = '''[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]
# [[[5,[2,8]],4],[5,[[9,9],0]]]
# [6,[[[6,2],[5,6]],[[7,6],[4,7]]]]
# [[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]
# [[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]
# [[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]
# [[[[5,4],[7,7]],8],[[8,3],8]]
# [[9,3],[[9,9],[6,[4,9]]]]
# [[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]
# [[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]'''
# inp = '''[1,1]
# [2,2]
# [3,3]
# [4,4]
# [5,5]
# [6,6]'''

def solveWithTrees(inp):
    class Node(object):
        value = None
        left = None
        right = None
        parent = None

        def __str__(self):
            if self.value is not None:
                return str(self.value)
            else:
                return '[{},{}]'.format(str(self.left), str(self.right))

        def isLeftChild(self):
            if self.parent is None:
                return False
            return self == self.parent.left

        def isRightChild(self):
            if self.parent is None:
                return False
            return self == self.parent.right

        def height(self):
            height = 0
            p = self.parent
            while p is not None:
                height += 1
                p = p.parent
            return height

        def checkHeights(self):
            if self.value is not None:
                print('node {} has a height of {}'.format(self.value, self.height()))
            else:
                self.left.checkHeights()
                self.right.checkHeights()

        def traverse(self, acc):
            if self.value is not None:
                acc.append(self)
                return
            else:
                self.left.traverse(acc)
                self.right.traverse(acc)

        def explode(self):
            orderedValueNodes = []
            self.traverse(orderedValueNodes)
            for i, (n1, n2) in enumerate(zip(orderedValueNodes, orderedValueNodes[1:])):
                if n1.parent == n2.parent and n1.height() > 4:
                    if i > 0:
                        orderedValueNodes[i-1].value += n1.value
                    if i + 2 < len(orderedValueNodes):
                        orderedValueNodes[i+2].value += n2.value
                    n1.parent.value = 0
                    n1.parent.left = n1.parent.right = None
                    return True
            return False

        def split(self):
            orderedValueNodes = []
            self.traverse(orderedValueNodes)
            for n in orderedValueNodes:
                if n.value > 9:
                    n.left = Node()
                    n.left.value = n.value // 2
                    n.left.parent = n
                    n.right = Node()
                    n.right.value = n.value // 2 if n.value % 2 == 0 else (n.value + 1) // 2
                    n.right.parent = n
                    n.value = None
                    return True
            return False

        def magnitude(self):
            if self.value is not None:
                return self.value
            else:
                return self.left.magnitude() * 3 + self.right.magnitude() * 2

    def buildTree(line):
        if line[0] in '0123456789':
            n = Node()
            n.value = int(line[0])
            return n, line[1:]
        if line[0] == '[':
            n = Node()
            n.left, line = buildTree(line[1:])
            n.left.parent = n
            assert line[0] == ','
            n.right, line = buildTree(line[1:])
            n.right.parent = n
            assert line[0] == ']'
            return n, line[1:]
        assert False, 'Should not be here'

    def addition(n1, n2):
        n = Node()
        n.left = n1
        n.left.parent = n
        n.right = n2
        n.right.parent = n
        return n

    snums = []
    for line in inp.splitlines():
        n, _ = buildTree(line)
        snums.append(n)
    # print(snums[0])

    def sreduce(tree):
        changed = True
        while changed:
            # print(tree)
            changed = tree.explode()
            if not changed:
                changed = tree.split()
        return tree

    cur = snums[0]
    for snum in snums[1:]:
        cur = addition(cur, snum)
        # cur.checkHeights()
        sreduce(cur)

    # Part 1
    print(cur.magnitude())  # 4289


    lines = inp.splitlines()
    part2 = 0
    for i, snum1 in enumerate(lines):
        for snum2 in lines[i+1:]:
            part2 = max(part2, sreduce(addition(buildTree(snum1)[0], buildTree(snum2)[0])).magnitude())
            part2 = max(part2, sreduce(addition(buildTree(snum2)[0], buildTree(snum1)[0])).magnitude())
    print(part2)  # 4807

##########################################################
##########################################################
# Start alternate solution using lists.
##########################################################
##########################################################

def solveWithLists(inp):
    snums = []
    for line in inp.splitlines():
        snum = []
        for c in line:
            if c == ',':
                continue
            if c in '[]':
                snum.append(c)
            else:
                snum.append(int(c))
        snums.append(snum)

    def isNum(n):
        return str(n) not in '[]'

    def sexplode(cur):
        while True:
            has_changed = False
            # print(cur)
            for i, (a, b) in enumerate(zip(cur, cur[1:])):
                if isNum(a) and isNum(b):
                    depth = cur[:i].count('[') - cur[:i].count(']')
                    if depth < 5:
                        continue
                    for j in range(i - 1, -1, -1):
                        if isNum(cur[j]):
                            cur[j] += a
                            break
                    for j in range(i + 2, len(cur)):
                        if isNum(cur[j]):
                            cur[j] += b
                            break
                    cur = cur[:i - 1] + [0] + cur[i+3:]
                    # print('explode:', snumstr(cur))
                    has_changed = True
                    break
            if not has_changed:
                break

        # print(cur)
        return cur

    def ssplit(cur):
        for i, n in enumerate(cur):
            if isNum(n) and n > 9:
                cur = cur[:i] + ['[', n // 2, n // 2 if n % 2 == 0 else (n // 2) + 1, ']'] + cur[i+1:]
                # print('split:', snumstr(cur))
                break
        return cur

    def snumstr(snum):
        return ' '.join(map(str, snum))

    def sreduce(cur):
        while True:
            before = cur
            cur = sexplode(cur)
            cur = ssplit(cur)
            if before == cur:
                break
        return cur

    def addsnums(a, b):
        return ['['] + a + b + [']']

    cur = snums[0]
    for snum in snums[1:]:
        cur = addsnums(cur, snum)
        # print('addition:', snumstr(cur))
        cur = sreduce(cur)
    # print('final', snumstr(cur))

    def magnitude(cur):
        while len(cur) > 1:
            for i, (a, b) in enumerate(zip(cur, cur[1:])):
                if isNum(a) and isNum(b):
                    cur = cur[:i-1] + [3*a + 2*b] + cur[i+3:]
                    break
        return cur[0]

    part1 = magnitude(cur)
    print(part1)

    part2 = 0
    for i in range(len(snums)):
        for j in range(i+1, len(snums)):
            part2 = max(part2, magnitude(sreduce(addsnums(snums[i], snums[j]))))
            part2 = max(part2, magnitude(sreduce(addsnums(snums[j], snums[i]))))
    print(part2)

print('With trees:')
solveWithTrees(inp)  # ~3.3s
print('With lists:')
solveWithLists(inp)  # ~4.6s