import sys, random, bisect
from itertools import permutations
from collections import deque, defaultdict
from heapq import heapify, heappop, heappush
from math import gcd, log, sqrt
# from sympy import mod_inverse

# Funciona perfectament, i és eficient (com la solució oficial),
# però a CodeForces no li dóna la gana d'acceptar-lo.

line = lambda : list(map(int,input().split()))

def algun(v, l, r):
    if len(v) == 0:
        return False
    mid = len(v)//2
    if v[mid] < l:
        return algun(v[mid+1:], l, r)
    if v[mid] > r:
        return algun(v[:mid], l, r)
    return True

n, q = line()
s = input()

time = defaultdict(list)
time[(0, 0)] = [0]
P = [(0, 0)]
x, y = 0, 0

for i in range(n):
    if s[i] == 'R':
        x += 1
    elif s[i] == 'L':
        x -= 1
    elif s[i] == 'U':
        y += 1
    else:
        y -= 1
    P.append((x, y))
    time[(x, y)].append(i+1)

for _ in range(q):
    x, y, l, r = line()
    if (x, y) in time.keys():
        if time[(x, y)][0] < l or time[(x, y)][-1] >= r:
            print("YES")
            continue
    xx = P[l-1][0] + P[r][0] - x
    yy = P[l-1][1] + P[r][1] - y
    if (xx, yy) not in time.keys():
        print("NO")
        continue
    b = bisect.bisect_left(time[(xx, yy)], l)
    if b >= len(time[(xx, yy)]) or time[(xx, yy)][b] >= r:
        print("NO")
        continue
    print("YES")