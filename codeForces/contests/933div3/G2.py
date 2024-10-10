
from collections import deque, defaultdict
line = lambda : list(map(int, input().split()))

for _ in range(int(input())):

    n, m = line()
    bg = defaultdict(list)
    for i in range(m):
        u, v, c = line()
        bg[u].append(n+c)
        bg[v].append(n+c)
        bg[n+c].append(u)
        bg[n+c].append(v)
    b, e = line()
    if b == e:
        print(0)
        continue

    fet = False
    dist = {b: 0}
    q = deque([b])
    while q:
        v = q.popleft()
        for w in bg[v]:
            if w not in dist.keys():
                dist[w] = dist[v] + 1
                q.append(w)
                if w == e:
                    fet = True
                    break
        if fet:
            break

    # print(dist)
    ans = dist[e]//2
    print(ans)