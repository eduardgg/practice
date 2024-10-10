
line = lambda : list(map(int, input().split()))

for _ in range(int(input())):
    n = int(input())

    if n == 1:
        print(1)
        print(1, 0)
        continue

    g = [[] for _ in range(n+1)]
    for i in range(n-1):
        u, v = line()
        g[u].append(v)
        g[v].append(u)
    
    dist = [0]*(n+1)
    ant = [0]*(n+1)
    stack = [1]
    primer = 0
    while stack:
        u = stack.pop()
        for v in g[u]:
            if v != ant[u]:
                ant[v] = u
                dist[v] = dist[u] + 1
                if dist[v] > dist[primer]:
                    primer = v
                stack.append(v)


    dist = [0]*(n+1)
    ant = [0]*(n+1)
    stack = [primer]
    ultim = 0
    while stack:
        u = stack.pop()
        for v in g[u]:
            if v != ant[u]:
                ant[v] = u
                dist[v] = dist[u] + 1
                if dist[v] > dist[ultim]:
                    ultim = v
                stack.append(v)
    
    diam = dist[ultim]
    mig = ultim
    for i in range(diam//2):
        mig = ant[mig]

    ans = diam//2 + 1 + (diam % 4 == 1)
    print(ans)

    if diam % 2 == 0:
        for i in range(ans):
            print(mig, i)
    else:
        mig2 = ant[mig]
        for i in range(ans//2):
            print(mig, 1+2*i)
            print(mig2, 1+2*i)