import sys, random, bisect
from itertools import permutations
from collections import deque, defaultdict
from heapq import heapify, heappop, heappush
from math import gcd, log, sqrt
# from sympy import mod_inverse

line = lambda : list(map(int,input().split()))

for _ in range(int(input())):
    n, m = line()
    a = line()
    s = input()
    s = s[:n-1]
    i, j = 0, n-1
    for e in s:
        if e == 'L':
            i += 1
        else:
            j -= 1
    s = s[::-1]
    ans = []
    prod = a[i]%m
    ans.append(prod)
    for e in s:
        if e == 'L':
            i -= 1
            prod *= a[i]
        else:
            j += 1
            prod *= a[j]
        prod %= m
        ans.append(prod)
    ans = ans[::-1]
    print(*ans)