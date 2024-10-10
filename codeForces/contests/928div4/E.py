import sys, random, bisect
from itertools import permutations
from collections import deque, defaultdict
from heapq import heapify, heappop, heappush
from math import gcd, log, sqrt
# from sympy import mod_inverse

line = lambda : list(map(int,input().split()))

for _ in range(int(input())):
    n, k = line()
    exp = 0
    while k > (n+1)//2:
        k -= (n+1)//2
        exp += 1
        n //= 2
    print((2*k-1)*(2**exp))