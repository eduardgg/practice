from collections import deque
line = lambda : list(map(int, input().split()))

for _ in range(int(input())):
    n, m = line()
    G = [[] for _ in range(n+1)]
    C = [[] for _ in range(n+1)]
    for i in range(m):
        u, v, c = line()
        G[u].append(v)
        C[u].append(c)
        G[v].append(u)
        C[v].append(c)
    b, e = line()
    if b == e:
        print(0)
        continue

    fet = False
    rec = [False]*(n+1)
    dist = [-1]*(n+1)
    dist[b] = 0
    queue = deque()
    queue.append(b)
    while queue:
        v = queue.popleft()
        if rec[v]:
            continue
        rec[v] = True
        for i in range(len(G[v])):
            c = C[v][i]
            w = G[v][i]
            stack = [w]
            vistos = set()
            if dist[w] == -1:
                queue.append(w)
                dist[w] = dist[v] + 1
                if w == e:
                    fet = True
                    break
            while stack:
                u = stack.pop()
                vistos.add(u)
                for j in range(len(G[u])):
                    w, k = G[u][j], C[u][j]
                    if w not in vistos and k == c and dist[w] != dist[v]:
                    # L'última condició de l'if és la clau del problema,
                    # i per evitar time limit. Això filtra molt el nombre
                    # de casos, ja que només entra als nodes que tenen
                    # alguna possibilitat de millorar la distància.
                        stack.append(w)
                        if dist[w] == -1:
                            queue.append(w)
                            dist[w] = dist[v] + 1
                            if w == e:
                                fet = True
                                break
                if fet:
                    break
            if fet:
                break
        if fet:
            break
    # print(dist)
    print(dist[e])