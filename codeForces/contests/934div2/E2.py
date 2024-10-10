
line = lambda : list(map(int, input().split()))

for _ in range(int(input())):
    n = int(input())

    if n == 1:
        print(1)
        print(1, 0)
        continue

    deg = [0]*(n+1)
    g = [[] for _ in range(n+1)]
    for i in range(n-1):
        u, v = line()
        g[u].append(v)
        g[v].append(u)
        deg[u] += 1
        deg[v] += 1
    
    leaves = []
    for v in range(1, n+1):
        if deg[v] == 1:
            leaves.append(v)
    
    nodes = n
    radi = 0
    old = set()
    while nodes > 2:
        radi += 1
        nodes -= len(leaves)
        new = []
        for l in leaves:
            old.add(l)
            for v in g[l]:
                if v not in old:
                    deg[v] -= 1
                    if deg[v] == 1:
                        new.append(v)
                    break
        leaves = new
    
    ans = radi + 1
    if nodes == 1:
        print(ans)
        for i in range(ans):
            print(leaves[0], i)

    else:
        if radi%2 == 0:
            ans += 1
        print(ans)
        for i in range(ans//2):
            print(leaves[0], 1+2*i)
            print(leaves[1], 1+2*i)