
# Aquesta implementació és ineficient, guarda tot el graf.
# Fa servir un DSU, estructura union-find, implementació senzilla.

def find(u):
    if leader[u] == u:
        return u
    leader[u] = find(leader[u])
    return leader[u]

def union(a, b):
    la = leader[a]
    lb = leader[b]
    if rank[la] > rank[lb]:
        leader[lb] = la
    elif rank[la] < rank[lb]:
        leader[la] = lb
    else:
        leader[lb] = la
        rank[la] += 1
    return

def dfs(node, ant):
    visited[node] = True
    if node == initial[0]:
        return True
    for w in G[node]:
        if w != ant and not visited[w] and dfs(w, node):
            ans.append(w)
            return True
    return False



line = lambda : list(map(int,input().split()))
for _ in range(int(input())):
    n, m = line()
    G = [[] for _ in range(n+1)]
    A = []
    for _ in range(m):
        u, v, w = line()
        G[u].append(v)
        G[v].append(u)
        A.append((w, u, v))
    A.sort()

    rank = [1]*(n+1)
    leader = [i for i in range(n+1)]
    
    while A:
        w, u, v = A.pop()
        if find(u) == find(v):
            W, U, V = w, u, v
        else:
            union(u, v)
    
    visited = [False]*(n+1)
    initial = [U]
    ans = [V]
    if dfs(V, U):
        print(W, len(ans))
        print(*ans)