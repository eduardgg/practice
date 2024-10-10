import sys, random, bisect
from itertools import permutations
from collections import deque, defaultdict
from heapq import heapify, heappop, heappush
from math import gcd, log, sqrt
# from sympy import mod_inverse

line = lambda : list(map(int,input().split()))

for _ in range(int(input())):
    n, m = line()
    if n < m:
        n, m = m, n
    if m == 1:
        if n < 3 or n%2 == 1:
            print("NO")
        else:
            print("YES")
        continue

    if n%2 + m%2 == 2:
        print("NO")
        continue
    if n%2 + m%2 == 0:
        print("YES")
        continue
    if n == 2*m:
        print("NO")
        continue
    print("YES")