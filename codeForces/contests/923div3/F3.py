
# ACCEPTED

# Aquesta implementació és similar a l'anterior,
# però fa servir una stack en lloc d'una funció recursiva
# que excedeix la profunditat permesa. Més eficient.

# A més, he fet una petita modificació de l'estructura
# union-find, en la que el "find" actualitza tots els leaders
# trobats pel camí, només duplicant el cost de la funció.
# He eliminat la funció union, ja que simplement consisteix en
# actualitzar un dels dos líders (no importa quin).

def find(u):
    v = []
    while leader[u] != u:
        v.append(u)
        u = leader[u]
    for e in v:
        leader[e] = u    
    return u

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
            leader[leader[u]] = leader[v]


    ant = [-1]*(n+1)
    stack = [V]
    while stack:
        v = stack.pop()
        if v == U:
            break
        for w in tree[v]:
            if w != ant[v]:
                stack.append(w)
                ant[w] = v 

    ans = []
    while v != -1:
        ans.append(v)
        v = ant[v]
    
    print(W, len(ans))
    print(*ans)