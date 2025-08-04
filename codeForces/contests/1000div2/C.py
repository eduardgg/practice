
from collections import defaultdict

for _ in range(int(input())):

    n = int(input())
    t = defaultdict(list)
    d = [-1] + [0]*n

    for i in range(n-1):
        u, v = list(map(int, input().split()))
        t[u].append(v)
        t[v].append(u)
        d[u] += 1
        d[v] += 1

    top = []
    best = -1
    for i in range(n+1):
        if d[i] > best:
            top = [i]
            best = d[i]
        elif d[i] == best:
            top.append(i)
    
    if len(top) <= 2:
        comps = []
        for node in top:
            comps.append(d[node])
            d[node] = -1
            for v in t[node]:
                d[v] -= 1
            comps[-1] += max(d)-1
            d[node] = len(t[node])
            for v in t[node]:
                d[v] += 1
        print(max(comps))
    
    else:
        print(2*best-1)