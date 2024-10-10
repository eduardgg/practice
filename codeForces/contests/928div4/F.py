import sys, random, bisect
from itertools import permutations
from collections import deque, defaultdict
from heapq import heapify, heappop, heappush
from math import gcd, log, sqrt
# from sympy import mod_inverse

line = lambda : list(map(int,input().split()))

for _ in range(int(input())):
    m = []
    for i in range(7):
        s = input()
        m.append([e for e in s])
    kill = 0
    while True:
        count = [[0 for _ in range(7)] for _ in range(7)]
        for i in range(5):
            for j in range(5):
                if m[i][j] == 'B' and m[i][j+2] == 'B' and m[i+2][j] == 'B' and m[i+2][j+2] == 'B' and m[i+1][j+1] == 'B':
                    count[i][j] += 1
                    count[i][j+2] += 1
                    count[i+2][j] += 1
                    count[i+1][j+1] += 1
                    count[i+2][j+2] += 1
        mi, mj = 0, 0
        for i in range(7):
            for j in range(7):
                if count[i][j] > count[mi][mj]:
                    mi, mj = i, j

        if count[mi][mj] == 0:
            break
        else:
            kill += 1
            m[mi][mj] = 'W'
    print(kill)
    