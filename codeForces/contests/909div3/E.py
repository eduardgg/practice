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
    ok = True
    i = 0
    l = n-1
    while i < l:
        while a[i] <= a[l]:
            l -= 1
            if i == l:
                i -= 1
                break
            if a[l] > a[l+1]:
                ok = False
                break
        if not ok:
            break
        i += 1
    
    if not ok:
        print(-1)
    else:
        print(i)  