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
    if n > 53:
        a = n-52
    else:
        a = 1
    if n-a > 27:
        b = n-a-26
    else:
        b = 1
    c = n-a-b
    print(abc[a-1] + abc[b-1] + abc[c-1])
    