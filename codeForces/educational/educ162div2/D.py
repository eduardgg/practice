import sys, random, bisect
from itertools import permutations
from collections import deque, defaultdict
from heapq import heapify, heappop, heappush
from math import gcd, log, sqrt

line = lambda : list(map(int, input().split()))

def dp(a):

    n = len(a)
    sumes = [0]
    first = [0]
    for i in range(n):
        sumes.append(sumes[-1] + a[i])
        if i > 0:
            if a[i] == a[i-1]:
                first.append(first[-1])
            else:
                first.append(i)

    v = [-1]*n
    for k in range(1, n):
        if a[k-1] > a[k]:
            v[k] = 1
            continue
        if sumes[k] <= a[k] or (k > 1 and first[k-1] == 0):
            continue
        i, j = 0, k
        while i <= j:
            m = (i + j) // 2
            if sumes[k]-sumes[m] > a[k]:
                i = m+1
            else:
                j = m-1
        v[k] = max(k-i+1, k-first[k-1]+1)
    
    return v

for _ in range(int(input())):
    n = int(input())
    a = line()
    
    dpl = dp(a)
    dpr = dp(a[::-1])[::-1]

    ans = []
    for i in range(n):
        if dpl[i] > 0 and dpr[i] > 0:
            ans.append(min(dpl[i], dpr[i]))
        else:
            ans.append(max(dpl[i], dpr[i]))
    print(*ans)