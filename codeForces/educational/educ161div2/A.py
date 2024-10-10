import sys, random, bisect
from collections import deque, defaultdict
from heapq import heapify, heappop, heappush
from itertools import permutations
from math import gcd, log, sqrt
 
mi = lambda :map(int,input().split())
li = lambda :list(mi())

for _ in range(int(input())):
    n = int(input())
    a = input()
    b = input()
    c = input()
    match = False
    for i in range(n):
        if a[i] != c[i] and b[i] != c[i]:
            match = True
            break
    if match:
        print("YES")
    else:
        print("NO")
