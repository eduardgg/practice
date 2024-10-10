import sys, random, bisect
from collections import deque, defaultdict
from heapq import heapify, heappop, heappush
from itertools import permutations
from math import gcd, log, sqrt
# from sympy import mod_inverse

line = lambda : list(map(int,input().split()))

for _ in range(int(input())):
    n, k = line()
    b = line()
    shift = 0
    ans = True
    vistos = [False]*len(b)
    for _ in range(k):
        if b[n-1-shift] > n:
            ans = False
            break
        if vistos[n-1-shift]:
            break
        vistos[n-1-shift] = True
        shift += b[n-1-shift]
        shift %= n
    if ans:
        print("YES")
    else:
        print("NO")
