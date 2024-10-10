import sys, random, bisect
from itertools import permutations
from collections import deque, defaultdict
from heapq import heapify, heappop, heappush
from math import gcd, log, sqrt
# from sympy import mod_inverse

line = lambda : list(map(int,input().split()))

for _ in range(int(input())):
    n = int(input())
    a = line()
    time = a[0]
    for e in a[1:]:
        if time%e == 0:
            time += e
        else:
            time = e*(time//e + 1)
    print(time)
