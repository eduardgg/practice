
# Aquest és el cas CONTINU del problema
# Cada variable i és uniforme en l'interval [0, ri]
n = int(input())
r = list(map(int, input().split()))
ans = 0
for i in range(n-1):
    for j in range(i+1, n):
        # Comparem r[i] amb r[j]
        # Suposant i < j i ri < rj tenim:
        # P[inversió] = P[j < i] =
        # int(i: 0 -> ri) int(j: 0 -> i) 1/(ri·rj) =
        # ri^2/2 · 1/(ri·rj) = ri/(2·rj)
        # Si, en canvi, i < j però ri > rj:
        # P[rj < ri] = (ri-rj)/ri * 1 + rj/ri * 1/2 =
        # = 1 - rj/(2·ri), cosa que té sentit
        if r[i] >= r[j]: incr = 1 - r[j] / (2*r[i])
        else: incr = r[i] / (2*r[j])
        print(incr)
        ans += incr
print(ans)