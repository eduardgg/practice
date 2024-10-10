
from heapq import heappop, heappush

def dijkstra(i):
    dist = [float('inf')]*(n+1)
    heap = []
    c = [i in a for i in range(n+1)]
    heappush(heap, (0, i, c[i]))
    while heap:
        d, u, b = heappop(heap)
        if d < dist[u] or (b and not c[u]):
            if d < dist[u]: dist[u] = d
            else: c[u] = True
            for v, w in g[u]:
                t = d + (w//2 if b else w)
                if t < dist[v] or (b and not c[v]):
                    heappush(heap, (t, v, b or c[v]))
    return dist

for _ in range(int(input())):
    n, m, h = list(map(int, input().split()))
    a = set(map(int, input().split()))
    g = [[] for _ in range(n+1)]
    for i in range(m):
        ui, vi, wi = list(map(int, input().split()))
        g[ui].append((vi, wi))
        g[vi].append((ui, wi))
    d1 = dijkstra(1)
    dn = dijkstra(n)
    if d1[n] == float('inf'):
        print(-1)
    else:
        ans = min([max(d1[i], dn[i]) for i in range(1, n+1)])
        print(ans)