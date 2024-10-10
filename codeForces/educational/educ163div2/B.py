import sys, random, bisect
from itertools import permutations
from collections import deque, defaultdict
from heapq import heapify, heappop, heappush
from math import gcd, log, sqrt

line = lambda : list(map(int, input().split()))

for _ in range(int(input())):
    n = int(input())
    a = line()
    if a[0]%10 < a[0]//10:
        e = a[0]
    else:
        e = a[0]%10
    
    ok = True
    for f in a[1:]:
        if f < e:
            ok = False
            break
        if f%10 >= f//10 >= e:
            e = f%10
        else:
            e = f
    if ok:
        print("YES")
    else:
        print("NO")