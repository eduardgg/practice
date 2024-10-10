
from heapq import heappop, heappush

line = lambda : list(map(int, input().split()))

for _ in range(int(input())):
    n, k = line()
    a = line()
    b = line()

    m = [(b[i], a[i]) for i in range(n)]
    m.sort()
    m = m[::-1]

    p = [0]
    for i in range(n-1, -1, -1):
        p.append(p[-1] + max(0, m[i][0]-m[i][1]))
    p = p[::-1]

    h = []
    ben = 0
    for i in range(k):
        heappush(h, -m[i][1])
        ben -= m[i][1]

    top = max(0, ben + p[k])

    for i in range(k, n):
        heappush(h, -m[i][1])
        ben -= m[i][1]
        ben -= heappop(h)
        top = max(top, ben + p[i+1])

    print(top)