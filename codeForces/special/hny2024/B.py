import sys, random, bisect
from collections import deque, defaultdict
from heapq import heapify, heappop, heappush
from itertools import permutations
from math import gcd, log
 
mi = lambda :map(int,input().split())
li = lambda :list(mi())

for _ in range(int(input())):
    x = int(input())
    s = input()
    suma = 0
    for c in s:
        if c == '+':
            suma += 1
        else:
            suma -= 1
    print(abs(suma))