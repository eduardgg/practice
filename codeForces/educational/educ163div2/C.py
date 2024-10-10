import sys, random, bisect
from itertools import permutations
from collections import deque, defaultdict
from heapq import heapify, heappop, heappush
from math import gcd, log, sqrt

line = lambda : list(map(int, input().split()))

for _ in range(int(input())):
    n = int(input())
    v = [input(), input()]
    ok = True
    for i in range(n//2):
        if v[1][2*i] == '<' and v[0][2*i+1] == '<':
            ok = False
            break
    for i in range((n-1)//2):
        if v[0][2*i+1] == '<' and v[1][2*i+2] == '<':
            ok = False
            break
    if ok:
        print("YES")
    else:
        print("NO")