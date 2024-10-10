import sys, random, bisect
from collections import deque, defaultdict
from heapq import heapify, heappop, heappush
from itertools import permutations
from math import gcd, log
 
mi = lambda :map(int,input().split())
li = lambda :list(mi())

for _ in range(int(input())):
    n, k, x = li()
    a = li()
    a.sort()

    suma = sum(a[:n-x]) - sum(a[n-x:])
    topSuma = suma
    for i in range(k):
        nou = 0
        if n-1-i-x >= 0:
            nou += a[n-1-i-x]
        suma = suma + a[n-1-i] - 2*nou
        if suma > topSuma:
            topSuma = suma

    print(topSuma)