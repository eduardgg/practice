import bisect
from collections import defaultdict
line = lambda : list(map(int, input().split()))
for _ in range(int(input())):
    n, q = line()
    a = line()
    b = [0]
    pos = defaultdict(list)
    for i in range(n):
        b.append(b[-1]^a[i])
        pos[b[-1]].append(i+1)
    for _ in range(q):
        l, r = line()
        if not b[r]^b[l-1]:
            print("YES")
            continue
        i = bisect.bisect_left(pos[b[r]], l)
        j = bisect.bisect_left(pos[b[l-1]], pos[b[r]][i]+1)
        if j >= len(pos[b[l-1]]) or pos[b[l-1]][j] >= r:
            print("NO")            
        else:
            print("YES")
    print()