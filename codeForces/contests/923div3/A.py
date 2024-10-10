import sys, random, bisect
from itertools import permutations
from collections import deque, defaultdict
from heapq import heapify, heappop, heappush
from math import gcd, log, sqrt
# from sympy import mod_inverse

line = lambda : list(map(int,input().split()))

for _ in range(int(input())):
    n = int(input())
    s = input()
    primer = False
    for i in range(n):
        if s[i] == 'B':
            u = i
            if not primer:
                p = i
            primer = True
    if not primer:
        print(0)
    else:
        print(u-p+1)