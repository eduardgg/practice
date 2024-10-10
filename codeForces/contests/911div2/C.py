import sys, random, bisect
from itertools import permutations
from collections import deque, defaultdict
from heapq import heapify, heappop, heappush
from math import gcd, log, sqrt
# from sympy import mod_inverse

line = lambda : list(map(int,input().split()))

for _ in range(int(input())):
    n = int(input())
    s = "x" + input()
    left, right, up = [0]*(n+1), [0]*(n+1), [0]*(n+1)
    for i in range(1, n+1):
        a, b = line()
        left[i] = a
        right[i] = b
        up[a] = i
        up[b] = i

    stack = [(1, 0)]
    minim = float('inf')
    while stack:
        e, c = stack.pop()
        if right[e] + left[e] == 0:
            minim = min(minim, c)
            continue
        if right[e] != 0:
            stack.append((right[e], c + int(s[e] != 'R')))
        if left[e] != 0:
            stack.append((left[e], c + int(s[e] != 'L')))
    
    print(minim)