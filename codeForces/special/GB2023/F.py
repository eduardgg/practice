import sys, random, bisect
from collections import deque, defaultdict
from heapq import heapify, heappop, heappush
from itertools import permutations
from math import gcd, log
 
mi = lambda :map(int,input().split())
li = lambda :list(mi())

for _ in range(int(input())):
    N0, N1, M = mi()
    graph = defaultdict(list)
    for i in range(M):
        u, v = mi()
        graph[u].append(v)
        graph[v].append(u)
    
    A = {1}
    cand = graph[1]

    while len(A) < N0:
        vists = [False]*(N0+N1)
        v = cand[-1]
        stack = [v]
        quants = 1
        while stack:
            v = stack.pop()
            vists[v-1] = True
            for w in graph[v]:
                if w not in A and not vists[w-1]:
                    vists[w-1] = True
                    stack.append(w)
                    quants += 1
        if quants < N0+N1-len(A):
            cand.pop()
            continue
        else:
            A.add(v)
            for w in graph[v]:
                if w not in cand:
                    cand.append(w)
    
    B = set()
    for v in graph.keys():
        if v not in A:
            B.add(v)
    
    print(*A)
    print(*B)