import sys, random, bisect
from itertools import permutations
from collections import deque, defaultdict
from heapq import heapify, heappop, heappush
from math import gcd, log, sqrt

line = lambda : list(map(int, input().split()))

for _ in range(int(input())):
    n, m = line()
    a = []
    for _ in range(n):
        a.append(line())

    todo = []
    for j in range(m-2, -1, -1):
        for i in range(n-1, -1, -1):
            if a[i][j]:
                continue
            if a[(i+1)%n][j+1]:
                if a[(i+1)%n][j] or a[(i+2)%n][j]:
                    a[i][j] = 1
                    if j > 0:
                        todo.append((i, j))

    while todo:
        i, j = todo.pop()
        if a[i][j-1] or a[(i+1)%n][j-1]:
            a[(i-1)%n][j-1] = 1
        if a[(i-1)%n][j+1]:
            a[(i-2)%n][j] = 1

    i, j = 0, 0
    t = 0
    seg = 0
    ok = True
    while j < m-1:
        if not a[(i+t+1)%n][j+1]:
            j += 1
            seg = 0
        elif a[(i+t+1)%n][j] or a[(i+t+2)%n][j]:
            ok = False
            break
        else:
            i += 1
            seg += 1
            if seg > 2*n:
                ok = False
                break
        t += 1
    if not ok:
        print(-1)
        continue
    i %= n
    t += min(n-1-i, i+1)
    print(t)