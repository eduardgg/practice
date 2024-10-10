
for _ in range(int(input())):
    n, k = list(map(int, input().split()))
    a = list(map(int, input().split()))
    a.sort()
    d = {}
    maxim = 0
    for e in a:
        d[e] = d.get(e, 0) + 1
        if d[e] > maxim:
            maxim = d[e]
    if k > maxim:
        print(n)
    else:
        print(k-1)