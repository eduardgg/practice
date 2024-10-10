import sys, random, bisect
from itertools import permutations
from collections import deque, defaultdict
from heapq import heapify, heappop, heappush
from math import gcd, log, sqrt
# from sympy import mod_inverse

line = lambda : list(map(int,input().split()))

for _ in range(int(input())):
    n, m, k = line()
    if k < n+m-2 or (k-n-m+2) % 2 != 0:
        print("NO")
    else:
        t1, t2 = False, False
        if (n+m)%2 == 0:
            t1 = True
        if (n+m-2-k)%4 == 0:
            t2 = True
        print("YES")
        print("R B "*((m-1)//2) + "R"*((m-1)%2))
        for _ in range(n-3):
            print("B "*(m-1))
        if t1 ^ t2:
            print("B "*(m-1))
            print("B "*(m-1))
        else:
            print("B "*(m-2) + "R")
            print("B "*(m-2) + "R")
        for i in range(n-2):
            c = 'R'
            if (m+i)%2 == 0:
                c = 'B'
            print("B "*(m-1) + c)
        if t1 ^ t2:
            print("B "*(m-2) + "R R")
        else:
            print("B "*(m))