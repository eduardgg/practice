
from heapq import heappop, heappush
for _ in range(int(input())):
    n, m = list(map(int, input().split()))
    t0, t1, t2 = list(map(int, input().split()))
    g = [[] for _ in range(n+1)]
    for _ in range(m):
        u, v, l1, l2 = list(map(int, input().split()))
        g[u].append((v, l1, l2))
        g[v].append((u, l1, l2))
    best = [float('inf')]*n + [0]
    fet = [False]*n + [True]
    heap = [(0, n)]
    while heap:
        t, u = heappop(heap)
        fet[u] = True
        if u == 1 or best[u] > t0: break
        for v, l1, l2 in g[u]:
            if fet[v]: continue
            if best[u] + l1 <= t0 - t2: best[v] = min(best[v], best[u] + l1)
            else: best[v] = min(best[v], max(t0 - t1, best[u]) + l1, best[u] + l2)
            heappush(heap, (best[v], v))
    print(max(t0 - best[1], -1))