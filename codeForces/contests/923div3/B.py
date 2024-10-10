import sys, random, bisect
from itertools import permutations
from collections import deque, defaultdict
from heapq import heapify, heappop, heappush
from math import gcd, log, sqrt
# from sympy import mod_inverse

line = lambda : list(map(int,input().split()))

abc = "abcdefghijklmnopqrstuvwxyz"

for _ in range(int(input())):
    n = int(input())
    a = line()
    v = [0]*26
    s = ""
    for i in a:
        for e in range(26):
            if v[e] == i:
                v[e] += 1
                s += abc[e]
                break
    print(s)