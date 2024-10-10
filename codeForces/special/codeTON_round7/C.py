
line = lambda : list(map(int, input().split()))

for _ in range(int(input())):
    n, x = line()
    a = line()
    b = line()

    ai = [(a[i], i) for i in range(n)]
    ai.sort()
    b.sort()
    b = b[x:] + b[:x]

    count = 0
    for i in range(n):
        if ai[i][0] > b[i]:
            count += 1

    if count == x:
        print("YES")
        bi = [-1]*n
        for i in range(n):
            bi[ai[i][1]] = b[i]
        print(*bi)
    
    else:
        print("NO")