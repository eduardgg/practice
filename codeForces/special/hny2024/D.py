import sys, random, bisect
from collections import deque, defaultdict
from heapq import heapify, heappop, heappush
from itertools import permutations
from math import gcd, log
 
mi = lambda :map(int,input().split())
li = lambda :list(mi())

for _ in range(int(input())):
    n = int(input())
    b = li()

    zeros = 0
    for e in b:
        if e == 0:
            zeros += 1
            if zeros > 1:
                break
    if zeros != 1:
        print("NO")
        continue

    nxt = [i+1 for i in range(n)]
    prv = [i-1 for i in range(n)]
    nxt[-1], prv[0] = None, None

    v = [(b[i], i) for i in range(n)]
    v.sort()
    correct = True
    while len(v) > 1:
        _, i = v.pop()
        # print(nxt, prv, v, i)
        b1 = prv[i] != None and prv[i] >= 0 and (b[i] - b[prv[i]] in {0, 1}) 
        b2 = nxt[i] != None and nxt[i] < n and (b[i] - b[nxt[i]] in {0, 1})
        if (b1 or b2):
            if prv[i] != None and prv[i] >= 0:
                nxt[prv[i]] = nxt[i]
            if nxt[i] != None and nxt[i] < n:
                prv[nxt[i]] = prv[i]
        else:
            correct = False
            break
    
    if correct:
        print("YES")
    else:
        print("NO")