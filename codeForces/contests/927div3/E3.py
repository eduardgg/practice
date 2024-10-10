import sys, random, bisect
from itertools import permutations
from collections import deque, defaultdict
from heapq import heapify, heappop, heappush
from math import gcd, log, sqrt
# from sympy import mod_inverse

line = lambda : list(map(int,input().split()))

for _ in range(int(input())):
    n = int(input())
    s = input()
    
    suma = 0
    for c in s:
        suma += int(c)
    
    ans = []
    por = 0
    i = 0
    while suma+por > 0:
        ans.append((suma+por)%10)
        por = (suma+por)//10
        if i < n:
            suma -= int(s[n-1-i])
            i += 1
    
    ans = ans[::-1]
    for i in range(len(ans)):
        if ans[i] != 0:
            for j in range(i, len(ans)):
                print(ans[j], end="")
            break
    print()