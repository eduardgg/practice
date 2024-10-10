import sys, random, bisect
from itertools import permutations
from collections import deque, defaultdict
from heapq import heapify, heappop, heappush
from math import gcd, log, sqrt
# from sympy import mod_inverse

line = lambda : list(map(int,input().split()))
n, q = line()
a = line()

for _ in range(q):
    k = int(input())
    
    M = max(a)
    S = sum(a)
    if k >= M*n - S:
        k -= (M*n - S)
        print(M + k//n)
        continue
    
    
    aa = [e for e in a]
    for i in range(19, -1, -1):
        cc = 0
        aaa = [e for e in aa]
        for j in range(n):
            if aaa[j]&(1<<i) == 0:
                inc = (1<<i) - (aaa[j]&((1<<i)-1))
                cc += inc
                aaa[j] += inc
        if cc <= k:
            k -= cc
            aa = [e for e in aaa]

    top = aa[0]
    for e in aa:
        top &= e
    print(top)