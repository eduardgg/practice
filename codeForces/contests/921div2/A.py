import sys, random, bisect
from collections import deque, defaultdict
from heapq import heapify, heappop, heappush
from itertools import permutations
from math import gcd, log, sqrt
 
line = lambda : list(map(int,input().split()))

for _ in range(int(input())):
    n, k = line()
    abc = "abcdefghijklmnopqrstuvwxyz"
    print(abc[:k]*n)