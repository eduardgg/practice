import sys, random, bisect
from collections import deque, defaultdict
from heapq import heapify, heappop, heappush
from itertools import permutations
from math import gcd, log, sqrt
 
mi = lambda :map(int,input().split())
li = lambda :list(mi())

def bin(n, k):
    if k < 0 or k > n:
        return 0
    result = 1
    for i in range(1, min(k, n - k) + 1):
        result = (result * (n - i + 1)) // i
    return result

for _ in range(int(input())):
    n = int(input())
    a = li()
    a.sort()
    g = {}
    for e in a:
        g[e] = g.get(e, 0) + 1
    result = 0
    suma = 0
    for e in g.keys():
        result += bin(g[e], 3)
        result += bin(g[e], 2)*suma
        suma += g[e]
    print(result)