import sys, random, bisect
from collections import deque, defaultdict
from heapq import heapify, heappop, heappush
from itertools import permutations
from math import gcd, log, sqrt
# from sympy import mod_inverse

line = lambda : list(map(int,input().split()))

for _ in range(int(input())):
    n, m = line()
    a = line()
    b = line()
    b.sort()
    b = b[::-1]
    c = []
    i = 0
    j = 0
    while i < n and j < m:
        if b[j] >= a[i]:
            c.append(b[j])
            j += 1
        else:
            c.append(a[i])
            i += 1
    if i < n:
        c += a[i:]
    else:
        c += b[j:]
    
    for e in c:
        print(e, end=" ")
    print()