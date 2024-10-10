import sys, random, bisect
from collections import deque, defaultdict
from heapq import heapify, heappop, heappush
from itertools import permutations
from math import gcd, log
 
mi = lambda :map(int,input().split())
li = lambda :list(mi())

for _ in range(int(input())):
    n = int(input())
    a = li()
    e1 = a[0]
    e2 = None
    pen = 0
    for i in range(1, len(a)):
        if e2 == None:
            if a[i] > e1:
                e2 = a[i]
            else:
                e1 = a[i]
        else:
            if a[i] <= min(e1, e2):
                if e1 < e2:
                    e1 = a[i]
                else:
                    e2 = a[i]
            elif a[i] <= e1:
                e1 = a[i]
            elif a[i] <= e2:
                e2 = a[i]
            else:
                pen += 1
                if e1 < e2:
                    e1 = a[i]
                else:
                    e2 = a[i]
    print(pen)