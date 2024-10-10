import sys, random, bisect
from collections import deque, defaultdict
from heapq import heapify, heappop, heappush
from itertools import permutations
from math import gcd, log, sqrt
 
mi = lambda :map(int,input().split())
li = lambda :list(mi())

for _ in range(int(input())):
    n = int(input())
    sq = int(sqrt(n)) + 1
    a = li()
    result = 0
    altres = []

    for i in range(1, sq):
        if n%i != 0:
            continue
        altres.append(n//i)
        m = 0
        for j in range(n-i):
            m = gcd(m, abs(a[j]-a[j+i]))
            if m == 1:
                break
        if m != 1:
            result += 1

    if altres[-1]**2 == n:
        altres.pop()
        
    for i in altres:
        if n%i != 0:
            continue
        m = 0
        for j in range(n-i):
            m = gcd(m, abs(a[j]-a[j+i]))
            if m == 1:
                break
        if m != 1:
            result += 1

    print(result)