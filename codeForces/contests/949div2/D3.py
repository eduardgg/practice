
# Aquest algorisme usa el fet que el graf és complet, i
# explora totes les arestes del graf fent servir, de
# manera greedy i per cada vèrtex on es troba, una
# direcció que va augmentant al voltant del polígon.

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



for _ in range(int(input())):
    n = int(input())
    V = bisect_left(nodes, n)

    i = 0
    cami = [0]
    dir = [0 for _ in range(V)]
    while len(cami) < n and ((i < V//2 and dir[i] <= V//2) or (V//2 <= i and dir[i] < (V+1)//2)):
        new = (i + dir[i]) % V
        dir[i] += 1
        cami.append(new)
        i = new

    ans = [primes[e] for e in cami]
    print(*ans)