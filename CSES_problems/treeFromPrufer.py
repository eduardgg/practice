
from heapq import heapify, heappop, heappush
from collections import Counter

n = int(input())
pc = list(map(int, input().split()))
c = Counter(pc)

fulles = [i for i in range(1, n+1) if not c[i]]
heapify(fulles)

for node in pc:
    print(heappop(fulles), node)
    c[node] -= 1
    if c[node] == 0:
        heappush(fulles, node)
        
print(heappop(fulles), heappop(fulles))