
import heapq

t = int(input())
for _ in range(t):
    n, m = list(map(int, input().split()))    
    
    g = {}
    for _ in range(m):
        u, v, w = list(map(int, input().split()))
        g[u-1] = g.get(u-1, []) + [(v-1, w)]
        g[v-1] = g.get(v-1, []) + [(u-1, w)]
    s = list(map(int, input().split()))
    
    heap = [(0, 0, s[0])]
    while heap:
        (t, u, b) = heapq.heappop(heap)
        if u == n-1:
            print(t)
            break
        for (v, w) in g[u]:
            heapq.heappush(heap, (t + w*b, v, min(b, s[v])))