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
    l = max(a)
    r = sum(a)
    while l < r:
        m = (l+r)//2
        ok = True
        v = [a[0]]
        for i in range(1, n):
            minim = float('inf')
            suma = 0
            j = 1
            while i-j >= 0 and suma <= m:
                minim = min(minim, v[i-j] + a[i])
                suma += a[i-j]
                j += 1
            if suma <= m:
                minim = a[i]
            v.append(minim)
        s = 0
        i = 0
        ok = False
        while s <= m:
            if v[-1-i] <= m:
                ok = True
                break
            s += a[-1-i]
            i += 1
        if ok:
            r = m
        else:
            l = m+1
        # print(m, v)
    print(r)