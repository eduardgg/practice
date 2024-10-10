
from collections import defaultdict

line = lambda : list(map(int, input().split()))

for _ in range(int(input())):
    n = int(input())
    a = line()
    b = line()
    m = int(input())
    d = line()
    if d[-1] not in b:
        print("NO")
        continue
    D = defaultdict(int)
    for i in range(n):
        if b[i] != a[i]:
            D[b[i]] += 1
    for e in d:
        if e in D.keys():
            D[e] -= 1
    if any([v > 0 for v in D.values()]):
        print("NO")
    else:
        print("YES")