
from bisect import bisect_left

line = lambda : list(map(int, input().split()))

for _ in range(int(input())):
    n = int(input())
    n, d = line()
    pl, nl = {}, {}
    for i in range(1, n+1):
        x, y = line()
        pl[y-x].append(x)
        nl[y+x].append(x)
    for k in pl.keys(): pl[k].sort()
    for k in nl.keys(): nl[k].sort()
    
    found = set()
    for k in pl.keys():
        if len(pl[k]) == 1: continue
        for x in pl[k]:
            i = bisect_left(pl[k], x + d//2)
            if pl[k][i] == x + d//2:
                if k+d in pl.keys():
                    j = bisect_left(pl[k+d], x)
                    if pl[k+d][j] == x:
                        found = {(x, x+k), (x+d//2, x+d//2+k), (x, x+d+k)}
                        break
                    elif pl[k+d][j-1] + (k+d) >= k + x + d//2:
                        found = {(x, x+k), (x+d//2, x+d//2+k), (pl[k+d][j-1], pl[k+d][j-1]+k+d)}
                        break
                if k-d in pl.keys():
                    j = bisect_left(pl[k-d], x+d)
                    if pl[k-d][j] == x+d:
                        found = {(x, x-k), (x+d//2, x+d//2+k), (x, x+d+k)}
                        break

                    y = k + x + d//2
                    if x + d//2 <= pl[k+d][j] <= x + k:
                        found = True
                        break

        if found: break
    
    if found: continue

    # Repeat for pr.keys