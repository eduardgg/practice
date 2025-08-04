
import math
n = int(input())
r = list(map(int, input().split()))
ans = 0
for i in range(n-1):
    for j in range(i+1, n):
        # Comparem r[i] amb r[j]
        # Suposant i < j i ri <= rj tenim:
        # P[inversió] = P[j < i] =
        # suma(i: 1 -> ri) suma(j: 1 -> ri-1) 1/(ri·rj) =
        # (ri-1)·ri/2 · 1/(ri·rj) = (ri-1)/(2·rj)
        # Si, en canvi, i < j però ri > rj:
        # P[j < i] = (ri-rj)/ri·1 + rj/ri·(rj-1)/(2·rj) =
        # = 1 - rj/ri + (rj-1)/(2·ri) = 1 - (rj+1)/(2·ri)
        if r[i] <= r[j]: incr = (r[i]-1)/(2*r[j]) 
        else: incr = 1-(r[j]+1)/(2*r[i])
        ans += incr

ans = math.ceil(ans * 10**6) / 10**6
print(format(ans, "6f"))