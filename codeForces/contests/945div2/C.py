
for _ in range(int(input())):
    n = int(input())
    p = list(map(int, input().split()))
    taken = set()
    i = 1
    while i < n-1:
        if p[i] != 1:
            taken.add(p[i])
            i += 2
        else:
            i += 1
    nottaken = list({k for k in range(1, n+1) if k not in taken})
    taken = list(taken)
    taken.sort()
    nottaken.sort()

    maxim = n
    f = [-1]*(n+1)
    for e in taken:
        f[e] = maxim
        maxim -= 1
    maxim = n - len(taken)
    for e in nottaken:
        f[e] = maxim
        maxim -= 1

    a = [f[e] for e in p]
    print(*a)