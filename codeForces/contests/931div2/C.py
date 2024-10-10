import sys, random, bisect
from itertools import permutations
from collections import deque, defaultdict
from heapq import heapify, heappop, heappush
from math import gcd, log, sqrt

line = lambda : list(map(int, input().split()))

for _ in range(int(input())):
    n, m = line()
    print("?", 1, 1)
    md1 = int(input())
    print("?", 1, m)
    md2 = int(input())
    print("?", n, 1)
    md3 = int(input())
    if md1+md2 >= m-1 and md1+md3 >= n-1:
        y = 1+(md1+md3-(n-1))//2
        x = md1-y+2
        print("?", x, y)
        md4 = int(input())
        if md4 == 0:
            print("!", x, y)
        else:
            x = 1+(md1+md2-(m-1))//2
            y = md1-x+2
            print("!", x, y)
    elif md1+md2 < m-1:
        y = 1+(md1+md3-(n-1))//2
        x = md1-y+2
        print("!", x, y)
    else:
        x = 1+(md1+md2-(m-1))//2
        y = md1-x+2
        print("!", x, y)
        
