import sys, random, bisect
from itertools import permutations
from collections import deque, defaultdict
from heapq import heapify, heappop, heappush
from math import gcd, log, sqrt

line = lambda : list(map(int, input().split()))

for _ in range(int(input())):
    n = int(input())
    a = line()
    q = int(input())

    s = [0]
    for e in a:
        s.append(s[-1] + e)
    
    #print(s)
    ans = []
    for _ in range(q):
        l, u = line()
        i = bisect.bisect_left(s, u+s[l-1])

        #print("debug", i, u, s[i-1], s[l-1])
        #if i<n:
        #    print(a[i-1])

        if i > n:
            ans.append(n)
        elif i <= l:
            ans.append(i)
        elif s[i] == s[l-1] + u:
            ans.append(i)
        elif u - (s[i-1] - s[l-1]) < (a[i-1]+1)//2:
            ans.append(i-1)
        else:
            ans.append(i)
    print(*ans)