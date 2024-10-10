import sys, random, bisect
from itertools import permutations
from collections import deque, defaultdict
from heapq import heapify, heappop, heappush
from math import gcd, log, sqrt

line = lambda : list(map(int, input().split()))

for _ in range(int(input())):
    n = int(input())
    a = line()
    b = [(a[i], i) for i in range(n)]
    b.sort()
    suma = 0
    c = []
    ans = [n-1]*n
    for i in range(n-1):
        suma += b[i][0]
        if suma < b[i+1][0]:
            j = i
            while j>=0 and ans[b[j][1]] == n-1:
                ans[b[j][1]] = i
                j -= 1
    print(*ans)