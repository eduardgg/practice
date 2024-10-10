

# Petita millora, tot i que segueix fallant
# Implementat amb programació dinàmica per guardar
# les solucions completes del camí per cada V maximal
# (les menors usen el mateix camí, retallat per n).

from bisect import bisect_left

N = 1000001
primes = []
isprime = [True] * N
for i in range(2, N):
    if not isprime[i]: continue
    primes.append(i)
    for j in range(i*2, N, i):
        isprime[j] = False

nodes = [0]
for i in range(1, 1500):
    if i%2: nodes.append(1+i*(i+1)//2)
    else: nodes.append(1+i*(i+1)//2-(i-2)//2)





dp = [[0], [0, 0], [0, 0, 1, 1]] + [[] for _ in range(1500)]

for _ in range(int(input())):
    n = int(input())
    V = bisect_left(nodes, n)
    # Cal trobar un camí eulerià en V vèrtexos.

    if dp[V]:
        ans = [primes[e] for e in dp[V][:n]]
        print(*ans)
        continue

    g = [{i for i in range(V)} for _ in range(V)]
    if V%2 == 0:
        for i in range(V):
            if i%2: g[i-1].remove(i)
            else: g[i+1].remove(i)
    
    # Algorisme de Fleury per a camins eulerians
    dp[V] = [0] if V%2 else [1, 0]
    left = set()
    while len(dp[V]) < nodes[V]:
        v = dp[V][-1]
        if v in g[v]:
            dp[V].append(v)
            g[v].remove(v)
            if not g[v]: left.add(v)
            continue
        for w in g[v]:
            # Comprovem si v-w no és un pont:
            vistos = {v, w}
            dfs = [w]
            pont = True
            while dfs:
                node = dfs.pop()
                for neighbor in g[node]:
                    if neighbor == v and node != w:
                        pont = False
                        break
                    if not neighbor in vistos:
                        dfs.append(neighbor)
                        vistos.add(neighbor)
                if len(vistos) >= V - len(left):
                    pont = False
                    break
                if not pont:
                    break
            if not pont:
                g[w].remove(v)
                g[v].remove(w)
                if not g[w]: left.add(w)
                if not g[v]: left.add(v)
                dp[V].append(w)
                break

    ans = [primes[e] for e in dp[V][:n]]
    print(*ans)