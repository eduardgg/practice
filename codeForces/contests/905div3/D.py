
from heapq import heappop, heappush
from collections import defaultdict

minr, maxl = [], []
ldel, rdel = defaultdict(int), defaultdict(int)

q = int(input())
for _ in range(q):
    a = input().split()
    if a[0] == '+':
        heappush(maxl, -int(a[1]))
        heappush(minr, int(a[2]))
    else:
        ldel[int(a[1])] += 1
        rdel[int(a[2])] += 1
        while maxl and ldel.get(-maxl[0], 0):
            ldel[-heappop(maxl)] -= 1
        while minr and rdel.get(minr[0], 0):
            rdel[heappop(minr)] -= 1
    
    if (minr and maxl and minr[0] < -maxl[0]):
        print("YES")
    else:
        print("NO")