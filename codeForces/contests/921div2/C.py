import sys, random, bisect
from collections import deque, defaultdict
from heapq import heapify, heappop, heappush
from itertools import permutations
from math import gcd, log, sqrt
 
line = lambda : list(map(int,input().split()))

for _ in range(int(input())):
    n, k, m = line()
    s = input()
    abc = "abcdefghijklmnopqrstuvwxyz"
    vists = set()
    paraula = ""
    i = 0
    while i < m:
        if len(paraula) >= n:
            break
        if s[i] not in vists:
            vists.add(s[i])
            if len(vists) == k:
                paraula += s[i]
                vists = set()
        i += 1

    if len(paraula) >= n:
        print("YES")
    else:
        print("NO")
        for i in abc:
            if i not in vists:
                paraula += i
                break
        print(paraula)