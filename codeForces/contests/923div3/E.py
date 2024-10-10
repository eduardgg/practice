import sys, random, bisect
from itertools import permutations
from collections import deque, defaultdict
from heapq import heapify, heappop, heappush
from math import gcd, log, sqrt
# from sympy import mod_inverse

line = lambda : list(map(int,input().split()))

for _ in range(int(input())):
    n, k = line()
    v = [-1]*n
    inf, sup = 1, n
    for i in range(k//2):
        j = 0
        while 2*i+k*j < n:
            v[2*i+k*j] = sup
            sup -= 1
            j += 1
        j = 0
        while 2*i+1+k*j < n:
            v[2*i+1+k*j] = inf
            inf += 1
            j += 1
    for e in v:
        print(e, end=" ")
    print()