
for _ in range(int(input())):
    n = int(input())
    a = [0] + list(map(int, input().split()))
    p = [-1, -1] + list(map(int, input().split()))
    fills = [[] for _ in range(n+1)]
    for i in range(2, n+1):
        fills[p[i]].append(i)
    minim = [10**9]*(n+1)
    dfs = []
    stack = [1]
    while stack:
        v = stack.pop()
        for u in fills[v]:
            dfs.append(u)
            stack.append(u)
    while dfs:
        u = dfs.pop()
        if not fills[u]:
            minim[u] = a[u]
        elif a[u] < minim[u]:
            minim[u] = a[u] + (minim[u] - a[u])//2
        minim[p[u]] = min(minim[p[u]], minim[u])
    print(a[1] + minim[1])