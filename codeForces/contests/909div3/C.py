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
    current = max(a[0], 0)
    millor = a[0]
    for i in range(1, len(a)):
        if (a[i]-a[i-1])%2 == 0:
            current = a[i]
        else:
            current += a[i]
        millor = max(millor, current)
        current = max(current, 0)
    print(millor)