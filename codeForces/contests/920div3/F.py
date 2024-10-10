import sys, random, bisect
from collections import deque, defaultdict
from heapq import heapify, heappop, heappush
from itertools import permutations
from math import gcd, log, sqrt
 
mi = lambda :map(int,input().split())
li = lambda :list(mi())

def f(i, d):
    if i >= n:
        return 0
    if A[i][d] != -1:
        return A[i][d]
    A[i][d] = a[i] + f(i+d, d)
    return A[i][d]

for _ in range(int(input())):
    n, q = li()
    a = li()
    A = [[-1 for _ in range(n+1)] for _ in range(n)]
    Q = []
    for _ in range(q):
        s, d, k = li()
        Q.append((s-1, d, k))
    for (s, d, k) in Q:
        suma = - k*f(s+d*k, d)
        for i in range(k):
            suma += f(s+d*i, d)
        print(suma, end=" ")
    print()