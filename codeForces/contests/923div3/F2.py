
# Runtime error al test case 27.
# Probablement, la funció dfs supera la profunditat permesa.
# Refem el test amb una stack a F3.py, i funciona.

# Aquesta implementació és una mica millor
# No guarda tot el graf, sinó només un arbre que s'obté
# d'aquelles arestes que uneixen components diferents.
# Així el problema es redueix a trobar un (únic) camí
# d'un node a un altre en un arbre.

def find(u):
    v = []
    while leader[u] != u:
        v.append(u)
        u = leader[u]
    for e in v:
        leader[e] = u    
    return u

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
    if node == initial[0]:
        return True
    for w in tree[node]:
        if w != ant and dfs(w, node):
            ans.append(w)
            return True
    return False



line = lambda : list(map(int,input().split()))
for _ in range(int(input())):
    n, m = line()
    tree = [[] for _ in range(n+1)]
    rank = [1]*(n+1)
    leader = [i for i in range(n+1)]
    A = []
    for _ in range(m):
        u, v, w = line()
        A.append((w, u, v))
    A.sort()
    while A:
        w, u, v = A.pop()
        if find(u) == find(v):
            W, U, V = w, u, v
        else:
            tree[u].append(v)
            tree[v].append(u)
            union(u, v)
            # leader[leader[u]] = leader[v]

    
    initial = [U]
    ans = [V]
    if dfs(V, -1):
        print(W, len(ans))
        print(*ans)
