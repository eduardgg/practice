import sys, random, bisect
from itertools import permutations
from collections import deque, defaultdict
from heapq import heapify, heappop, heappush
from math import gcd, log, sqrt
# from sympy import mod_inverse

# Sembla que aquest sigui millor però encara falla en alguns casos.
# Si hi ha una cadena de C, un extrem està unit amb uns quants 'S' i
# l'altre extrem amb alguns 'P', la resposta seria 1, però aquest codi
# convertiria totes les C en la millor entre S i P, fent que s'obtingui
# com a resposta min(#S, #P), clarament superior a 1.

line = lambda : list(map(int,input().split()))

for _ in range(int(input())):
    n = int(input())
    a = line()
    s = "X" + input()
    T = [[] for _ in range(n+1)]
    status = [c for c in s]
    for i in range(n-1):
        T[a[i]].append(i+2)
        T[i+2].append(a[i])

    for i in range(1, n+1):
        if status[i] == 'C':
            p, s = 0, 0
            comodins = {i}
            stack = [i]
            while stack:
                v = stack.pop()
                for w in T[v]:
                    if status[w] == 'P':
                        p += 1
                    elif status[w] == 'S':
                        s += 1
                    elif w not in comodins:
                        comodins.add(w)
                        stack.append(w)
                if p != s:
                    break
            for e in comodins:
                if s > p:
                    status[e] = 'S'
                else:
                    status[e] = 'P'

    # Ara tots els vèrtexs tenen status S o P.
    # Serà tan senzill com trobar el nombre de canvis S-P

    walls = 0
    stack = [1]
    visited = set()
    while stack:
        v = stack.pop()
        visited.add(v)
        for w in T[v]:
            if w not in visited:
                stack.append(w)
                if status[w] != status[v]:
                    walls += 1

    print(walls)