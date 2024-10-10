import sys, random, bisect
from collections import deque, defaultdict
from heapq import heapify, heappop, heappush
from itertools import permutations
from math import gcd, log, sqrt
# from sympy import mod_inverse

line = lambda : list(map(int,input().split()))

for _ in range(int(input())):
    n = int(input())
    a = line()
    b = []
    q = [0]*100
    primer = None
    segon = None
    for i in a:
        q[i-1] += 1
        if q[i-1] == 1:
            b.append(1)
        elif primer in {None, i}:
            primer = i
            b.append(2)
        else:
            segon = i
            b.append(3)
    if not primer or not segon:
        print(-1)
    else:
        for e in b:
            print(e, end=" ")
        print()