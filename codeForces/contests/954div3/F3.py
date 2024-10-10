
# Versió iterativa per evitar recursion depth limit.
# Finalment, aquest codi sí que és acceptat.

def find_bridges(graph):

    n = len(graph)
    ids = [-1] * n
    low = [0] * n
    bridges = []
    id_counter = 0
    stack = []
    parent = [-1] * n

    for i in range(n):
        if ids[i] == -1:
            stack.append((i, iter(graph[i])))
            ids[i] = low[i] = id_counter
            id_counter += 1

            while stack:
                v, children = stack[-1]
                for to in children:
                    if ids[to] == -1:
                        stack.append((to, iter(graph[to])))
                        parent[to] = v
                        ids[to] = low[to] = id_counter
                        id_counter += 1
                        break
                    elif to != parent[v]:
                        low[v] = min(low[v], ids[to])
                else:
                    stack.pop()
                    if parent[v] != -1:
                        low[parent[v]] = min(low[parent[v]], low[v])
                        if ids[parent[v]] < low[v]:
                            bridges.append((parent[v], v))

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