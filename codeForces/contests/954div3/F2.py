
# dfs encara recursiu, però amb una sola variable d'entrada.
# El temps és inútil i el "parent" es memoritza al vector.
# Provem d'incrementar el recursion depth a 10**5.

import sys
sys.setrecursionlimit(10**5)

def find_bridges(graph):

    def dfs(v):
        nonlocal id_counter
        ids[v] = low[v] = id_counter
        id_counter += 1

        for to in graph[v]:
            if to == parent[v]:
                continue
            if ids[to] == -1:
                parent[to] = v
                dfs(to)
                low[v] = min(low[v], low[to])
                if ids[v] < low[to]:
                    bridges.append((v, to))
            else:
                low[v] = min(low[v], ids[to])
    
    n = len(graph)
    ids = [-1] * n
    low = [0] * n
    parent = [-1] * n
    bridges = []
    id_counter = 0

    for i in range(n):
        if ids[i] == -1:
            dfs(i)

    return bridges

for _ in range(int(input())):
    n, m = list(map(int, input().split()))
    g = [[] for _ in range(n)]
    for _ in range(m):
        u, v = list(map(int, input().split()))
        g[u-1].append(v-1)
        g[v-1].append(u-1)
    sizes = [1]*n
    pare = [-1]*n
    stack = [0]
    dfs = []
    while stack:
        u = stack.pop()
        for v in g[u]:
            if pare[v] == -1 and v != 0:
                pare[v] = u
                stack.append(v)
                dfs.append(v)
    while dfs:
        u = dfs.pop()
        sizes[pare[u]] += sizes[u]
    
    bridges = find_bridges(g)
    ans = n*(n-1)//2
    for (u, v) in bridges:
        x = min(sizes[u], sizes[v])
        ans = min(ans, x*(x-1)//2 + (n-x)*(n-x-1)//2)

    print(ans)