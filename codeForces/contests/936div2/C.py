
line = lambda : list(map(int, input().split()))

for _ in range(int(input())):
    n, k = line()
    g = [[] for _ in range(n+1)]
    deg = [0 for _ in range(n+1)]
    for _ in range(n-1):
        u, v = line()
        g[u].append(v)
        g[v].append(u)
        deg[u] += 1
        deg[v] += 1

    """
    # Mètode per trobar els tamanys dels subarbres
    # (i un topological sort)
    stack = [1]
    size = [1]*(n+1)
    ant = [0]*(n+1)
    vist = [False]*(n+1)
    while stack:
        v = stack[-1]
        if vist[v]:
            stack.pop()
            for u in g[v]:
                if u != ant[v]:
                    size[v] += size[u]
        else:
            vist[v] = True
            for u in g[v]:
                if u != ant[v]:
                    ant[u] = v
                    stack.append(u)
    print(size)
    """

    dfs = [1]
    ant = [0]*(n+1)
    i = 0
    while i < len(dfs):
        u = dfs[i]
        for v in g[u]:
            if v != ant[u]:
                ant[v] = u
                dfs.append(v)
        i += 1
    # print(dfs)

    l, r = 1, n+1
    # l: últim conegut vàlid
    # r: primer conegut no vàlid
    # Quan r-l = 1, el resultat serà l.
    while r - l > 1:
        m = (l+r)//2
        size = [1]*(n+1)
        kk = k
        i = n-1
        while i >= 0:
            u = dfs[i]
            if size[u] < m:
                size[ant[u]] += size[u]
            else:
                kk -= 1
                if kk < 0:
                    break
            i -= 1
        if kk < 0 or i >= m:
            l = m
        else:
            r = m
    
    print(l)