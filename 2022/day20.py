import collections
import itertools
import math
import re

inp = open('day20input.txt').read().strip()
_inp = '''1
2
-3
3
-2
0
4'''

class Num(object):
    n = -1
    next = None
    prev = None    

nums = list(map(int, inp.splitlines()))
order = []
zero = None
for n in nums:
    num = Num()
    num.n = n
    order.append(num)
    if n == 0:
        zero = num
def init():
    for i, num in enumerate(order):
        num.next = order[(i+1) % len(nums)]
        num.prev = order[i-1]
init()

def move_forward(num):
    next_num = num.next
    prev_num = num.prev
    next_num.next.prev = num
    num.next = next_num.next
    num.prev = next_num
    prev_num.next = next_num
    next_num.next = num
    next_num.prev = prev_num

def move_backward(num):
    next_num = num.next
    prev_num = num.prev
    prev_num.prev.next = num
    num.next = prev_num
    num.prev = prev_num.prev
    next_num.prev = prev_num
    prev_num.next = next_num
    prev_num.prev = num

def to_list(num):
    lst = []
    for _ in range(len(nums)):
        lst.append(num.n)
        num = num.next
    return lst

def to_list_prev(num):
    lst = []
    for _ in range(len(nums)):
        lst.insert(0, num.n)
        num = num.prev
    return lst

def mix():
    for num in order:
        if num.n > 0:
            for _ in range(num.n % (len(nums) - 1)):
                move_forward(num)
        elif num.n < 0:
            for _ in range(-num.n % (len(nums) - 1)):
                move_backward(num)
        # print(num.n)
        # print(to_list(num))
        # print(to_list_prev(num))

mix()

def coords():
    cur = zero
    for _ in range(1000):
        cur = cur.next
    ans = cur.n
    for _ in range(1000):
        cur = cur.next
    ans += cur.n
    for _ in range(1000):
        cur = cur.next
    ans += cur.n
    return ans
print(coords())

init()
for num in order:
    num.n *= 811589153
for _ in range(10):
    mix()
print(coords())
