
line = lambda : list(map(int, input().split()))

for t in range(int(input())):
    n, k, d = line()
    a = line()
    v = line()

    coin = 0
    for i in range(n):
        if a[i] == i+1:
            coin += 1
    topcoin, topdia = coin, 0

    for dia in range(min(2*n, d-1)):
        for j in range(v[dia%k]):
            if a[j] == j:
                coin += 1
            elif a[j] == j+1:
                coin -= 1
            a[j] += 1
        if 2*coin - (dia+1) > 2*topcoin - topdia:
            topdia = dia+1
            topcoin = coin
    
    score = topcoin + (d-topdia-1)//2
    print(score)