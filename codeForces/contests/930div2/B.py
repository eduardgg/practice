import sys, random, bisect
from itertools import permutations
from collections import deque, defaultdict
from heapq import heapify, heappop, heappush
from math import gcd, log, sqrt

line = lambda : list(map(int, input().split()))

for _ in range(int(input())):
    n = int(input())
    a = []
    a.append(input())
    a.append(input())
    i = 0
    ld = -1
    v = [a[0][0]]
    while i < n-1:
        if a[0][i+1] == a[1][i]:
            v.append(a[0][i+1])
        else:
            if a[0][i+1] < a[1][i]:
                ld = i
                v.append(a[0][i+1])
            else:
                break
        i += 1
    ans = i-ld
    while i < n:
        v.append(a[1][i])
        i += 1

    for e in v:
        print(e, end="")
    print()
    print(ans)