import sys, random, bisect
from itertools import permutations
from collections import deque, defaultdict
from heapq import heapify, heappop, heappush
from math import gcd, log, sqrt

line = lambda : list(map(int, input().split()))

abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for _ in range(int(input())):
    n = int(input())
    if n%2 == 1:
        print("NO")
        continue
    else:
        print("YES")
        i = 0
        while i < n//2:
            print(abc[i], end="")
            print(abc[i], end="")
            i += 1
        print()
