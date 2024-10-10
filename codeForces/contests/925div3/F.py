import sys, random, bisect
from itertools import permutations
from collections import deque, defaultdict
from heapq import heapify, heappop, heappush
from math import gcd, log, sqrt
# from sympy import mod_inverse

line = lambda : list(map(int,input().split()))

for _ in range(int(input())):
    n, k = line()
    ok = True
    a = line()

    if k == 1:
        print("YES")
        continue
    
    b = line()
    c = []
    i = 1

    while i < n and a[i] == b[i]:
        i += 1
    if a[i] == b[0] and b[i] != a[0]:
        v = a[1:i+1] + b[i:]
    elif a[i] != b[0] and b[i] == a[0]:
        v = b[1:i+1] + a[i:]
    elif k == 2:
        j = i+1
        while j < n:
            if a[j] != b[j]:
                ok = False
                break
            j += 1
        if not ok:
            print("NO")
        else:
            print("YES")
        continue
    else:
        c = line()
        for e in c:
            if e == a[0]:
                v = a[1:i] + [a[0], b[0]] + b[i+1:]
                break
            elif e == b[0]:
                v = a[1:i] + [b[0], a[0]] + b[i+1:]
                break

    j = 0
    for i in range(n-1):
        if a[i+1] == v[i+j]:
            continue
        elif j == 1:
            ok = False
            break
        elif v[i] == a[0]:
            j = 1
        else:
            ok = False
            break

    j = 0
    for i in range(n-1):
        if b[i+1] == v[i+j]:
            continue
        elif j == 1:
            ok = False
            break
        elif v[i] == b[0]:
            j = 1
        else:
            ok = False
            break

    if ok and k == 2:
        print("YES")
        continue

    if len(c) == 0:
        c = line()

    j = 0
    for i in range(n-1):
        if c[i+1] == v[i+j]:
            continue
        elif j == 1:
            ok = False
            break
        elif v[i] == c[0]:
            j = 1
        else:
            ok = False
            break

    for _ in range(k-3):
        w = line()
        j = 0
        for i in range(n-1):
            if w[i+1] == v[i+j]:
                continue
            elif j == 1:
                ok = False
                break
            elif v[i] == w[0]:
                j = 1
            else:
                ok = False
                break

    if not ok:
        print("NO")
    else:
        print("YES")