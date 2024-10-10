import sys, random, bisect
from itertools import permutations
from collections import deque, defaultdict
from heapq import heapify, heappop, heappush
from math import gcd, log, sqrt
# from sympy import mod_inverse

line = lambda : list(map(int,input().split()))

for _ in range(int(input())):
    n, P, l, t = line()
    nt = (n-1)//7 + 1


    if (l+2*t)*(nt//2) >= P:
        d = P // (l+2*t)
        if P % (l+2*t) != 0:
            d += 1
        print(n-d)
        continue
    
    d = nt//2
    P -= (l+2*t)*d
    
    d += 1
    P -= (l+t*(nt%2))

    if P <= 0:
        print(n-d)
        continue

    d += P // l
    P -= (P//l)*l
    
    if P == 0:
        print(n-d)
    else:
        d += 1
        print(n-d)