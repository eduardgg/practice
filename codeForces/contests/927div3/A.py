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
    t = 0
    c = 0
    for i in s:
        if i == '*':
            t += 1
            if t == 2:
                break 
            continue
        t = 0
        if i == '@':
            c += 1
    print(c)