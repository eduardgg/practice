
line = lambda : list(map(int, input().split()))

for _ in range(int(input())):
    n, m, k = line()
    a = line()
    v = [(a[i], i) for i in range(n)]
    v.sort()
    q = []
    for i in range(k//m):
        q.append((v[i][1], v[i][0], m))
    if (k%m != 0):
        q.append((v[k//m][1], v[k//m][0], k%m))
    q.sort()
    cost = 0
    incr = 0
    for (ind, val, qua) in q:
        cost += (val+incr)*qua
        incr += qua
    print(cost)
