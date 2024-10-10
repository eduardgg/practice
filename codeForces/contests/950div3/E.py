from collections import defaultdict

line = lambda : list(map(int, input().split()))

for _ in range(int(input())):
    n, m = line()
    a = [line() for _ in range(n)]
    b = [line() for _ in range(n)]
    
    hashra, hashca = defaultdict(int), defaultdict(int)
    hashrb, hashcb = defaultdict(int), defaultdict(int)
    
    for i in range(n):
        c = [e for e in a[i]]
        c.sort()
        hashra[hash(tuple(c))] += 1
        c = [e for e in b[i]]
        c.sort()
        hashrb[hash(tuple(c))] += 1
    
    for i in range(m):
        c = [a[j][i] for j in range(n)]
        c.sort()
        hashca[hash(tuple(c))] += 1
        c = [b[j][i] for j in range(n)]
        c.sort()
        hashcb[hash(tuple(c))] += 1

    if hashra == hashrb and hashca == hashcb:
        print("YES")
    else:
        print("NO")